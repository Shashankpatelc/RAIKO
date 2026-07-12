import ollama
import config

def check(user_input):
    print("cmd is here")
    formated_input = user_input.split()
    print(formated_input)
    if formated_input[1] == "command" or formated_input[1] == "cmd":
        handle(user_input)
        return True
    else:
        return False
    
cmd = ""
def handle(user_input):
    cmd = user_input[user_input.index("cmd")+1:]
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
            f"Input Request: {cmd} " \
            "Output:"
        }
    ]

    cmd_to_exe : ollama.ChatResponse = ollama.chat(
        model=config.Model,
        messages=prompt
    )

    print(cmd_to_exe)
