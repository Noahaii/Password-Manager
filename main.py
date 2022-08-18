from random import choice, randint, shuffle
import tkinter
from tkinter import messagebox
import json

GRAY = "#EAEDED" 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- SEARCH WEB ------------------------------- #
def find_password():
    try:
        with open("C:\\Users\\ninoc\\projects\\CodingProjects\\Password_Manager\\venv\\data.json", 'r') as data_file:
            contents = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="ERROR", message="No Data File found")
    else:
        website = website_input.get()
        try:
            login = contents[website]
        except KeyError:
            messagebox.showwarning(title="ERROR", message=f"No info for {website} website")
        else:
            messagebox.showinfo(title="Login Info", message=f"{login['email']} \n{login['password']}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    pass_letters = [choice(letters) for _ in range(randint(5, 7))]
    pass_num = [choice(numbers) for _ in range(randint(1, 2))]
    pass_symb = [choice(symbols) for _ in range(randint(1, 2))]
    password_list = pass_letters + pass_symb + pass_num
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_input.get()
    user = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Missing Fields", message="Please fill out missing fields")
    else:
        try:
            with open("C:\\Users\\ninoc\\projects\\CodingProjects\\Password_Manager\\venv\\data.json", "r") as f:
                # reads old data
                data = json.load(f)  
        except FileNotFoundError:
            with open("C:\\Users\\ninoc\\projects\\CodingProjects\\Password_Manager\\venv\\data.json", "w") as f:
                json.dump(new_data, f, indent=4)
                website_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)
        else:
             # updating old data with new data
            data.update(new_data)
            with open("C:\\Users\\ninoc\\projects\\CodingProjects\\Password_Manager\\venv\\data.json", "w") as f:
                # writes new data into file
                json.dump(data, f, indent=4)
        finally:
                website_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="C:\\Users\\ninoc\\projects\\CodingProjects\\Password_Manager\\venv\\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:", font=('Arial', 8, 'bold'))
website_label.grid(column=0, row=1)
website_input = tkinter.Entry(width=22, bg=GRAY)
website_input.grid(column=1, row=1)

username_label = tkinter.Label(text="Email/Username:", font=('Arial', 8, 'bold'))
username_label.grid(column=0, row=2)
username_input = tkinter.Entry(width=45, bg=GRAY, highlightthickness=0)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "ninocencio73@gmail.com")

password_label = tkinter.Label(text="Password:", font=('Arial', 8, 'bold'))
password_label.grid(column=0, row=3)
password_input = tkinter.Entry(width=22, bg=GRAY)
password_input.grid(column=1, row=3)

search_button = tkinter.Button(text="Search", width=22, font=('Arial', 8), command=find_password)
search_button.grid(column=2, row=1)

generate_button = tkinter.Button(text="Generate Password", width=22, font=('Arial', 8), command=generate)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=40, font=('Arial', 8), command=add)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()