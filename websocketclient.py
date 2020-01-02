import asyncio
import websockets


async def joke():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        response = input("listen an joke Press J and Press R for Riddle ")

        await websocket.send(response)
        print(f"> {response}")

        a = await websocket.recv()
        print(f"< {a}")
        b = await websocket.recv()
        print(f"< {b}")
        c = await websocket.recv()
        print(f"< {c}")


asyncio.get_event_loop().run_until_complete(joke())
