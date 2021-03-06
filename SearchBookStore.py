#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import html.parser
import tkinter as tk
import pickle

window = tk.Tk()
window.title('Search Book')
window.geometry('450x600')


tk.Label(window, text='Book name: ').place(x=50, y= 30)

var_book_name = tk.StringVar()
var_book_name.set('搜尋')
entry_book_name = tk.Entry(window, textvariable = var_book_name)
entry_book_name.place(x=160, y=30)

def insert_point(out):
    t.insert('end',out)
    
def search():
    Key = var_book_name.get()
    Sanmin =urlopen("http://www.sanmin.com.tw/search/index/?ct=N&qu=" + urllib.parse.quote(Key) + "&ls=SD")
    SanminObj = BeautifulSoup(Sanmin, "html.parser")
    SanminList = SanminObj.findAll("li", {"class":"ProductName"})
    SanminList_child = SanminObj.findAll("span", {"class":{"Author","Publisher","PublisheDate","BaseInfo","Sale_Price"}})

    Book = urlopen("https://search.books.com.tw/search/query/key/" + urllib.parse.quote(Key) + "/cat/all")
    bookObj = BeautifulSoup(Book, "html.parser")
    BookList = bookObj.findAll("a",{"rel":"mid_name"})
    BookList_child = bookObj.findAll("a",{"rel":{"go_author","mid_publish",}})
    BookList_price = bookObj.find("span",{"class":"price"})

    for book in range(0,len(BookList)):
        BookList[book] = (BookList[book].get_text()).strip()
    BookList_price = (BookList_price.get_text()).replace("放入購物車","")
    BookList_price = BookList_price.replace("試閱","")
    BookList_price = BookList_price.strip()

    #KingStone = urlopen("https://www.kingstone.com.tw/search/result.asp?c_name=" + urllib.parse.quote(urllib.parse.quote(Key)) + "&se_type=4")
    #KingStoneObj = BeautifulSoup(KingStone, "html.parser")
    #KingStoneList = KingStoneObj.findAll("a",{"class":"anchor"})

    insert_point("三民書局：\n")
    
    insert_point(SanminList[0].get_text() + "\n")
    for child in range(0,5):
        insert_point(SanminList_child[child].get_text() + "\n")
    insert_point("\n\n博客來書局：\n")
    insert_point(BookList[0]+"\n")
    for child in range(0,3):    
        insert_point(BookList_child[child].get_text() + "\n")
    insert_point(BookList_price + "\n\n\n")
    
btn_search = tk.Button(window, text='Search', command=search)
btn_search.place(x=170, y=60)
btn_quit = tk.Button(window, text='Quit', command = window.destroy)
btn_quit.place(x=270, y=60)
t = tk.Text(window, height=25)
t.place(x=0, y=100, anchor='nw')


window.mainloop()
