# from tkinter import *

# root = Tk()  # create root window
# root.title("Frame Example")
# root.config(bg="#1f1f1f")

# # Create Frame widget
# left_frame = Frame(root, width=200, height=400, bg='#1f1f1f')
# left_frame.grid(row=0, column=0, padx=10, pady=5)

# right_frame = Frame(root, width=650, height=400, bg='#1f1f1f')
# right_frame.grid(row=0, column=1, padx=10, pady=5)

# # Create frame within left_frame
# tool_bar = Frame(left_frame, width=180, height=185, bg="#3b3b3b")
# tool_bar.grid(row=2, column=0, padx=5, pady=5)

# # Create label above the tool_bar
# label = Label(left_frame, text="Example Text", bg='#1f1f1f', fg='white').grid(row=1, column=0, padx=5, pady=5)

# root.mainloop()

from tkinter import *
from PIL import ImageTk, Image

root = Tk()  # create root window
root.title("Basic GUI Layout")  # title of the GUI window
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg='#1f1f1f')  # specify background color

# Create left and right frames
left_frame = Frame(root, width=200, height=400, bg='#1f1f1f')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=650, height=400, bg='#1f1f1f')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create frames and labels in left_frame
Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

# load image to be "edited"
img = Image.open("./custom_interface/profile.png")
image_small = ImageTk.PhotoImage(img.resize((100, 100)))
Label(left_frame, image=image_small).grid(row=1, column=0, padx=5, pady=5)

# Display image in right_frame
image_big = ImageTk.PhotoImage(img.resize((300, 300)))
Label(right_frame, image=image_big).grid(row=0,column=0, padx=5, pady=5)

# Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets
Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

# Example labels that could be displayed under the "Tool" menu
Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)
root.mainloop()