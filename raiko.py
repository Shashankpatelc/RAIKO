import modules.chat as chat

cond = True

chat.load_memory()
# Main loop for the coversation
while cond:
    cond = chat.main()
    