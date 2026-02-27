import os
import shutil
import tkinter as tk
from ttkbootstrap import Style
import fire

def showFolder(p: str) -> str:
    if next(os.scandir(p), None) is None:
        return "Folder is empty"
    else:
        str1=f"Files in this folder:\n\n"
        str2=""
        for i in os.listdir(p):
            str2 = str2 +f"{i}\n"
    return str1+str2

def deleteFiles(p:str):
    for i in os.listdir(p):
        full = os.path.join(p, i)
        if os.path.isfile(full):
            os.remove(full)
        else:
            shutil.rmtree(full)

def main(path:str):
    root = tk.Tk()                 
    style = Style(theme="darkly") 
    root.title("Folder cleaner")
    root.geometry("400x400")
    label1 = tk.Label(text=showFolder(path),font=(16))
    label1.pack()

    button1 = tk.Button(root, text="delete all Files", command=lambda:deleteFiles(path), font=(10))
    button1.pack(pady=50)

    button2 = tk.Button(root, text="end programm", command=root.destroy, font=(10))
    button2.pack(pady=5)
    root.mainloop()

if __name__ == "__main__":
    fire.Fire(main)
