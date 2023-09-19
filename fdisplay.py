from tkinter import *

window = TK()
window.title('add image')
window = Canvas(window, width= 250, height= 250)
window.pack()
image = PhotoImage(file = 'D://Pallavi_Project3//hangman.png')
window.create_image(0, 0, ANCHOR= NW, image = image)

window.mainloop()