from configuration import *
from interaction import * 
#from read_code import *
#from analyze_code import * 

import os
import google.generativeai as genai



def main() : 
    console = Console()
    model = init_model()
    convo = model.start_chat(history=[])

    meow_loop(console, convo) ; 
    

if __name__ == "__main__":
    main()


