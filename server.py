import asyncio
import websockets
import json

# Function to handle incoming WebSocket connections
async def handler(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        payload = data.get('payload')
        response = {}

        if payload == '-alert(xss)-':
            response['valid'] = True
            response['flag'] = 'Anzen CTF{alert}'
        else:
            response['valid'] = False
        
        await websocket.send(json.dumps(response))

# Start the WebSocket server
start_server = websockets.serve(handler, 'localhost', 8080)

# Run the server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
