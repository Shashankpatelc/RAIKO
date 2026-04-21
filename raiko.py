import modules.chat as chat
from google import genai
import config 

client = genai.Client(api_key=config.API_KEY)

cond = True

# Main loop for the coversation
while cond:
    cond = chat.main()
    