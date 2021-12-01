from tkinter import*
import random

root = Tk()

root.title("list")
root.geometry("400x400")

items_list = Label(root)
ran_num = Label(root)

gifts = ['Bottel', 'ID Card', 'Tiffin', 'Chocolates', 'Chips']
print(gifts)

items_list["text"] = "Listed Items: " + str(gifts)

def random_item():
    num_items = len(gifts)
    print(num_items)
    
    random_number = random.randint(0, num_items - 1)
    print(random_number)
    ran_num["text"] = "Put item no. [" + str(random_number) + "] in bag."
    
btn = Button(root, text = "Which item to put in bag?", command = random_item)

items_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
ran_num.place(relx = 0.5, rely = 0.6, anchor = CENTER)


root.mainloop()