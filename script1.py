from tkinter import *

window = Tk()


def search_titles():
    print('Success!')


b1 = Button(window, text='Clear')
b1.grid()
b2 = Button(window, text='Search', command=search_titles)
b2.grid(row=0, column=2)
book_title_label = Label(text='Title:')
book_title_label.grid(row=1, column=0)
book_title = Entry(window)
book_title.grid(row=1, column=1)

book_author_label = Label(text='Author:')
book_author_label.grid(row=2, column=0)
book_author = Entry(window)
book_author.grid(row=2, column=1)

book_isbn_label = Label(text='ISBN:')
book_isbn_label.grid(row=3, column=0)
book_isbn = Entry(window)
book_isbn.grid(row=3, column=1)

book_price_label = Label(text='price:')
book_price_label.grid(row=4, column=0)
book_price = Entry(window)
book_price.grid(row=4, column=1)

window.mainloop()
