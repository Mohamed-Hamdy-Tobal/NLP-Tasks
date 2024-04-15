import tkinter as tk
import nltk
from tkinter import Text, OptionMenu, StringVar

# Download NLTK resources if not already downloaded
nltk.download('punkt')

def text_operation():
    text = text_entry.get("1.0", tk.END).strip()
    choice = choice_var.get()

    if choice == "Tokenized words":
        results = nltk.word_tokenize(text)
    elif choice == "Tokenized sentences":
        results = nltk.sent_tokenize(text)
    elif choice == "Output using split function.":
        results = text.split()
    else:
        results = "Invalid choice. Please enter option (1, 2, or 3)."

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, str(results))
    result_text.config(state="disabled")

win = tk.Tk()
win.title("Text Tokenizer")

# Text entry field
text_label = tk.Label(win, text="Enter a Text:", font=("Helvetica", 20))
text_label.pack()
text_entry = Text(win, height=5, font=("Helvetica", 12))
text_entry.pack()

# Choice dropdown
choice_label = tk.Label(win, text="Choose an option operation for your text:")
choice_label.pack()
choice_var = StringVar(win)
choice_var.set("Tokenized words")  # Default choice
choice_dropdown = OptionMenu(win, choice_var,
                                "Tokenized words",
                                "Tokenized sentences",
                                "Output using split function.")
choice_dropdown.pack()

# Button submit
submit_button = tk.Button(win, text="Submit", command=text_operation, bg="green", fg="white")  # Set background color to green
submit_button.pack()

# Result text
result_label = tk.Label(win, text="Result Is :", font=("Helvetica", 12))
result_label.pack()
result_text = Text(win, height=10, state="disabled", font=("Helvetica", 12), fg="red")  # Set foreground color to red
result_text.pack(padx=10, pady=5)

# Start the Tkinter
win.mainloop()