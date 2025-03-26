import tkinter as tk
from delete_database import delete_DATABASE
from database_population import creare_DATABASE

window = tk.Tk()

window.columnconfigure(1, weight=2, minsize=100)
window.rowconfigure(1, weight=2, minsize=100)
window.columnconfigure(2, weight=1, minsize=100)
window.rowconfigure(2, weight=1, minsize=100)

def button_click_1_creare_DB():
    nome_database = entry_create_DB_nome.get()
    creare_DATABASE(nome_database)
    entry_create_DB_nome.delete(0, tk.END)
    lbl_db_creato["text"] = f"DATABASE CREATO:\n{nome_database}"

def button_click_2_cancellare_DB():
    nome_database = entry_eliminate_DB_nome.get()
    delete_DATABASE(nome_database)
    entry_eliminate_DB_nome.delete(0, tk.END)
    lbl_db_eliminato["text"] = f"DATABASE ELIMINATO:\n {nome_database}"

frame1_1 = tk.Frame(master=window, borderwidth=15, relief=tk.GROOVE)
frame1_1.grid(row=1, column=1)
label1_1 = tk.Label(
                    master=frame1_1, 
                    text="CLICCARE PER CREARE DB", 
                    font="Courier 30 bold")
label1_1.pack()

button_1 = tk.Button(
                text="Crea DB", 
                font=("Courier 25 bold"),
                bg="black",
                fg="#53a8bd",
                width=10,
                height=3,
                master=frame1_1,
                relief=tk.RAISED,
                borderwidth=5,
                command=button_click_1_creare_DB
                )

button_1.pack()

frame1_2 = tk.Frame(master=window, borderwidth=15, relief=tk.GROOVE)
frame1_2.grid(row=1, column=2)
label1_2 = tk.Label(master=frame1_2, text="CLICCARE PER CANCELLARE DB", font="Courier 30 bold")
label1_2.pack()

entry_create_DB_nome = tk.Entry(
                    fg="white",
                    bg="black",
                    font="Courier 25 bold",
                    master=frame1_1
                    )

lbl_db_creato = tk.Label(
                    text="",
                    fg="green",
                    font="Courier 25 bold",
                    master=frame1_1
                    )
                
entry_create_DB_nome.pack()
lbl_db_creato.pack()

button_2 = tk.Button(
                text="Cancella DB", 
                font=("Courier 25 bold"),
                bg="black",
                fg="#53a8bd",
                width=10,
                height=3,
                master=frame1_2,
                relief=tk.RAISED,
                borderwidth=5,
                command=button_click_2_cancellare_DB
                )

button_2.pack()

entry_eliminate_DB_nome = tk.Entry(
                    fg="white",
                    bg="black",
                    font="Courier 25 bold",
                    master=frame1_2
                    )

lbl_db_eliminato = tk.Label(
                    text="",
                    fg="red",
                    font="Courier 25 bold",
                    master=frame1_2
                    )
                
entry_eliminate_DB_nome.pack()
lbl_db_eliminato.pack()

window.mainloop()