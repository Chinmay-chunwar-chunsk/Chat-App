import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        height=500
        send=ctk.CTkButton(master=self,text="SEND",width=70,height=30,command=None)
        send.place(relx=0.9,rely=0.94)
        message=ctk.CTkEntry(master=self,width=430)
        message.place(relx=0.1,rely=0.94)
        self.mainloop()

if __name__=="__main__":
    App()