import websocket
import json

old_metadata = ""

def on_message(wsapp, message):
    global old_metadata
    jsontxt = json.loads(message)
    metadata = jsontxt['menu']['bm']['metadata']
    if metadata != old_metadata:
        text = f'Listening to {metadata["title"]}[{metadata["difficulty"]}] by {metadata["artist"]}'
        print(text)
        with open("nowplaying.txt", "w") as f:
            f.write(text)
        old_metadata = metadata

wsapp = websocket.WebSocketApp("ws://localhost:24050/ws", on_message=on_message)
wsapp.run_forever()