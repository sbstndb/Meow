from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
import os

# Set up words for autocompletion
words = ['read_file', 'read_folder', 'give_optims', 'give_bugs', 'give_guidelines', 'give_resume']
completer = WordCompleter(words, ignore_case=True)

# Create a history file path
history_file = os.path.expanduser("~/.input_history")  # save history in home directory

# Initialize a PromptSession with history and autocomplete features
session = PromptSession(history=FileHistory(history_file), completer=completer)

while True:
    try:
        # Prompt the user for input with autocomplete and persistent history
        user_input = session.prompt('Please enter your command :  ')
        print(f'You entered: {user_input}')
    except (KeyboardInterrupt, EOFError):
        print("Exiting...")
        break

