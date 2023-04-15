import customtkinter as ctk

def move():
    global button_x
    button_x+=0.01
    if button_x < 0:
        frame.place(relx=button_x,rely=0.1)
        root.after(10,move)

root=ctk.CTk()
root.geometry("500x500")
root.resizable(False,False)
button=ctk.CTkButton(master=root,text="MOVE SIDEBAR",command=move)
button_x=-0.5
button.place(relx=0.5,rely=0.5,anchor="center")
frame=ctk.CTkFrame(master=root)
frame.place(relx=button_x,rely=0.1)
root.mainloop()