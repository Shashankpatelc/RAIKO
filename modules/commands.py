import ollama
# import config

def check(user_input):
    print("cmd is here")    
    formated_input = user_input.split() # Split the input as a list
    print(formated_input)
    if formated_input[1] == "command" or formated_input[1] == "cmd":    # check if it is a command or not
        handle(' '.join(formated_input[2:]))        # passing the main command to the model
        return True
    else:
        return False
    
def handle(user_input):
    cmd = user_input
    prompt = [
        {
            "role" : "system",
            "content" : "You are a strict Windows automation engine. " \
            "Your only job is to translate a natural language request into a standalone, executable Python script using standard libraries (like os, subprocess, shutil, sys). " \
            "CRITICAL CONSTRAINTS: " \
            "1. Output ONLY valid, raw, executable Python code.  " \
            "2. Do NOT use markdown code blocks (do not wrap code in ```python ... ```). " \
            "3. Do NOT include any explanations, introduction, greetings, or conversational filler. " \
            "4. Assume the script runs on Windows. For example, use 'cls' instead of 'clear', and use proper Windows paths or commands. " \
            "5. If the request cannot be turned into a script, output only the phrase: print(\"Command not recognized\") " \
            "6. Never use print() statements to simulate a command. You must write the actual execution logic."
            "7. To launch applications, ALWAYS use os.system('start <app_name>'). Do not use os.startfile()."
            f"Input Request: {cmd} " \
            "Output:"
        }
    ]

    cmd_to_exe : ollama.ChatResponse = ollama.chat(
        # model=config.Model,
        model="qwen2.5-coder:1.5b",
        messages=prompt
    )

    raw_output = cmd_to_exe.message.content         # Model output code
    exe_cmd = raw_output.replace("```python","").replace("```","")      # Filtered code
    print(exe_cmd)

    # Try catch to execute the command and any error try not to break the whole code
    try:
        print("Command is try to execute")
        exec(exe_cmd)       # Execute the Code
    except Exception as e:
        print("Failed to Execute the command")
        print(f"Error is : {e}")
    

check("raiko cmd write i am raiko to tril.txt file ")