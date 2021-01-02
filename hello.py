import tkinter

#defined window
root= tkinter.Tk()

#Customization
#title
root.title('Window Basics!')
#artwork
#root.iconbitmap("Header_logo1_9Pj_.icon")

root.geometry('250x700')
root.resizable(0,0)
root.config(bg='blue')

#second window
top=tkinter.Toplevel()
top.title('Second Window')
top.config(bg='#123456')
top.geometry('200x200+500+50')

#Run Root Window main loop
root.mainloop()


