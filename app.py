'''Used to create the GUI for the translation application and connect the UI to the backend.'''
from tkinter import *
from tkinter import ttk, messagebox
from main import translate_text, get_supported_languages

def perform_translation():
    source_lang = source_language_var.get()
    target_lang = target_language_var.get()
    text = text_var.get()
    translation = translate_text(text, source_lang, target_lang)
    result_label.config(text=translation)

def exit_app():
    root.destroy()

root = Tk()
root.title("Local Translator")

#Content Frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

supported_languages = get_supported_languages()

source_language_var = StringVar()
source_language_var_dropdown = ttk.Combobox(mainframe, textvariable=source_language_var, values=supported_languages)
source_language_var_dropdown.grid(column=2, row=1)

target_language_var = StringVar()
target_language_var_dropdown = ttk.Combobox(mainframe, textvariable=target_language_var, values=supported_languages)
target_language_var_dropdown.grid(column=2, row=2)

text_var = StringVar()
text_var_entry = ttk.Entry(mainframe, width=20, textvariable=text_var)
text_var_entry.grid(column=2, row=3)

ttk.Label(mainframe, text="Source Language").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Target Currency").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Text to Translate").grid(column=3, row=3, sticky=W)

translate_button = ttk.Button(mainframe, text="Translate", command=perform_translation)
translate_button.grid(column=2, row=5, sticky=(W, E))

result_label = ttk.Label(mainframe, text="")
result_label.grid(column=2, row=6, sticky=(W, E))

root.bind('<Return>', lambda _: perform_translation())
root.bind('<Escape>', lambda _: exit_app())

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()


