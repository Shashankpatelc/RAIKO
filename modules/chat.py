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
            data = json.load(file)
            # print(data[0]['content']) # The Passing Data to the model
            if data:
                conversation.append({
                    "role": "system",
                    "content": f"Previous conversation summary: {data[0]['content']}"
                })
                response: ollama.ChatResponse = ollama.chat(model=Model, messages=conversation)
                # print(response.message.content) # The response after the passing the summanry
    except:
        print("Some Error while recovering the previous chat")
        return None

# Use to get the response from the model
def get_respond(user_input):
    # Update the user conversation
    conversation.append({
            'role' : 'user',
            'content' : user_input
        })
    # Update the Model response
    response: ollama.ChatResponse = ollama.chat(model=Model, messages=conversation)
    conversation.append(
        {
        'role' : 'model',
        'content' : response.message.content
        }
    )
    return response.message.content

# Main where each function is called
def main():
    user_input = model_input.get() # get the user input
    print()

    # Exit the model
    if user_input.lower() == "bye":
        # Get the summary of the chat and pass to the new list
        summary = [{
            "role": "system",
            "content": get_respond("Summarize the whole chat so you can remember it.")
        }]
        # Write the summary to the memory.json file
        with open('memory.json', 'w') as file:
            json.dump(summary, file)
        return False
    # Check the commands
    elif commands.check(user_input):
        print("Commmand found..............")
    else:
        # Get the response from model
        replay = get_respond(user_input)
        # Show the Output
        model_output.put(replay)
    return True
