import asyncio
import json


def begin_game():

    while True:
        try:
            num_players = input("\nHow many players will be joining the game?\n")
            name = input("\nPlease enter your name:\n")
            char = input("\nPlease choose a character from the following: Miss Scarlet, Mrs White, Mrs Peacock, "
                         "Col Mustard, Prof Plum, Mr Green \n")

            vars = name + "," + char + "," + num_players

            break

        except ValueError:
            print("\nSorry, I didn't understand that.")
            # better try again... Return to the start of the loop
            continue

    print("\nThanks for starting a game!\n")

    sys_call = {"join_game": vars}

    return json.dumps(sys_call)


def make_selection(message):
    while True:
        try:
            selection = input(message)
            break

        except ValueError:
            print("\nSorry, I didn't understand that.")
            # better try again... Return to the start of the loop
            continue

    sys_call = {"turn_selection": selection}
    return json.dumps(sys_call)


def make_suggestion():
    while True:
        try:
            char = input("\nPlease choose a character from the following: Miss Scarlet, Mrs White, Mrs Peacock, "
                         "Col Mustard, Prof Plum, Mr Green \n")
            weapon = input("\nPlease choose a weapon from the following: Rope, Lead Pipe, Knife, Wrench, "
                           "Candlestick, Revolver \n")
            room = input("\nPlease choose a room from the following: Study, Hall, Lounge, Library, Billiard Room,"
                         "Dining Room, Conservatory, Ballroom, Kitchen \n")

            vars = char + "," + weapon + "," + room

            break

        except ValueError:
            print("\nSorry, I didn't understand that.")
            # better try again... Return to the start of the loop
            continue

    print("\nGreat suggestion!\n")

    sys_call = {"make_suggestion": vars}

    return json.dumps(sys_call)


def handle_message(message):
    if 'Please enter the number associated with your chosen move:' in message:
        val = make_selection(message)
    elif 'Please make a suggestion' in message:
        val = make_suggestion()
    else:
        print(message)
        val = None
    return val


class ClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost, loop):
        self.message = message
        self.loop = loop
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(self.message.encode())
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        value = handle_message(message)
        if value is not None:
            self.transport.write(value.encode())

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)


async def main(vars):
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()

    transport, protocol = await loop.create_connection(
        lambda: ClientProtocol(vars, on_con_lost, loop),
        '54.183.147.155', 8888)

    # Wait until the protocol signals that the connection
    # is lost and close the transport.
    try:
        await on_con_lost
    finally:
        transport.close()

if __name__ == "__main__":
    vars = begin_game()

    asyncio.run(main(vars))

