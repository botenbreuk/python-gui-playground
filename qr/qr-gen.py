import pyotp, threading, tkinter as tk, os, base64
from pyqrcode import QRCode
from tkinter import messagebox
from tkinter import filedialog

# Function to generate QR code
def generate_qr():
  # Getting the text or url from the text field
  data = entry.get()

  if var1.get() == 0:
    data = base64.b32encode(data.encode())
    base32_str.set(data)
    base32_entry.pack(fill='x')
  else:
    base32_entry.pack_forget()

  # Checking if the data is empty
  if data and data != "Enter the text or url":
    # Creating the QR code and saving it as qrcode.png
    global myQr, totp
    topt_link = pyotp.TOTP(data, digits=6, interval=30).provisioning_uri(name='TEST TOTP', issuer_name='TOTP Python App')
    myQr = QRCode(topt_link)

    # Opening the QR code and resizing it to fit the label
    img = tk.PhotoImage(data=myQr.png_as_base64_str(scale=6))
    # Setting the image and text in the label
    label.config(text='QR code generated',image=img,compound='bottom')
    label.image = img

    totp = pyotp.TOTP(data)
    print_totp()
    ent.pack()
  
  else:
    # If the data is empty, show an error message
    label.config(text="Please Enter the data")

# Function to save the QR code
def save():
  # Getting the file name and location to save the QR code
  input_path = filedialog.asksaveasfilename(title="Save Image", filetyp=(("PNG File", ".png"), ("All Files", "*.*")))

  # Checking if the file name is not empty   
  if input_path:
    print(input_path)
    if input_path.endswith(".png"):
      myQr.png(input_path, scale=6)
      # Showing a success message after saving the QR code
      messagebox.showinfo("Success", "QR code saved successfully")
    else:
      input_path = f'{input_path}.png'
      print(input_path)
      myQr.png(input_path, scale=6)
      # Showing a success message after saving the QR code
      messagebox.showinfo("Success", "QR code saved successfully")

def print_totp():
  global totp

  # threading.Timer(1.0, print_totp).start()
  data_string.set(totp.now())
  root.after(1000, print_totp) # every second...

# Creating the GUI
root = tk.Tk()
# Setting the title and window size
root.geometry('700x700')
root.title('Project Gurukul - QR Code Generator')

# Creating the entry to enter the text
entry = tk.Entry(root, width=40)
entry.pack()
# entry.bind("<FocusIn>", lambda args: entry.delete('0', 'end'))
entry["justify"] = "center"
# Creating a placeholder text
# entry.insert(0, "Enter the text or url")

var1 = tk.IntVar()
c1 = tk.Checkbutton(root, text='Is base32 string',variable=var1, onvalue=1, offvalue=0)
c1.pack()

base32_str = tk.StringVar()
base32_str.set("")
base32_entry = tk.Entry(root,textvariable=base32_str,fg="black",bg="white",bd=0,state="readonly", font=("Arial", 12) )
base32_entry["justify"] = "center"

# Creating the button to generate the QR code
button = tk.Button(root, text='Generate QR code', command=generate_qr)
button.pack()

label = tk.Label(root)
label.config(text='No QR',compound='bottom')
label.pack()

# Creating the button to save the QR code
saveButton = tk.Button(root, text="Save", command=save)
saveButton.pack()

totp = pyotp.TOTP('')

data_string = tk.StringVar()
data_string.set("")
ent = tk.Entry(root,textvariable=data_string,fg="black",bg="white",bd=0,state="readonly", font=("Arial", 25) )
ent["justify"] = "center"

# Running the mainloop
root.mainloop()