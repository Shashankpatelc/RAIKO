from google import genai
from config import API_KEY
from modules import model_input
from modules import model_output

client = genai.Client(api_key=API_KEY)
Model = "gemini-3-flash-preview"

cond = True

def get_respond(user_input):
    response = client.models.generate_content(
        model = Model,
        contents = user_input 
    )
    return response.text

def main():
    user_input = model_input.get()
    print()
    if user_input.lower() == "bye":
        return False
    model_output.put(get_respond(user_input))
    return True
