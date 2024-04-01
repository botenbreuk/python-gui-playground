import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1000x600")

counter = 1

def login():
  print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

def count():
  global counter
  counter += 1
  label2.configure(text=counter)

label = customtkinter.CTkLabel(master=frame, text="Login system")
label.pack(pady=12, padx=10)

entryl = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entryl.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text=counter)
label2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Count", command=count)
button.pack(pady=12, padx=10)

root.mainloop()

# https://stackoverflow.com/questions/34689889/update-label-text-after-pressing-a-button-in-tkinter