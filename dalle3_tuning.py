from prompt import Prompt
from openai import OpenAI
from config import *

class Creator:
    def __init__(self, prompt, model) -> None:
        self.trasfomer = Prompt("gpt-4-turbo-preview", 250, "Do short prompts for dalle-3 in english, with all details")
        self.prompt = prompt
        self.model = model
        self.api_key = OPENAI_KEY
        self.dalle3 = OpenAI(api_key=OPENAI_KEY)
        
    def prompt_conver(self):
        converted_prompt = self.trasfomer.response(self.prompt)
        return converted_prompt
    
    
        
    def image_gen(self):
        image = self.dalle3.images.generate(
            model=self.model,
            prompt=str(self.prompt_conver()),
            n=1,
            size="1024x1024",
            style="vivid",
            
            
        )
        return image.data[0].url