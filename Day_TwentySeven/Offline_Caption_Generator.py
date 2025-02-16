import cv2
import numpy as np
import torch
import clip
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import pyperclip
import pyttsx3
import os
import json
import googletrans

# Load CLIP model and tokenizer
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)
translator = googletrans.Translator()

# Initialize text-to-speech engine
engine = pyttsx3.init()

history_file = "caption_history.json"
if not os.path.exists(history_file):
    with open(history_file, "w") as f:
        json.dump([], f)

def generate_caption(image_path):
    """Generate a caption using OpenAI's CLIP model."""
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    texts = ["A cat", "A dog", "A sunset", "A city", "A person"]
    text_inputs = clip.tokenize(texts).to(device)
    
    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text_inputs)
        similarities = (image_features @ text_features.T).softmax(dim=-1)
    
    caption = texts[similarities.argmax().item()]
    save_caption(image_path, caption)
    return caption

def save_caption(image_path, caption):
    """Save caption to history file."""
    with open(history_file, "r") as f:
        history = json.load(f)
    history.append({"image": image_path, "caption": caption})
    with open(history_file, "w") as f:
        json.dump(history, f)

def copy_to_clipboard(text):
    pyperclip.copy(text)
    messagebox.showinfo("Copied", "Caption copied to clipboard!")

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def translate_caption(text, lang):
    translated_text = translator.translate(text, dest=lang).text
    messagebox.showinfo("Translation", f"Translated Caption: {translated_text}")

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        caption = generate_caption(file_path)
        img = Image.open(file_path)
        img.thumbnail((250, 250))
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
        caption_text.delete("1.0", tk.END)
        caption_text.insert(tk.END, caption)

def open_history():
    with open(history_file, "r") as f:
        history = json.load(f)
    history_window = tk.Toplevel(root)
    history_window.title("Caption History")
    text_widget = scrolledtext.ScrolledText(history_window, width=50, height=20)
    text_widget.pack()
    for item in history:
        text_widget.insert(tk.END, f"Image: {item['image']}\nCaption: {item['caption']}\n\n")

# GUI Setup
root = tk.Tk()
root.title("AI Image Caption Generator")
root.geometry("500x600")
root.configure(bg="#282C34")

frame = tk.Frame(root, bg="#3C4043", padx=10, pady=10)
frame.pack(pady=20)

title = tk.Label(frame, text="AI Image Caption Generator", fg="white", bg="#3C4043", font=("Arial", 16, "bold"))
title.pack()

image_label = tk.Label(frame, bg="#3C4043")
image_label.pack(pady=10)

btn_browse = tk.Button(frame, text="Choose Image", command=browse_image, bg="#61AFEF", fg="white", font=("Arial", 12))
btn_browse.pack()

caption_text = scrolledtext.ScrolledText(frame, width=50, height=5, font=("Arial", 12))
caption_text.pack(pady=10)

btn_copy = tk.Button(frame, text="Copy Caption", command=lambda: copy_to_clipboard(caption_text.get("1.0", tk.END)), bg="#98C379", fg="black", font=("Arial", 12))
btn_copy.pack(side=tk.LEFT, padx=5)

btn_speak = tk.Button(frame, text="Speak", command=lambda: speak_text(caption_text.get("1.0", tk.END)), bg="#E5C07B", fg="black", font=("Arial", 12))
btn_speak.pack(side=tk.LEFT, padx=5)

btn_history = tk.Button(frame, text="History", command=open_history, bg="#C678DD", fg="white", font=("Arial", 12))
btn_history.pack(side=tk.LEFT, padx=5)

root.mainloop()
