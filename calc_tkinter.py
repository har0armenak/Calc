# from tkinter import *


# def str_to_sort_list(event):
#     s = ent.get()
#     s = s.split()
#     s.sort()
#     lab['text'] = ' '.join(s)


# root = Tk()

# ent = Entry(root, width=30)
# but = Button(root, width=20, text="Преобразовать")
# lab = Label(root, width=30, bg='black', fg='white')

# but.bind('<Button-1>', str_to_sort_list)

# ent.pack()
# but.pack()
# lab.pack()
# root.mainloop()


from tkinter import *
 
 
# class Block:
#     def __init__(self, master, func):
#         self.ent = Entry(master, width=20)
#         self.but1 = Button(master,
#                           text="1but 1")
#         self.but2 = Button(master,
#                           text="Преобразовать")
#         self.lab = Label(master, width=20,
#                          bg='black', fg='white')
#         self.but2['command'] = self.str_to_sort
#         self.but1['command'] = self.str_reverse
        
#         self.ent.pack()
#         self.but1.pack()
#         self.but2.pack()
#         self.lab.pack()
 
#     def str_to_sort(self):
#         s = self.ent.get()
#         s = s.split()
#         s.sort()
#         self.lab['text'] = ' '.join(s)
 
#     def str_reverse(self):
#         s = self.ent.get()
#         s = s.split()
#         s.reverse()
#         self.lab['text'] = ' '.join(s)
 
 
# root = Tk()
 
# first_block = Block(root, '')
# # second_block = Block(root, 'str_reverse')
# # second_block1 = Block(root, 'str_reverse')
 
# root.mainloop()

class Block:
    def __init__(self, master):

        self.ent1 = Entry(master, width=40)
        self.ent2 = Entry(master, width=40)
        self.but_plus = Button(master, width=10, text="+")
        self.but_minus = Button(master, width=10, text="-")
        self.but_bazm = Button(master, width=10, text="*")
        self.but_baj = Button(master, width=10, text="/")
        self.lab = Label(master, width=20, bg='black', fg='white')

        self.but_plus['command'] = self.pres_for_plus
        self.but_minus['command'] = self.pres_for_minus
        self.but_bazm['command'] = self.pres_for_bazm
        self.but_baj['command'] = self.pres_for_baj
        
        self.ent1.pack()
        self.ent2.pack()
        
        self.but_plus.pack()
        self.but_minus.pack()
        self.but_bazm.pack()
        self.but_baj.pack()

        self.lab.pack()
 
    def pres_for_plus(self):
        a = self.ent1.get()
        b = self.ent2.get()
        a1 = int(a)
        b1 = int(b)
        sum = a1+b1
        self.lab['text'] = sum
 
    def pres_for_minus(self):
        a = self.ent1.get()
        b = self.ent2.get()
        a1 = int(a)
        b1 = int(b)
        sum = a1-b1
        self.lab['text'] = sum

    def pres_for_bazm(self):
        a = self.ent1.get()
        b = self.ent2.get()
        a1 = int(a)
        b1 = int(b)
        sum = a1*b1
        self.lab['text'] = sum

    def pres_for_baj(self):
        a = self.ent1.get()
        b = self.ent2.get()
        a1 = int(a)
        b1 = int(b)
        sum = a1/b1 
        self.lab['text'] = sum
 
 
root = Tk()

 
first_block = Block(root)

root.mainloop()