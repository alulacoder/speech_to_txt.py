import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox, scrolledtext

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        root.update()
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            text_area.insert(tk.END, text + "\n")
        except sr.UnknownValueError:
            text_area.insert(tk.END, "Sorry, could not understand the audio.\n")
        except sr.RequestError:
            text_area.insert(tk.END, "Could not request results. Check your internet connection.\n")
            status_label.config(text="Ready")

try:
    import speech_recognition as sr
except ModuleNotFoundError:
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", "speech_recognition module not found. Please install it using 'pip install SpeechRecognition'.")
    raise SystemExit

root = tk.Tk()
root.title("Speech to Text Converter")
root.geometry("400x300")

status_label = tk.Label(root, text="Press 'Start' and speak", font=("Arial", 12))
status_label.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Arial", 10))
text_area.pack(pady=10)

start_button = tk.Button(root, text="Start", command=speech_to_text, font=("Arial", 12))
start_button.pack(pady=10)

root.mainloop()
