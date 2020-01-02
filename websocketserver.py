import asyncio
import websockets


async def joke(websocket, path):
    response = await websocket.recv()
    if response == "J":
        a = "here is the joke u want to listen"
        await websocket.send(a)
        b = "What happens to a frog's car when it breaks down?"
        c = "It gets toad away."
        await websocket.send(b)
        await asyncio.sleep(5)
        await websocket.send(c)
    elif response == "R":
        a = "here is the Riddle For You"
        await websocket.send(a)
        b = "Can you guess what is at the end of a rainbow??"
        await websocket.send(b)

        await asyncio.sleep(5)
        c = "The letter ‘W’"
        await websocket.send(c)
    else:
        a = "U have entered Invalid Response"
        await websocket.send(a)
        b = "Re run Webclient"
        await websocket.send(b)
        c = "Re Run WEbclient"
        await websocket.send(c)


start_server = websockets.serve(joke, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
