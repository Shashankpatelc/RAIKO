from google import genai
from modules import model_input
from modules import model_output

import config 
import json

# Model Credential
client = genai.Client(api_key=config.API_KEY)
Model = config.Model
chat_session = client.chats.create(model=Model)  # Create a chat session 

cond = True

# Use to load the prevous chat to model
def load_memory():
    try:
        with open('memory.json', 'r') as file:
            summary = json.load(file)
            chat_session.send_message(f"Here the summary of the previous conversation {summary['summary']}").text
    except:
        return None

# Use to get the response from the model
def get_respond(user_input):
    response = chat_session.send_message(user_input)
    return response.text

# Main where each function is called
def main():
    user_input = model_input.get() # get the user input
    print()

    # Exit the model
    if user_input.lower() == "bye":
        summary = {
             "summary" :  chat_session.send_message("Summarize the whole chat so you can remember that when i pass that in a new chat.").text
            }
        with open('memory.json', 'w') as file:
            json.dump(summary, file)
        return False

    # Get the response from model
    replay = get_respond(user_input)

    # Show the Output
    model_output.put(replay)
    return True
