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
    disprover = 0
    sugg_char = None
    sugg_weapon = None
    sugg_room = None

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

        if 'make_suggestion' in actions:
            internal.handle_suggestion(actions)

        if 'make_accusation' in actions:
            internal.handle_accusation(actions)

        if 'check_suggestion' in actions:
            internal.handle_suggestion_input(actions)


    @staticmethod
    def begin_game():
        # initialize the game
        internal.current_game.initialize_game()
        ServerProtocol.message_all_players(Display.display_board(internal.current_game.board))
        internal.begin_turn(1)

    @staticmethod
    def join_game(actions, transport):
        data = actions.get('join_game').split(',')
        player_name = data[0]
        character = data[1]
        internal.current_players[internal.num_players + 1] = {"name": player_name,
                                                              "character": character,
                                                              "transport": transport}

        if internal.current_game is None:
            internal.current_game = Game()
            expected_players = data[2]
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
            suggestion_possible = True

        for space in adjacent_spaces:
            if isinstance(space, Room):
                potential_moves[count] = space.space_id
                count += 1
            elif not space.occupied:
                potential_moves[count] = space.space_id
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
            internal.make_suggestion(player)
        elif 'accusation' in turn:
            internal.make_accusation(player)
        else:
            space_id = turn
            space_type = internal.current_game.move_player_to_space_by_id(space_id, player_character, location)

            ServerProtocol.message_all_players("\n" + player_name + " moved " + player_character + " to " +
                                               space_id + ".\n")

            ServerProtocol.message_all_players(Display.display_board(internal.current_game.board))

            if space_type is 'Room':
                internal.make_suggestion(player, space_id)
            else:
                internal.finish_turn()

    @staticmethod
    def make_suggestion(player, space_id):
        player_transport = player.get("transport")

        ServerProtocol.message_current_player(player_transport, "\nPlease make a suggestion in the :" + space_id)

    @staticmethod
    def handle_suggestion(suggestion):
        player = internal.current_players.get(internal.active_player)
        player_name = player.get("name")

        pieces = suggestion.get('make_suggestion').split(',')
        internal.sugg_char = pieces[0]
        internal.sugg_weapon = pieces[1]
        internal.sugg_room = pieces[2]

        suggestion_string = "\n" + player_name + " suggested: " + internal.sugg_char + " in the " + internal.sugg_room + \
                            " with the " + internal.sugg_weapon + ".\n"

        ServerProtocol.message_all_players(suggestion_string)

        internal.check_suggestions(internal.active_player, internal.sugg_char, internal.sugg_weapon, internal.sugg_room)

        internal.finish_turn()

    @staticmethod
    def check_suggestions(player_num, char, weapon, room):
        curr_player = player_num
        if player_num < internal.expected_players:
            curr_player += 1
        else:
            curr_player = 1

        internal.prompt_player(curr_player, char, weapon, room)


    @staticmethod
    def prompt_player(player_num, char, weapon, room):
        player = internal.current_players.get(player_num)
        player_transport = player.get("transport")

        ServerProtocol.message_current_player(player_transport,
                                              "\nDo you have any information to share about the suggestion?" + char +
                                              "?" + weapon + "?" + room)
        return True

    @staticmethod
    def handle_suggestion_input(actions):
        pieces = actions.get('check_suggestion').split(',')
        char = pieces[0]
        weapon = pieces[1]
        room = pieces[2]

        if char is '' and weapon is '' and room is '':
            response = None
        elif char is not '':
            response = char
        elif weapon is not '':
            response = weapon
        elif room is not '':
            response = room

        dis = internal.current_players.get(internal.disprover)
        active = internal.current_players.get(internal.active_player)

        if response is not None:
            ServerProtocol.message_current_player(dis.get("transport"), "\n" + dis.get("name") +
                                                  " can disprove:" + response)
            ServerProtocol.message_all_players("\n" + dis.get("name") + " was able to disprove part of " +
                                               active.get("name") + "'s suggestion.\n")
        else:
            if internal.disprover < internal.expected_players:
                internal.disprover += 1
            else:
                internal.disprover = 1

            if internal.disprover != internal.active_player:
                internal.prompt_player(internal.disprover, internal.sugg_char, internal.sugg_weapon, internal.sugg_room)
            else:
                internal.finish_turn()

    @staticmethod
    def make_accusation(player):
        player_transport = player.get("transport")

        ServerProtocol.message_current_player(player_transport, "\nPlease make an accusation.")

    @staticmethod
    def handle_accusation(suggestion):
        player = internal.current_players.get(internal.active_player)
        player_name = player.get("name")

        pieces = suggestion.get('make_accusation').split(',')
        char = pieces[0]
        weapon = pieces[1]
        room = pieces[2]

        result = internal.check_accusation(char, weapon, room)

        if result is True:
            ServerProtocol.message_all_players("\n" + player_name + " correctly accused " + char + " in the " + room +
                                               " with the " + weapon + ".\n")
            internal.terminate_game()
        else:
            ServerProtocol.message_all_players("\n" + player_name + " made an invalid accusation. They are no longer "
                                                                    "active in the game.\n")
            internal.remove_player_from_game(internal.active_player)

            if len(internal.current_players.keys()) == 1:
                internal.terminate_game()

        internal.finish_turn()

    @staticmethod
    def check_accusation(char, weapon, room):
        casefile = internal.current_game.case_file
        return casefile.check_solution(char, weapon, room)

    @staticmethod
    def finish_turn():
        sys.stdout.flush()

        if internal.active_player < internal.expected_players:
            internal.active_player += 1
        else:
            internal.active_player = 1

        if internal.current_game is not None:
            internal.begin_turn(internal.active_player)

    @staticmethod
    def go_to_next_valid_player():
        player_valid = False
        while not player_valid:
            internal.active_player += 1
            if internal.active_player not in internal.current_players:
                continue
            else:
                player_valid = True

    @staticmethod
    def remove_player_from_game(player_num):
        del internal.current_players[player_num]


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



