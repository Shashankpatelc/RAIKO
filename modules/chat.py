from modules import model_input
from modules import model_output
from modules import commands

import ollama
import config 
import json

# Model Credential
Model = config.Model

conversation = []
cond = True

# Use to load the prevous chat to model
def load_memory():
    try:
        with open('memory.json', 'r') as file:
            summary = json.load(file)
            ollama.chat(model=Model, messages=summary)
    except:
        return None

# Use to get the response from the model
def get_respond(user_input):
    conversation.append({
        'role' : 'user',
        'content' : user_input
        })
    response: ollama.ChatResponse = ollama.chat(model=Model, messages=conversation)
    conversation.clear()
    return response.message.content

# Main where each function is called
def main():
    user_input = model_input.get() # get the user input
    print()

    # Exit the model
    if user_input.lower() == "bye":
        summary = {
             "summary" :  get_respond("Summarize the whole chat so you can remember that when i pass that in a new chat.")
            }
        with open('memory.json', 'w') as file:
            json.dump(summary, file)
        return False
    elif commands.check(user_input):
        print("Commmand found..............")
    else:
        # Get the response from model
        replay = get_respond(user_input)

        # Show the Output
        model_output.put(replay)
    return True
