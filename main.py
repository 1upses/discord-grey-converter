import tkinter as tk
from PIL import Image, ImageTk
import os

im1 = None

def threshold_change(val):
    threshold_value.set(int(val))

def on_submit():
    global im1
    os.system(f"py compute_image.py \"{filepath_entry.get()}\" \"{threshold_value.get()}\" \"{text_entry.get()}\"")
    im1 = Image.open("grey-" + filepath_entry.get())
    im1 = ImageTk.PhotoImage(im1)
    image_label.configure(image=im1)
    image_label.image = im1

def on_focus_in(event):
    if filepath_entry.get() == "filepath":
        filepath_entry.delete(0, "end")
        filepath_entry.config(fg = 'black')
    if text_entry.get() == "text":
        text_entry.delete(0, "end")
        text_entry.config(fg = 'black')

def on_focus_out(event):
    if not filepath_entry.get():
        filepath_entry.insert(0, "filepath")
        filepath_entry.config(fg = 'grey')
    if not text_entry.get():
        text_entry.insert(0, "text")
        text_entry.config(fg = 'grey')

root = tk.Tk()
root.title("Discord Grey Converter")

filepath = tk.StringVar()
text = tk.StringVar()
threshold_value = tk.IntVar()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width = int(screen_width * 0.4)
height = int(screen_height * 0.4)

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))

threshold_label = tk.Label(root, text="threshold")
threshold_label.pack()

threshold_slider = tk.Scale(root, from_=0, to=255, orient='horizontal', variable = threshold_value, command=threshold_change)
threshold_slider.pack()

filepath_entry = tk.Entry(root, textvariable=filepath)
filepath_entry.insert(0, "filepath")
filepath_entry.config(fg = 'grey')
filepath_entry.pack()
filepath_entry.bind("<FocusIn>", on_focus_in)
filepath_entry.bind("<FocusOut>", on_focus_out)

text_entry = tk.Entry(root, textvariable=text)
text_entry.insert(0, "text")
text_entry.config(fg = 'grey')
text_entry.pack()
text_entry.bind("<FocusIn>", on_focus_in)
text_entry.bind("<FocusOut>", on_focus_out)

image_label = tk.Label(root)
image_label.pack()

submit_button = tk.Button(root, text='Submit', command=on_submit)
submit_button.pack()

root.mainloop()
