import asyncio
import json


def join_game(message):

    while True:
        try:
            name = input("\nThanks for joining! Please enter your name:\n")
            char = input("\n" + message + "\n")

            vars = name + "," + char

            break

        except ValueError:
            print("\nSorry, I didn't understand that.")
            # better try again... Return to the start of the loop
            continue

    sys_call = {"join_game": vars}

    return json.dumps(sys_call)


def handle_message(message):
    if 'Please choose from the remaining characters:' in message:
        val = join_game(message)
        return val
    else:
        print(message)


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
    sys_call = {"enter_game": None}

    asyncio.run(main(json.dumps(sys_call)))

