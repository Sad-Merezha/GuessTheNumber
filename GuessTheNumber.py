import random
import customtkinter as ctk  
from tkinter import messagebox

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")  

attempts = 5
secret_num = random.randint(1, 100)

def check_number():
    global attempts, secret_num
    
    try:
        user_guess = int(user_input.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    if user_guess == secret_num:
        messagebox.showinfo("Win!", "Congratulations! You guessed it!")
        root.destroy()
        return

    if user_guess > secret_num:
        attempts = attempts - 1
        hint.configure(text="Too many, try some littler", text_color="red")

    if user_guess < secret_num:
        attempts = attempts - 1
        hint.configure(text="It's too little, try some more", text_color="red")

    attempts_text.configure(text=f"Guess number from 1 to 100, you have {attempts} attempts:")
    user_input.delete(0, 'end')

    if attempts == 0:
        messagebox.showinfo("Game Over", f"You lose! Hidden number was {secret_num}")
        root.destroy()
        return

root = ctk.CTk()
root.title("GuessTheNumber")
root.geometry("640x480")
root.resizable(False, False)

main_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="#222222") 
main_frame.pack(fill="both", expand=True)

attempts_text = ctk.CTkLabel(main_frame, text=f"Guess number from 1 to 100, you have {attempts} attempts:")
attempts_text.configure(font=("Arial", 16, "bold"), text_color="white")
attempts_text.pack(pady=30)

user_input = ctk.CTkEntry(main_frame, width=140, height=50, justify="center")
user_input.configure(font=("Arial", 20, "bold"))
user_input.pack(pady=20)
user_input.focus()

guess_button = ctk.CTkButton(main_frame, text="Apply!", command=check_number, width=180, height=45)
guess_button.configure(font=("Arial", 14, "bold"))
guess_button.pack(pady=20)

hint = ctk.CTkLabel(main_frame, text="")
hint.configure(font=("Arial", 16, "bold"), text_color="gray")
hint.pack(pady=30)

watermark = ctk.CTkLabel(main_frame, text="© Created by Sad-Merezha")
watermark.configure(font=("Arial", 12), text_color="gray")
watermark.place(x=470, y=440) 

root.mainloop()

