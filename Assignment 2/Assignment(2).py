
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10229825
#    Student name: Levi Breakwell
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Online Shopping Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for simulating an online shopping experience.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.
#

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + \
                        url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents
#
#--------------------------------------------------------------------#
#-----Student's Solution---------------------------------------------#
# Put your solution at the end of this file.
# Name of the invoice file. To simplify marking, your program should
# generate its invoice using this file name.
invoice_file = 'invoice.html'

total = 0
### The 4 URL's that the catagries are coming from
#Home Decor
url_1 = "http://india-shopping.khazano.com/rss/catalog/category/cid/11store_id/1/"
#Stationary
url_2 = open('stationary.xhtml')
html_2 = url_2.read()
#Indian Handicrafts
url_3 = open('handicrafts.xhtml')
html_3 = url_3.read()
#Fashion Bags
url_4 = "http://india-shopping.khazano.com/rss/catalog/category/cid/4store_id/1/"

### Getting the HTML's into a string
web_doc = urlopen(url_1)
web_doc_bytes = web_doc.read()
html_1 = web_doc_bytes.decode('UTF-8')
web_doc.close()

web_doc = urlopen(url_4)
web_doc_bytes = web_doc.read()
html_4 = web_doc_bytes.decode('UTF-8')
web_doc.close()

### To find Titles of page and items and put in list called titles
## website 1
start_tag = '<title><![CDATA['
end_tag=']]></title>'
end_pos = 0
starting_pos = html_1.find(start_tag,end_pos)
end_pos = html_1.find(end_tag,starting_pos)
global titles_web1
titles_web1 = []
for title in range(11):
    if starting_pos !=-1 and end_pos !=-1:   
        titles_web1.append(html_1[starting_pos + len(start_tag) : end_pos])
        starting_pos = html_1.find(start_tag,end_pos)
        end_pos = html_1.find(end_tag,starting_pos)
## website 2
start_tag = '<title><![CDATA['
end_tag=']]></title>'
end_pos = 0
starting_pos = html_2.find(start_tag,end_pos)
end_pos = html_2.find(end_tag,starting_pos)
titles_web2 = []
for title in range(11):
    if starting_pos !=-1 and end_pos !=-1:   
        titles_web2.append(html_2[starting_pos + len(start_tag) : end_pos])
        starting_pos = html_2.find(start_tag,end_pos)
        end_pos = html_2.find(end_tag,starting_pos)
## website 3
start_tag = '<title><![CDATA['
end_tag=']]></title>'
end_pos = 0
starting_pos = html_3.find(start_tag,end_pos)
end_pos = html_3.find(end_tag,starting_pos)
titles_web3 = []
for title in range(11):
    if starting_pos !=-1 and end_pos !=-1:   
        titles_web3.append(html_3[starting_pos + len(start_tag) : end_pos])
        starting_pos = html_3.find(start_tag,end_pos)
        end_pos = html_3.find(end_tag,starting_pos)
## website 4
start_tag = '<title><![CDATA['
end_tag=']]></title>'
end_pos = 0
starting_pos = html_4.find(start_tag,end_pos)
end_pos = html_4.find(end_tag,starting_pos)
titles_web4 = []
for title in range(11):
    if starting_pos !=-1 and end_pos !=-1:   
        titles_web4.append(html_4[starting_pos + len(start_tag) : end_pos])
        starting_pos = html_4.find(start_tag,end_pos)
        end_pos = html_4.find(end_tag,starting_pos)
### To find prices of items and put them in a list called prices
prices_web1 = findall('id="product-price-[0-9]+">(?:<span class="price">|">)?Rs\. ([0-9]*\,*[0-9]+\.[0-9]+)</span>',html_1)
prices_temp1 =[]
for price in prices_web1:
    prices_temp1.append(price.replace(',',''))
prices_web1 = prices_temp1

prices_web2 = findall('id="product-price-[0-9]+">(?:<span class="price">|">)?Rs\. ([0-9]*\,*[0-9]+\.[0-9]+)</span>',html_2)
prices_temp2 =[]
for price in prices_web2:
    prices_temp2.append(price.replace(',',''))
prices_web2 = prices_temp2

prices_web3 = findall('id="product-price-[0-9]+">(?:<span class="price">|">)?Rs\. ([0-9]*\,*[0-9]+\.[0-9]+)</span>',html_3)
prices_temp3 =[]
for price in prices_web3:
    prices_temp3.append(price.replace(',',''))
prices_web3 = prices_temp3

prices_web4 = findall('id="product-price-[0-9]+">(?:<span class="price">|">)?Rs\. ([0-9]*\,*[0-9]+\.[0-9]+)</span>',html_4)
prices_temp4 =[]
for price in prices_web4:
    prices_temp4.append(price.replace(',',''))
prices_web4 = prices_temp4

### To find photos
photos_web1 = findall('<img src="(http://india-shopping\.khazano\.com/media/catalog/product/cache/1/thumbnail/.+\.jpg)"',html_1)
photos_web2 = findall('<img src="(http://india-shopping\.khazano\.com/media/catalog/product/cache/1/thumbnail/.+\.jpg)"',html_2)
photos_web3 = findall('<img src="(http://india-shopping\.khazano\.com/media/catalog/product/cache/1/thumbnail/.+\.jpg)"',html_3)
photos_web4 = findall('<img src="(http://india-shopping\.khazano\.com/media/catalog/product/cache/1/thumbnail/.+\.jpg)"',html_4)

### Putting all items into one list
web1 = []
web2 = []
web3 = []
web4 = []
for i in range (10):
    items1= titles_web1[i+1],prices_web1[i],photos_web1[i]
    web1.append(items1)
    items2= titles_web2[i+1],prices_web2[i],photos_web2[i]
    web2.append(items2)
    items3= titles_web3[i+1],prices_web3[i],photos_web3[i]
    web3.append(items3)
    items4= titles_web4[i+1],prices_web4[i],photos_web4[i]
    web4.append(items4)
all_items = []
all_items.append(web1)
all_items.append(web2)
all_items.append(web3)
all_items.append(web4)


###Setting up tKInter window
home = Tk()
home.title('The Greatest Indian Online Store')
#home.minsize(width = 300)
title = Label(home, text = 'Indian Homemades', font = ('comic sans ms', 20),pady = 1,padx = 20, borderwidth=2, relief="raised")
cart_items = []
item = IntVar()

def add():
    cart_items.append(item.get())


constant_html = '''<!DOCTYPE html>
<html>
<head>
<style>
div.container {
    width: 100%;
    border: 1px solid gray;
}
header, footer {
    padding: 1em;
    color: white;
    background-color: black;
    clear: left;
    text-align: center;
    border-bottom: 1px solid gray;
    h2{ font-size: 20px}
}
nav {
    float: left;
    max-width: 160px;
    margin: 0;
    padding: 1em;
}

nav ul {
    list-style-type: none;
    padding: 0;
}
   
nav ul a {
    text-decoration: none;
}

article {
    
    border: 1px solid gray;
    padding: 1em;
    overflow: hidden;
}
</style>
</head>
<body>

<div class="container">

<header>
   <h1>Your Indian Invoice</h1>'''
from sqlite3 import *   
def view():
    source =0
    htmlsource = 0
    invoice_list= []
    totalru = 0
    global total
    ###Linking number values on radio buttons with product info
    for product in cart_items:
        if product>=30 :
            htmlsource = 3
        elif product>20 :
            htmlsource = 2
        elif product>10 :
            htmlsource = 1
        else:
            htmlsource = 0

        if product >=30 :
            source = int(product)-30
        elif product >=20 :
            source = int(product)-20
        elif product >=10 :
            source = int(product)-10
        else :
            source = int(product)
            ###creating list of items added to cart with their info
        invoice_list.append(all_items[htmlsource][source])        
        totalru = totalru + float(all_items[htmlsource][source][1])
        total = round(totalru/51,2)
    #print(total)        
    #print(invoice_list)


    def write_html_for_cart():
        cart_html = ''
        if invoice_list == []:
            cart_html = '''<article>\
        <h1> You have no items in your cart! </h1>\
        '''
        else:
            cart_html =""
            for cart_item in invoice_list:
                cart_html =cart_html+ '''\
                <article>\
                <h1>''' + cart_item[0]+'''</h1>\
                <nav>
                  <ul>
                    <li><img src="''' + cart_item[2] +'''" </li>
                  </ul>
                </nav>
                <p> '''+ (cart_item[1])+''' Ru </p>\
                </article>'''
                
                
        return cart_html

    
    closing_html='''<footer><a href="http://india-shopping.khazano.com/rss/catalog/category/cid/11store_id/1/">Home Decor</a></footer>\
            <footer><a href="http://india-shopping.khazano.com/rss/catalog/category/cid/17store_id/1/">Stationary</a></footer>\
            <footer><a href="http://india-shopping.khazano.com/rss/catalog/category/cid/5store_id/1/">Indian Handicrafts</a></footer>\
            <footer><a href="http://india-shopping.khazano.com/rss/catalog/category/cid/4store_id/1/">Fashion Bags</a></footer>\
            </div>       </body>       </html>'''
     
    summary_line = '''<h2>You have '''+ str(len(cart_items))+ \
                   ''' items in your cart, at a total of AUD$ '''\
                   +str(total)+'''</h2>
                    </header>'''
    
    invoice = open('invoice.html', 'w')
    html_invoice_script = constant_html+ summary_line\
    + write_html_for_cart() + closing_html
    invoice.write(str(html_invoice_script))

    ###PART B DATABASE INVOICE
    connection = connect(database = 'shopping_cart.db')
    shopping_cart_db = connection.cursor()
    template = '''INSERT INTO ShoppingCart VALUES ('TITLE','PRICE')'''
    sql_delete = """DELETE FROM ShoppingCart"""
    shopping_cart_db.execute(sql_delete)
    for cart_item in invoice_list:
        shopping_cart_db.execute(template.replace('TITLE', cart_item[0]).replace('PRICE',cart_item[1]))
    connection.commit()
    shopping_cart_db.close()
    connection.close()
    ### END OF PART B
    
def home_decor_window():
    home_decor = Toplevel()
    home_decor.title('Home Decoration Store')
    ###Creating the labels displaying item names and prices
    products = Frame(home_decor)
    item1=Radiobutton(products,text=titles_web1[1]+"    "+prices_web1[0],variable=item,value=0).grid(row=1,column=1)
    item2=Radiobutton(products,text=titles_web1[2]+"    "+prices_web1[1],variable=item,value=1).grid(row=2,column=1)
    item3=Radiobutton(products,text=titles_web1[3]+"    "+prices_web1[2],variable=item,value=2).grid(row=3,column=1)
    item4=Radiobutton(products,text=titles_web1[4]+"    "+prices_web1[3],variable=item,value=3).grid(row=4,column=1)
    item5=Radiobutton(products,text=titles_web1[5]+"    "+prices_web1[4],variable=item,value=4).grid(row=5,column=1)
    item6=Radiobutton(products,text=titles_web1[6]+"    "+prices_web1[5],variable=item,value=5).grid(row=1,column=2)
    item7=Radiobutton(products,text=titles_web1[7]+"    "+prices_web1[6],variable=item,value=6).grid(row=2,column=2)
    item8=Radiobutton(products,text=titles_web1[8]+"    "+prices_web1[7],variable=item,value=7).grid(row=3,column=2)
    item9=Radiobutton(products,text=titles_web1[9]+"    "+prices_web1[8],variable=item,value=8).grid(row=4,column=2)
    item10=Radiobutton(products,text=titles_web1[10]+"    "+prices_web1[9],variable=item,value=9).grid(row=5,column=2)
    products.pack()
    add_btn=Button(home_decor,text='Add to cart',command=add).pack(fill = 'both')
    view_btn=Button(home_decor,text='Print Invoice',command=view).pack(fill = 'both')
    url_link = Label(home_decor, text='http://india-shopping.khazano.com/rss/catalog/category/cid/11store_id/1/', borderwidth=2, relief="groove").pack()
    

    
def stationary_window():
    stationary = Toplevel()
    stationary.title('Stationary Store')
    ###Creating the labels displaying item names and prices
    products = Frame(stationary)
    item1=Radiobutton(products,text=titles_web2[1]+"    "+prices_web2[0],variable=item,value=10).grid(row=1,column=1)
    item2=Radiobutton(products,text=titles_web2[2]+"    "+prices_web2[1],variable=item,value=11).grid(row=2,column=1)
    item3=Radiobutton(products,text=titles_web2[3]+"    "+prices_web2[2],variable=item,value=12).grid(row=3,column=1)
    item4=Radiobutton(products,text=titles_web2[4]+"    "+prices_web2[3],variable=item,value=13).grid(row=4,column=1)
    item5=Radiobutton(products,text=titles_web2[5]+"    "+prices_web2[4],variable=item,value=14).grid(row=5,column=1)
    item6=Radiobutton(products,text=titles_web2[6]+"    "+prices_web2[5],variable=item,value=15).grid(row=1,column=2)
    item7=Radiobutton(products,text=titles_web2[7]+"    "+prices_web2[6],variable=item,value=16).grid(row=2,column=2)
    item8=Radiobutton(products,text=titles_web2[8]+"    "+prices_web2[7],variable=item,value=17).grid(row=3,column=2)
    item9=Radiobutton(products,text=titles_web2[9]+"    "+prices_web2[8],variable=item,value=18).grid(row=4,column=2)
    item10=Radiobutton(products,text=titles_web2[10]+"    "+prices_web2[9],variable=item,value=19).grid(row=5,column=2)
    products.pack()
    add_btn=Button(stationary,text='Add to cart',command=add).pack(fill = 'both')
    view_btn=Button(stationary,text='Print Invoice',command=view).pack(fill = 'both')
    url_link = Label(stationary, text='http://india-shopping.khazano.com/rss/catalog/category/cid/17store_id/1/', borderwidth=2, relief="groove").pack()
    
def handicrafts_window():
    handicrafts = Toplevel()
    handicrafts.title('Indian Handicrafts Store')
        ###Creating the labels displaying item names and prices
    products = Frame(handicrafts)
    item1=Radiobutton(products,text=titles_web3[1]+"    "+prices_web3[0],variable=item,value=20).grid(row=1,column=1)
    item2=Radiobutton(products,text=titles_web3[2]+"    "+prices_web3[1],variable=item,value=21).grid(row=2,column=1)
    item3=Radiobutton(products,text=titles_web3[3]+"    "+prices_web3[2],variable=item,value=22).grid(row=3,column=1)
    item4=Radiobutton(products,text=titles_web3[4]+"    "+prices_web3[3],variable=item,value=23).grid(row=4,column=1)
    item5=Radiobutton(products,text=titles_web3[5]+"    "+prices_web3[4],variable=item,value=24).grid(row=5,column=1)
    item6=Radiobutton(products,text=titles_web3[6]+"    "+prices_web3[5],variable=item,value=25).grid(row=1,column=2)
    item7=Radiobutton(products,text=titles_web3[7]+"    "+prices_web3[6],variable=item,value=26).grid(row=2,column=2)
    item8=Radiobutton(products,text=titles_web3[8]+"    "+prices_web3[7],variable=item,value=27).grid(row=3,column=2)
    item9=Radiobutton(products,text=titles_web3[9]+"    "+prices_web3[8],variable=item,value=28).grid(row=4,column=2)
    item10=Radiobutton(products,text=titles_web3[10]+"    "+prices_web3[9],variable=item,value=29).grid(row=5,column=2)
    products.pack()
    add_btn=Button(handicrafts,text='Add to cart',command=add).pack(fill = 'both')
    view_btn=Button(handicrafts,text='Print Invoice',command=view).pack(fill = 'both')
    url_link = Label(handicrafts, text='http://india-shopping.khazano.com/rss/catalog/category/cid/5store_id/1/', borderwidth=2, relief="groove").pack()

def bags_window():
    fashion_bags = Toplevel()
    fashion_bags.title('Fashion Bags Store')
        ###Creating the labels displaying item names and prices
    products = Frame(fashion_bags)
    item1=Radiobutton(products,text=titles_web4[1]+"    "+prices_web4[0],variable=item,value=30).grid(row=1,column=1)
    item2=Radiobutton(products,text=titles_web4[2]+"    "+prices_web4[1],variable=item,value=31).grid(row=2,column=1)
    item3=Radiobutton(products,text=titles_web4[3]+"    "+prices_web4[2],variable=item,value=32).grid(row=3,column=1)
    item4=Radiobutton(products,text=titles_web4[4]+"    "+prices_web4[3],variable=item,value=33).grid(row=4,column=1)
    item5=Radiobutton(products,text=titles_web4[5]+"    "+prices_web4[4],variable=item,value=34).grid(row=5,column=1)
    item6=Radiobutton(products,text=titles_web4[6]+"    "+prices_web4[5],variable=item,value=35).grid(row=1,column=2)
    item7=Radiobutton(products,text=titles_web4[7]+"    "+prices_web4[6],variable=item,value=36).grid(row=2,column=2)
    item8=Radiobutton(products,text=titles_web4[8]+"    "+prices_web4[7],variable=item,value=37).grid(row=3,column=2)
    item9=Radiobutton(products,text=titles_web4[9]+"    "+prices_web4[8],variable=item,value=38).grid(row=4,column=2)
    item10=Radiobutton(products,text=titles_web4[10]+"    "+prices_web4[9],variable=item,value=39).grid(row=5,column=2)
    products.pack()
    add_btn=Button(fashion_bags,text='Add to cart',command=add).pack(fill = 'both')
    view_btn=Button(fashion_bags,text='Print Invoice',command=view).pack(fill = 'both')
    url_link = Label(fashion_bags, text='http://india-shopping.khazano.com/rss/catalog/category/cid/4store_id/1/', borderwidth=2, relief="groove").pack()
img = PhotoImage(file='logo.gif')
logo = Label(home, image = img).pack(side = 'left')
oldies = Frame(home, bd=3, relief=SUNKEN)
latest = Frame(home, bd=3, relief=SUNKEN)
home_decor_btn = Button(latest, text = 'Home Decoration',height= 2, command = home_decor_window)
stationary_btn = Button(oldies, text = 'Stationary',height = 2, command = stationary_window)
handicrafts_btn = Button(oldies, text = 'Indian Handicrafts',height = 2, command = handicrafts_window)
bags_btn = Button(latest, text = 'Fashion Bags',height = 2, command = bags_window)
products = Frame(home,pady = 40)

title.pack()
oldies_lbl = Label(oldies,text = 'Oldies but Goodies').pack(fill = 'both')
oldies.pack(side='right',fill = 'both')
latest_lbl = Label(latest, text = 'Latest n Greatest').pack(fill = 'both')
latest.pack(side='left',fill = 'both')
home_decor_btn.pack()
stationary_btn.pack()
handicrafts_btn.pack()
bags_btn.pack()
home.mainloop()


