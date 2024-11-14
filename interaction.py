from rich import text
from rich.markdown import Markdown
from rich.console import Console

import readline


def talk(convo):
    meow = input("""\033[47m\033[30mMeow ?\033[0m """)
    print("\033[44m\033[37mWaitign for GeminiCat ... \033[0m")
    response = convo.send_message(meow)
    return response

def read(console, response):
    console.print(Markdown(response.text))

def meow_loop(console, convo):
    while True:
        response = talk(convo)
        read(console, response)

