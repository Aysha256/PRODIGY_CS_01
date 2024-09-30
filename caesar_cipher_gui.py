import tkinter as tk

letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def process_text(action):
    try:
        key = int(key_entry.get())
        text = text_entry.get().lower()
        result = ''
        for letter in text:
            if letter in letters:
                index = letters.find(letter)
                if action == "encrypt":
                    new_index = (index + key) % num_letters
                else:  # decrypt
                    new_index = (index - key) % num_letters
                result += letters[new_index]
            else:
                result += letter
        result_text.set(result)
    except ValueError:
        result_text.set("Invalid Key! Please enter a number.")

window = tk.Tk()
window.title("Caesar Cipher")

tk.Label(window, text="Enter Text:").pack()
text_entry = tk.Entry(window, width=50)
text_entry.pack()

tk.Label(window, text="Enter Key:").pack()
key_entry = tk.Entry(window, width=10)
key_entry.pack()

tk.Button(window, text="Encrypt", command=lambda: process_text("encrypt")).pack(pady=5)
tk.Button(window, text="Decrypt", command=lambda: process_text("decrypt")).pack(pady=5)

result_text = tk.StringVar()
tk.Label(window, textvariable=result_text, bg="lightgray", width=50).pack(pady=10)

window.mainloop()
