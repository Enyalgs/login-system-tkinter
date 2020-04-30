#Importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

corPrincipal = '#14171c'

#Criação da janela
window = Tk()
window.title("UFO Systems - Access Painel")
window.geometry("600x300") #Tamanho da tela
window.configure(background="#a3a3a3")
window.resizable(width=False, height=False) #Alteração do tamanho da tela
window.attributes("-alpha", 0.5) #Tranparencia
#window.iconbitmap(default='img/logoIcon.ico')

#Carregando imagens
logo = PhotoImage(file="img/ufo.png")
user = PhotoImage(file="img/user.png")

#WIDGETS
LeftFrame = Frame(window, width = 200, height = 300, bg = corPrincipal, relief="raise")
RightFrame = Frame(window, width = 398, height = 300, bg = corPrincipal, relief="raise")

LeftFrame.pack(side=LEFT)
RightFrame.pack(side=RIGHT)

#Logo 
LogoLabel = Label(LeftFrame, image=logo, bg=corPrincipal)
LogoLabel.place(x=40, y=80) #Posicionamento

LogoUserLabel = Label(RightFrame, image=user, bg=corPrincipal)
LogoUserLabel.place(x = 180, y = 20)

TituloLoginLabel = Label(RightFrame, text="LOGIN", font=("Century Gothic", 18), bg=corPrincipal, fg="white" )
TituloLoginLabel.place(x = 160, y = 60)

#Login - Username
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 10), bg=corPrincipal, fg="white")
UserEntry = ttk.Entry(RightFrame, width=30)

UserLabel.place(x=78, y=100)
UserEntry.place(x=80, y=120)

#Login - password
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 10), bg=corPrincipal, fg="white")
PassEntry = ttk.Entry(RightFrame, width=30, show="*")

PassLabel.place(x=78, y=150)
PassEntry.place(x=80, y=170)

def Login():
    User = UserEntry.get()
    Password = PassEntry.get()
    if(User == "" or Password == ""):
        messagebox.showerror(title="Register Error", message="Complete all Fields of the Login")
    else:
        DataBaser.cursor.execute("""
            SELECT * FROM Users
            WHERE User = ? AND Password = ?
        """, (User, Password))
        VerifyLogin = DataBaser.cursor.fetchone()
        try:
            if(User in VerifyLogin and Password in VerifyLogin):
                messagebox.showinfo(title="Login Info", message="Acess Confirmed")
        except:
            messagebox.showerror(title="Login Erro", message="Acces Denied")

#Buttons -Login
LoginButton = ttk.Button(RightFrame, text="Login", width=20, command=Login)
LoginButton.place(x=115, y=210)

def Register():
    #Removendo Widgets de login
    LoginButton.place(x=4444)
    RegisterButton.place(x=4444)
    LogoUserLabel.place(x=4444)
    TituloLoginLabel.place(x=4444)
    #Inserindo Widgets de cadastro
    NameLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 10), bg=corPrincipal, fg="white")
    EmailLabel = Label(RightFrame, text="Email:",font=("Century Gothic", 10), bg=corPrincipal, fg="white")
    
    NameEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry = ttk.Entry(RightFrame, width=30)

    def RegisterToDataBase():
        Name = NameEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Password = PassEntry.get()

        if(Name == "" or Email == "" or User == "" or Password == ""):
            messagebox.showerror(title="Register Error", message="Complete all Fields of the Registration")
        else:
            DataBaser.cursor.execute("""
                INSERT INTO Users(Name, Email, User, Password) 
                VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Password))
            DataBaser.connection.commit()
            messagebox.showinfo(title="Register Info", message="Account Successfully Created")

    Register = ttk.Button(RightFrame, text="Register", width=20, command=RegisterToDataBase)

    NameLabel.place(x=78, y = 5)
    NameEntry.place(x= 80, y = 25)
    EmailLabel.place(x=78, y = 50)
    EmailEntry.place(x= 80, y = 70)
    Register.place(x=115, y=210)

    def BackToLogin():
        #Removendo Widgets de cadastro
        NameLabel.place(x=4444)
        NameEntry.place(x=4444)
        EmailLabel.place(x=4444)
        EmailEntry.place(x=4444)
        Register.place(x=4444)
        Back.place(x=4444)

        #Trazendo de volta o Widgets de login
        LoginButton.place(x=115)
        RegisterButton.place(x=130)
        LogoUserLabel.place(x=180)
        TituloLoginLabel.place(x=160)

    Back = ttk.Button(RightFrame, text="Back", width=15, command=BackToLogin)
    Back.place(x=130, y=250)


#Buttons - Register
RegisterButton = ttk.Button(RightFrame, text="Register", width=15, command=Register)
RegisterButton.place(x=130, y=250)


window.mainloop()