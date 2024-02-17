import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import dalle3_tuning as d3

class Screen:
    def __init__(self, title, size):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size)
        self.root.wm_iconbitmap("icon_dalle3.ico")
        self.setup_widgets()
    
    def setup_widgets(self):
        
        self.prompt_entry = tk.Entry(self.root, width=50)
        self.prompt_entry.pack(pady=20)
        
        
        submit_button = tk.Button(self.root, text="Generar Imagen", command=self.submit_prompt)
        submit_button.pack(pady=10)
        
        
        
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=20)

    def submit_prompt(self):
        
        prompt = self.prompt_entry.get()
        
        model = d3.Creator(prompt=prompt, model="dall-e-3")
       
        image_url = model.image_gen()
        
        
    
        self.display_image(image_url)

    
    
    def display_image(self, image_url):
        
        response = requests.get(image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        
        
        img = img.resize((800, 800), Image.ANTIALIAS)
        
        
        img_tk = ImageTk.PhotoImage(img)
        
        
        self.image_label.configure(image=img_tk)
        self.image_label.image = img_tk 
         
    def run(self):
        self.root.mainloop()

        
