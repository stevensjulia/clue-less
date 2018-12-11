from clueless.game import Game
from clueless.board import Room
from utils.display import Display
import asyncio
import json
import sys


class internal:
    current_players = {}
    current_game = None
    num_players = 0
    expected_players = 0
    remaining_characters = ["Miss Scarlet", "Mrs White", "Mrs Peacock", "Col Mustard", "Prof Plum", "Mr Green"]
    active_player = 1

    current_turn_options = {}


    @staticmethod
    def handle_input(message, transport):
        actions = json.loads(message)

        if 'join_game' in actions:
            internal.join_game(actions, transport)

        if 'terminate_game' in actions:
            internal.terminate_game()

        if 'enter_game' in actions:
            ServerProtocol.message_current_player(
                transport, "Please choose from the remaining characters: " + str(internal.remaining_characters))

        if 'begin_turn' in actions:
            internal.begin_turn(internal.active_player)

        if 'turn_selection' in actions:
            internal.take_turn(actions)


    @staticmethod
    def begin_game():
        # initialize the game
        internal.current_game.initialize_game()
        ServerProtocol.message_all_players(Display.display_board(internal.current_game.board))
        internal.begin_turn(0)

    @staticmethod
    def join_game(actions, transport):
        data = actions.get('join_game').split(',')
        player_name = data[0]
        character = data[1]
        if internal.num_players == 0:
            expected_players = data[2]
        internal.current_players[internal.num_players] = {"name": player_name,
                                                          "character": character,
                                                          "transport": transport}

        if internal.current_game is None:
            internal.current_game = Game()
            internal.expected_players = int(expected_players)

        # add player to game
        internal.current_game.add_player(player_name, character)
        internal.num_players += 1
        internal.remaining_characters.remove(character)

        players_left_to_join = str(internal.expected_players - internal.num_players)

        if internal.num_players == internal.expected_players:
            ServerProtocol.message_all_players(
                '{0} just joined the game as {1}. Everyone has joined! Lets begin.'.format(player_name, character))
            internal.begin_game()
        else:
            ServerProtocol.message_all_players(
                '{0} just joined the game as {1}. Waiting for {2} more player(s) to join!'.format(
                    player_name, character, players_left_to_join))

    @staticmethod
    def terminate_game():
        ServerProtocol.message_all_players('Please play again!')
        ServerProtocol.close_connections()

        internal.current_players = {}
        internal.current_game = None
        internal.num_players = 0
        internal.expected_players = 0

    @staticmethod
    def begin_turn(player_num):
        # get available moves
        # get adjacent spaces
        # get any secret passageways
        # make accusation
        # make suggestion

        potential_moves = {}
        count = 1
        suggestion_possible = False

        player = internal.current_players.get(player_num)
        player_character = player.get("character")
        player_transport = player.get("transport")
        location = internal.current_game.board.locate_character(player_character)

        adjacent_spaces = location.adjacent_spaces
        if isinstance(location, Room):
            secret_passage = location.secret_passage
            suggestion_possible = True
        else:
            secret_passage = None

        for space in adjacent_spaces:
            if isinstance(space, Room):
                potential_moves[count] = space.space_id
                count += 1
            elif not space.occupied:
                potential_moves[count] = space.space_id
                count += 1

        if secret_passage is not None:
            potential_moves[count] = secret_passage
            count += 1

        if suggestion_possible:
            potential_moves[count] = "Make a suggestion."
            count += 1

        potential_moves[count] = "Make an accusation"

        internal.current_turn_options = potential_moves

        ServerProtocol.message_current_player(player_transport,
                                              "\nIt's your turn!" +
                                              "\nPlease enter the number associated with your chosen move: " +
                                              "\n" + json.dumps(potential_moves) + "\n")


    @staticmethod
    def take_turn(actions):
        player = internal.current_players.get(internal.active_player)
        player_name = player.get("name")
        player_character = player.get("character")
        location = internal.current_game.board.locate_character(player_character)

        data = actions.get('turn_selection')
        turn = internal.current_turn_options.get(int(data))

        if 'suggestion' in turn:
            internal.make_suggestion()
        elif 'accusation' in turn:
            internal.make_accusation()
        else:
            space_id = turn
            internal.current_game.move_player_to_space_by_id(space_id, player_character, location)


            ServerProtocol.message_all_players("\n" + player_name + " moved " + player_character + " to " +
                                               space_id + ".\n")

            ServerProtocol.message_all_players(Display.display_board(internal.current_game.board))
            sys.stdout.flush()

            if internal.active_player < internal.expected_player:
                internal.active_player += 1
            else:
                internal.active_player = 1

            if internal.current_game is not None:
                internal.begin_turn(internal.active_player)

    @staticmethod
    def make_suggestion():
        pass

    @staticmethod
    def make_accusation():
        pass



class ServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport
        self.peername = peername

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        internal.handle_input(message, self.transport)

    @staticmethod
    def message_all_players(message):
        for k in internal.current_players:
            record = internal.current_players.get(k)
            curr_transport = record.get("transport")
            curr_transport.write(message.encode())
        sys.stdout.flush()

    @staticmethod
    def message_current_player(curr_transport, message):
        curr_transport.write(message.encode())

    @staticmethod
    def close_connections():
        for k in internal.current_players:
            record = internal.current_players.get(k)
            curr_transport = record.get("transport")
            curr_transport.close()


async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: ServerProtocol(),
        '172.31.15.89', 8888)

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())



