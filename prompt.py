from openai import OpenAI
from config import * 

class Prompt:
    def __init__(self, model, tokens, system) -> None:
        self.opeani = OpenAI(api_key=OPENAI_KEY)
        self.model = model
        self.tokens = tokens
        self.system = system
        
    def response(self, txt):
        message = self.opeani.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system},
                {"role": "user", "content": txt}
            ],
            max_tokens=self.tokens
        )
        return message.choices[0].message.content
        
    
        