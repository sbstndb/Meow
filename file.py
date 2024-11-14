from prompt_toolkit import PromptSession
from prompt_toolkit.completion import PathCompleter

# Configurez le compléteur de chemin de fichiers
file_completer = PathCompleter(only_directories=False)

# Créez une session interactive
session = PromptSession(completer=file_completer)

while True:
    try:
        # Essayez d'entrer un chemin de fichier pour voir si le PathCompleter fonctionne
        user_input = session.prompt('Sélectionnez un fichier: ')
        print(f"Vous avez sélectionné: {user_input}")
    except (KeyboardInterrupt, EOFError):
        print("Sortie...")
        break

