from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

jan = Tk()
jan.title("StyleSZA")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icones/LogoIcon.ico")

logo = PhotoImage(file="icones/estrela.png")

LeftFrame = Frame(jan, width=197, height=300, bg="LIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=400, height=300, bg="LIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="LIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Usuário: ", font=("Century Gothic", 20), bg="LIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="LIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE User = ? AND Password = ?
    """, (User, Pass))
    VerifyLogin = DataBaser.cursor.fetchone()

    if VerifyLogin:
        messagebox.showinfo(title="Login Info", message="Acesso Confirmado. Bem-vindo!")
    else:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se está cadastrado no sistema!")

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    LoginButton.place_forget()
    RegisterButton.place_forget()

    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="LIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="LIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if Name == "" or Email == "" or User == "" or Pass == "":
            messagebox.showerror(title="Register Error", message="Não deixe nenhum campo vazio. Preencha todos os campos.")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users (Name, Email, User, Password) VALUES (?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso.")
            BackToLogin()

    RegisterButtonConfirm = ttk.Button(RightFrame, text="Registrar", width=30, command=RegisterToDataBase)
    RegisterButtonConfirm.place(x=100, y=225)

    def BackToLogin():
        NomeLabel.place_forget()
        NomeEntry.place_forget()
        EmailLabel.place_forget()
        EmailEntry.place_forget()
        RegisterButtonConfirm.place_forget()
        BackButton.place_forget()

        LoginButton.place(x=100, y=225)
        RegisterButton.place(x=125, y=260)

    BackButton = ttk.Button(RightFrame, text="Voltar", width=20, command=BackToLogin)
    BackButton.place(x=125, y=260)

RegisterButton = ttk.Button(RightFrame, text="Registrar", width=20, command=Register)
RegisterButton.place(x=125, y=260)

jan.mainloop()
