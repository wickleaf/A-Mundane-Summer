default chat_memory = []

init python:
    import requests

    def get_ai_reply(player_text):
        proxy_url = "http://127.0.0.1:5000/chat"
        
        chat_memory.append({"role": "user", "text": player_text})
        
        payload = {"history": chat_memory}
        
        response = requests.post(proxy_url, json=payload)
        data = response.json()
        ai_reply = data["reply"]
        
        chat_memory.append({"role": "model", "text": ai_reply})
        
        return ai_reply

define s = Character("Hana")

label start:
    scene bg room
    
    "Connected to local Flask proxy on port 5000."
    
    s "Welcome to the shop. State your business."

label test_loop:
    $ user_input = renpy.input("Say something:")
    
    if user_input == "quit":
        return
        
    $ generated_response = get_ai_reply(user_input)
    
    s "[generated_response]"
    
    jump test_loop