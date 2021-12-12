from tkinter import *
root = Tk()
root.title("Schul-App")


mein_menu = Menu(root)
root.config(menu=mein_menu)

#Klick command
def unser_command():
    pass


file_menu = Menu(mein_menu) #Menü erstellen
mein_menu.add_cascade(label="File", menu=file_menu) #Sub-Menu erstellen
file_menu.add_separator() #Striche (______) einfügen
file_menu.add_command(label="Neu...",command=unser_command)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
file_menu.add_separator()

# edit menu item erstellen
edit_menu = Menu(mein_menu) #Menü erstellen
mein_menu.add_cascade(label="Edit", menu=edit_menu)


root.mainloop()


