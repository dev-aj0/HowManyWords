import tkinter as tk
from tkinter import ttk

def count_string_occurrences(text, target_string):
    count = 0
    index = 0
    while index < len(text):

        index = text.find(target_string, index)
        if index == -1:
            break
        count += 1
        index += len(target_string)
    return count

def count_occurrences():

    text = text_entry.get("1.0", "end-1c")
    target = target_entry.get()


    occurrences = count_string_occurrences(text, target)


    result_label.config(text=f"The string '{target}' occurs {occurrences} times in the text.")


window = tk.Tk()
window.title("String Occurrence Counter")
window.geometry("500x400")
window.configure(bg="#323232")

window.iconbitmap("counting.ico")



text_label = tk.Label(window, text="Enter the text:", bg="#323232", fg="#FFFFFF", font=("Arial", 12, "bold"))
text_label.pack(pady=10)


text_entry_frame = ttk.Frame(window)
text_entry_frame.pack(fill=tk.BOTH, expand=True)

text_entry = tk.Text(text_entry_frame, height=10, bg="#FFFFFF", fg="#333333", font=("Arial", 11))
text_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

text_scrollbar = ttk.Scrollbar(text_entry_frame, orient=tk.VERTICAL, command=text_entry.yview)
text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_entry.configure(yscrollcommand=text_scrollbar.set)


target_label = tk.Label(window, text="Enter the string to count:", bg="#323232", fg="#FFFFFF", font=("Arial", 12, "bold"))
target_label.pack(pady=10)


target_entry = tk.Entry(window, bg="#FFFFFF", fg="#333333", font=("Arial", 11))
target_entry.pack()


count_button = tk.Button(window, text="Count", command=count_occurrences, bg="#6A6AAE", fg="#FFFFFF", font=("Arial", 12, "bold"))
count_button.pack(pady=15)


result_label = tk.Label(window, text="", bg="#323232", fg="#FFFFFF", font=("Arial", 14, "bold"), pady=10)
result_label.pack()


window.mainloop()
