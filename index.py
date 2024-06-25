from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser


jan = Tk()
jan.title("Deshaibell")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/LogoIcon.ico")

logo = PhotoImage(file="icons/logo.png.png")

LeftFrame = Frame(jan, width=200, height=300, bg="TAN", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=400, height=300, bg="TAN", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="TAN")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Usuário: ", font=("Century Gothic", 20), bg="TAN", fg="Black")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic",20), bg="TAN", fg="Black")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User - ? and Password - ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado. Bem vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se está cadastrado no sistema!")


LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

def Register():
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="BLACK", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="BLACK", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)


    Register = ttk.Button(RightFrame, text="Register", width=30)
    Register.place(x=100, y=225)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" or Email == "" or User == "" or Pass == ""):
            messagebox.showerror(title="Register Error", message="Não Deixe Nenhum Campo Vazio. Preencha Todos os Campos")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com Sucesso")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)




    def BackToLogin():
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)


RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)


jan.mainloop()