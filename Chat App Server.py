import customtkinter as ctk
import socket

ctk.set_appearance_mode("System")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        global Appself
        Appself=self
        self.title("Chat App Server")
        self.geometry("300x300")
        self.resizable(False,False)
        button=ctk.CTkButton(master=self,text="CONNECT",command=App.Connect)
        button.pack(padx=20,pady=20)
        self.mainloop()

    def Connect():
        root=ctk.CTk()
        label=ctk.CTkLabel(master=root,text="Enter Address")
        entry=ctk.CTkEntry(master=root)
        port=ctk.CTkLabel(master=root,text="Enter Port")
        entryport=ctk.CTkEntry(master=root)
        button=ctk.CTkButton(master=root,text="CONNECT",command=lambda root=root,address=entry,port=entryport: App.Chat(root,address,port))
        label.pack(padx=20,pady=20)
        entry.pack(padx=20,pady=20)
        port.pack(padx=20,pady=20)
        entryport.pack(padx=20,pady=20)
        button.pack(padx=20,pady=20)
        root.mainloop()

    def Chat(root,address,port):
        address=address.get()
        port=int(port.get())
        root.destroy()
        Appself.destroy()
        App.Create_Chat(address,port)
        # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # server.bind((address,port))
        # server.listen()
        # client, addr = server.accept()
        # done = False
        # while not done:
        #     client.send(input("Message: ").encode("utf-8"))
        #     msg = client.recv(1024).decode("utf-8")
        #     if msg.lower()=="quit":
        #         done = True
        #     else:
        #         print(msg)

    def Create_Chat(address,port):
        root=ctk.CTk()
        root.geometry("500x500")
        entry=ctk.CTkEntry(master=root)
        button=ctk.CTkButton(master=root,text="SEND",width=10)
        entry.grid(row=2,column=2)
        button.grid(row=1,column=4)
        root.mainloop()



App()