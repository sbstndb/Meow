import os
import google.generativeai as genai



model_name = 'gemini-1.5-flash'

generation_config = {
    "temperature":0.05,
    "top_p":0.95,
    "top_k":0,
    "max_output_tokens":8192
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]


def init_model():
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key :
        raise ValueError("Can't find API key. Please add it to your variable GEMINI_API_KEY. ")
    genai.configure(api_key = api_key)
    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
        safety_settings=safety_settings)
    return model 

