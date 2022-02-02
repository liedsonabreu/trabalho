from tkinter import *
from dao.UsuarioDao import UsuarioDao
from config.Config import Config
from config.Database import Database

config = Config()
database = Database(config.config)
dao = UsuarioDao(database.conn)

main = Tk()
main.title("Alterar")
main.geometry("1500x1000")

row = Frame(main)
row.pack(side=TOP, fill=X, padx=5, pady=5)

lbl = Label(row, text="ID:", anchor='w')
lbl.pack(side=LEFT)

txt0 = Entry(row)
txt0.pack(side=LEFT, expand=YES, fill=X, padx=5)

lbl = Label(row, text="Nome: ", anchor='w')
lbl.pack(side=LEFT)

txt = Entry(row)
txt.pack(side=LEFT, expand=YES, fill=X, padx=5)

lbl = Label(row, text="G-mail: ", anchor='w')
lbl.pack(side=LEFT)

txt2 = Entry(row)
txt2.pack(side=LEFT, expand=YES, fill=X, padx=5)

lbl = Label(row, text="Senha:", anchor='w')
lbl.pack(side=LEFT)

txt3 = Entry(row)
txt3.pack(side=LEFT, expand=YES, fill=X, padx=5)

def alterarUsuario():

    id = txt0.get()
    nome = txt.get()
    email = txt2.get()
    senha = txt3.get()
    dao.alterarUsuario1(id, nome, email, senha)

btn = Button(main, text="Alterar", command=alterarUsuario)
btn.pack(side=LEFT, padx=5, pady=5)

btn = Button(main, text="Fechar", command=main.destroy)
btn.pack(side=RIGHT, padx=5, pady=5)

main.mainloop()