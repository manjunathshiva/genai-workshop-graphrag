import os
from colorama import init, Fore, Style
init()

env_file_exists = os.path.exists('.env')
if not env_file_exists:
    print(Fore.RED + "Environment .env file not found.")
    print(Fore.BLUE + "Goto https://graphacademy.neo4j.com/courses/genai-workshop/1-knowledge-graphs-vectors/1-getting-started/ for instructions on setting up your environment.")
    print(Style.RESET_ALL)