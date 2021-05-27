import pyautogui
import tkinter as tk
from tkinter import Label, filedialog
import pyperclip
import base64
import requests
import json

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

root.title("Screenshot")

def takeScreen ():
    
    scr = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    scr.save(file_path)
    print(f"Screenshot was saved in {file_path} !")

    config = json.load(open("config.json"))

    with open(file_path, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": str(config["api_token"]),
            "image": base64.b64encode(file.read()),
            "expiration": int(config["link_expire"])
        }
    post = requests.post(url, payload)

    print(post.json()['status'])

    print(f"Your Screenshot: {post.json()['data']['url_viewer']}")

button = tk.Button(text='Screenshot', command=takeScreen, bg='black',fg='red',font= 10)
canvas1.create_window(150, 150 , window=button)

def close_programm():
    root.destroy()

close = tk.Button(text="Quit Programm", command=close_programm, bg="black", fg="red", font=10)
canvas1.create_window(150, 200, window=close)


root.mainloop()
