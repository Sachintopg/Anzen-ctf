import asyncio
import websockets
import json

async def echo(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        payload = data.get("payload")
        
        # Validate payload
        if payload == '-alert(xss)-':
            response = {
                "valid": True,
                "flag": "Anzen CTF{alert}"
            }
        else:
            response = {
                "valid": False
            }
        
        await websocket.send(json.dumps(response))

start_server = websockets.serve(echo, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
print("WebSocket server is running on ws://localhost:8080")
asyncio.get_event_loop().run_forever()
