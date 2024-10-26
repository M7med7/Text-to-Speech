from gtts import gTTS
import os
import tkinter as tk

def text_to_speech():
    text = text_entry.get("1.0", tk.END)  # Get text from the text entry
    if text.strip():
        # Create a gTTS object
        tts = gTTS(text=text, lang='en', slow=False)
        
        # Save the audio file
        tts.save("output.mp3")
        
        # Play the audio file
        os.system("start output.mp3")  


app = tk.Tk()
app.title("Text to Speech converter")


lable = tk.Label(app,text = "Enter the text you want to convert to speech: ",font = ("Arial",14))
lable.pack(pady = 10)


text_entry = tk.Text(app,height = 5,width = 40,font = ("Arial",12))
text_entry.pack(pady = 10)  

convert_button = tk.Button(app,text = "Convert",command = text_to_speech)
convert_button.pack(pady = 10)
app.mainloop()

