def check(user_input):
    if user_input[:3].count("command"):
        handle(user_input)
        return True
    else:
        return False
    

cmd = ""
def handle(user_input):
    cmd = user_input[user_input.index("command")+1:]
