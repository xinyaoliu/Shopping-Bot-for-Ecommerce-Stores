from tkinter import *
import tkinter.scrolledtext as tkst
import requests
import re
from urllib import parse, request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
from io import BytesIO
import webbrowser 
import tkinter.messagebox
import hashlib
import hmac
from Crypto.Cipher import AES

c1 = 'light yellow' #input here's color
c2 = '#E3CAA8' #background for root
c3 = '#D2B48C' #search button
c4 = 'white' #result context
c5 = 'dark red' #background for window head
c6 = '#D2B48C' #button for window
c7 = '#E3CAA8'  #background for window 
c8 = 'white' #color for character

root = Tk()
root2 = Toplevel()

root.title("Shopping Crawler - Login")
root.geometry('800x600')
root.resizable(width=True,height=True)
frameH=Frame(height=170,width=800,bg=c5).pack(expand=YES)
frame=Frame(height=600,width=800,bg=c2).pack(expand=YES,fill=BOTH)
LabelT= Label(root, text = "Shopping Crawler", font=("Blackletter",18),background= c5,foreground=c8).place(x=30,y=30)
LabelT= Label(root, text = "Login", font=("Blackletter",36),background= c5,foreground=c8).place(x=30,y=60)
LabelT= Label(root, text = "Username:", font=("Blackletter",20),background= c7).place(x=215,y=250)
LabelT= Label(root, text = "Password:", font=("Blackletter",20),background= c7).place(x=215,y=330)
usrn = StringVar()
e = Entry(root, textvariable = usrn, background = c1,borderwidth = 1, width = 14,font=("Arial",20))
e.place(x=325,y=247)
# e = Entry(root, textvariable = var, background = c1,borderwidth = 3, width = 10,font=("Arial",30))
# e.place(x=200,y=250)
password = StringVar() #Password variable
passEntry = Entry(root, textvariable=password, show='*', background = c1,borderwidth = 1, width = 14,font=("Arial",20))
passEntry.place(x=325,y=327)

root2.title("Shopping Crawler - Home")
root2.geometry('800x600')
# root2.resizable(width=True,height=True)
frameRt2=Frame(root2,height=170,width=800,bg=c5).pack(expand=YES)
frameRt=Frame(root2,height=600,width=800,bg=c2).pack(expand=YES,fill=BOTH)
LabelT= Label(root2, text = "Shopping Crawler", font=("Blackletter",18),background= c5,foreground=c8).place(x=30,y=30)
LabelT= Label(root2, text = "Home", font=("Blackletter",36),background= c5,foreground=c8).place(x=30,y=60)


var = StringVar()
e = Entry(root2, textvariable = var, background = c1,borderwidth = 3, width = 30,font=("Arial",30))
e.place(x=80,y=200)
window = Toplevel()
window.title("Shopping Crawler - Result")
window.geometry('1260x800')
frame2=Frame(window,height=115,width=1260,bg=c5).pack(expand=YES)
frame1=Frame(window,height=800,width=1260,bg=c7).pack(expand=YES,fill=BOTH)

LabelT= Label(window, text = "Shopping Crawler", font=("Blackletter",18),background= c5,foreground=c8).place(x=24,y=10)
LabelT= Label(window, text = "Result", font=("Blackletter",36),background= c5,foreground=c8).place(x=24,y=40)


# LabelW= Label(window, text = "Result:", font=("Arial",35),background=c5,foreground=c8).place(x=550,y=10)

Label1 = Label(window,text = "Macy's:",font=("Arial",20),background=c5,foreground=c8).place(x=195,y=90)
Label2 = Label(window,text = "Nord Strom:",font=("Arial",20),background=c5,foreground=c8).place(x=580,y=90)
Label3 = Label(window,text = "Saks Fifth Ave:",font=("Arial",20),background=c5,foreground=c8).place(x=945,y=90)

window.resizable(width=True,height=True)
text1 = tkst.ScrolledText(window, width=53,height=33,background=c4)
text1.tag_configure('big',font=("Arial",20))
text1.place(x=31, y=115)
text2 = tkst.ScrolledText(window, width=53,height=33,background=c4)
text2.tag_configure('big',font=("Arial",20))
text2.place(x=435,y=115)
text3 = tkst.ScrolledText(window, width=53,height=33,background=c4)
text3.tag_configure('big',font=("Arial",20))
text3.place(x=841,y=115)
LINKS1 = []
LINKS2 = []
LINKS3 = []

def getHTMLText(url):
  req = Request(url , headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko)', 'usage':'For JHU 601.666 final project use', 'contact':'xliu106@jhu.edu or ywei30@jhu.edu'} )
  webpage = urlopen(req).read()
  webpage = webpage.decode('utf-8')
  return webpage


def parse(html, flag):
  if flag == 1: #nordstrom
    nord_title = []
    nord_price = []
    nord_pic = []
    nord_link = []
    nord_title = re.findall(r'yes\"\salt=\"[^\"]+\"', str(html))
    for i in range(len(nord_title)):
      nord_title[i] = re.sub(r'\s*\&\#x27\;', '\'', nord_title[i])
      nord_title[i] = re.sub(r'\&amp\;', '&', nord_title[i])
      nord_title[i] = nord_title[i][10:-1]

    for i in range(len(nord_title)):
      first = nord_title[i].split()[0]
      f_index = first.find('\'')
      if f_index == -1:
        reg = 'a\shref=\"\/s\/' + first[:-1].lower() + '[\S]+\"'
      else:
        reg = 'a\shref=\"\/s\/' + first[:f_index].lower() + '[\S]+\"'
      a = re.findall(reg, str(html))
      nord_link.append('https://shop.nordstrom.com' + a[0][8:-1])

    nord_pic = re.findall(r'\"https\:\/\/n\.nordstrommedia\.com\/ImageGallery\/store\/product\/Zoom\/[^\"]+\"\salt\=', str(html))

    for i in range(len(nord_pic)):
      nord_pic[i] = nord_pic[i][1:-6]
    nord_price = re.findall(r'Now\:\s\<\/span\>\<span\sclass\=\"[\S]+"\sdata-reactid=\"\d+\"\>\$\d*\,*\d*\,*\d+\.\d+\<|\"\>\<span\sclass\=\"[\S]+"\sdata-reactid=\"\d+\"\>\$\d*\,*\d*\,*\d+\.\d+\<|Now\:\s\<\/span\>\<span\sclass\=\"[\S]+"\sdata-reactid=\"\d+\"\>\$\d*\,*\d*\,*\d+\.\d+\s\–\s\$\d*\,*\d*\,*\d+\.\d+\<|\"\>\<span\sclass\=\"[\S]+"\sdata-reactid=\"\d+\"\>\$\d*\,*\d*\,*\d+\.\d+\s\–\s\$\d*\,*\d*\,*\d+\.\d+\<', str(html))
    for i in range(len(nord_price)):
      nord_price[i] = re.findall(r'\d*\,*\d*\,*\d+\.\d+', nord_price[i])
      if len(nord_price[i]) == 1:
        if nord_price[i][0].find(',') == -1:
          nord_price[i] = [nord_price[i][0], 0]
        else:
          nord_price[i] = [nord_price[i][0].replace(',', ''), 0]
      else:
        if nord_price[i][0].find(',') == -1 and nord_price[i][1] == -1:
          nord_price[i] = [nord_price[i][0], nord_price[i][1]]
        elif nord_price[i][0] == -1:
          nord_price[i] = [nord_price[i][0], nord_price[i][1].replace[',', '']]
        else:
          nord_price[i] = [nord_price[i][0].replace(',', ''), nord_price[i][1].replace(',', '')]
    
    if not default.get():
      nord_price1 = []
      nord_price2 = []

      for i in range(min(12, len(nord_price))):
        nord_price1.append(float(nord_price[i][0]))
        nord_price2.append(float(nord_price[i][1]))

      data = [(price1, price2,  title, pic, link) for price1, price2, title, pic, link in zip(nord_price1, nord_price2, nord_title, nord_pic, nord_link)]
      data.sort()
      nord_title = [title for price1, price2, title, pic, link in data]
      nord_pic = [pic for price1, price2, title, pic, link in data] 
      nord_link = [link for price1, price2, title, pic, link in data]


      for i in range(min(12, len(nord_title))):
        num1 = data[i][0]
        num2 = data[i][1]
        if num2 == 0:
          nord_price[i] = '$' + str(num1)
        else:
          nord_price[i] = '$' + str(num1) + ' - ' + '$' + str(num2)
      
    return [nord_title, nord_pic, nord_price, nord_link]

  if flag == 2:  #macys
    soup = BeautifulSoup(html, 'html.parser')
    macys_title = []
    macys_price = []
    macys_pic = []
    macys_link = []
    link = soup.find_all(class_ = 'productThumbnailImage')
    link2 = soup.find_all(class_ = 'productDescription')

    for i in range(min(12, len(link))):
      macys_title.append(link[i].a.attrs['title'])
      macys_pic.append(link[i].img.attrs['src'])
      price = link2[i].find_all(attrs={'class':'regular'})
      price2 = link2[i].find_all(attrs={'class':'discount'})
      macys_link.append('https://www.macys.com' + link[i].a.attrs['href'])
      if len(price2) > 0:
        macys_price.append([re.findall(r'\d*\,*\d+\.\d+', str(price[0]))[0].replace(',', ''),re.findall(r'\d*\,*\d+\.\d+', str(price2[0]))[0].replace(',', '')])
      elif len(price) > 0:

        macys_price.append([re.findall(r'\d*\,*\d+\.\d+', str(price[0]))[0].replace(',', ''), 0])
      else:
        price = link2[i].find_all(attrs={'class':"edv"})
        macys_price.append([re.findall(r'\d*\,*\d+\.\d+', str(price[0]))[0].replace(',', ''), 0])

 
    if not default.get():
      macys_price1 = []
      macys_price2 = []

      for i in range(min(12, len(macys_price))):
        macys_price1.append(float(macys_price[i][0]))
        macys_price2.append(float(macys_price[i][1]))

      data = [(price2, price1,  title, pic, link) for price1, price2, title, pic, link in zip(macys_price1, macys_price2, macys_title, macys_pic, macys_link)]
      data.sort()
      macys_title = [title for price1, price2, title, pic, link in data]
      macys_pic = [pic for price1, price2, title, pic, link in data] 
      macys_link = [link for price1, price2, title, pic, link in data]

      for i in range(min(12, len(macys_title))):
        num1 = data[i][0] #price 2
        num2 = data[i][1] #price 1
        if num1 == 0:
          macys_price[i] = '$' + str(num1)
        else:
          macys_price[i] = '$' + str(num1) + '   Sale:' + '$' + str(num2)
      

    return [macys_title, macys_pic, macys_price, macys_link]

  if flag == 3: #saks
    saks_title = []
    saks_price = []
    saks_pic = []
    saks_link = []
    soup = BeautifulSoup(html, 'html.parser')
    discription = soup.find_all(class_ = 'product-text')
    for i in range(min(12, len(discription))):
      saks_link.append(discription[i].a.attrs['href'])

    saks_title = re.findall(r'\<p\sclass\=\"product\-description\"\spriority\=\"9999\"\>[^\"]+\<\/p\>',str(html))
    for i in range(min(12, len(saks_title))):
        saks_title[i] = saks_title[i][47:-4]
        saks_title[i] = re.sub(r'\s*\&amp;','',saks_title[i]) 
    saks_pic = re.findall(r'\<img\sdata\-src\=\"\/\/image\.s5a\.com\/is\/image\/saks\/[\d]*\_247x329\.jpg"', str(html))
    for i in range(min(12, len(saks_pic))):
        saks_pic[i] = saks_pic[i][15:-1]
    saks_price = re.findall(r'[Now\s]*\<span\sclass\=\"product\-[sale\-]*price\"\>[\s]*\&\#\d+\;\d*\,*\d+\.\d+[\s\-\s\s\&\#\d+\;\d+\.\d+]*\<\/span\>',str(html))
    for i in range(min(12, len(saks_price))):
        saks_price[i] = re.findall(r'\d+\.\d+', saks_price[i])
        if(len(saks_price[i])==1):
           saks_price[i] = [(saks_price[i][0]), 0]
        else:
           saks_price[i] = [(saks_price[i][1]), (saks_price[i][0])]
    
    if not default.get():
      saks_price1 = []
      saks_price2 = []

      for i in range(min(12, len(saks_price))):
        saks_price1.append(float(saks_price[i][0]))
        saks_price2.append(float(saks_price[i][1]))

      data = [(price1, price2,  title, pic, link) for price1, price2, title, pic, link in zip(saks_price1, saks_price2, saks_title, saks_pic, saks_link)]
      data.sort()
      saks_title = [title for price1, price2, title, pic, link in data]
      saks_pic = [pic for price1, price2, title, pic, link in data] 
      saks_link = [link for price1, price2, title, pic, link in data]

      print (data)
      print (len(saks_title))

      for i in range(min(12, len(saks_title))):
        num1 = data[i][0]
        num2 = data[i][1]
        if num2 == 0:
          saks_price[i] = '$' + str(num1)
        else:
          saks_price[i] = '$' + str(num1) + ' - ' + '$' + str(num2)
    

    return [saks_title, saks_pic, saks_price, saks_link]

def ret():
   window.withdraw()
   text1.delete(1.0,END)
   text2.delete(1.0,END)
   text3.delete(1.0,END)
   root2.deiconify()
Buttonws = Button(window,text = "Search Again" , command = ret,font=("Arial",25), width =15,background=c6).place(x=380, y=640)
def quitAll():
   if tkinter.messagebox.askyesno('Confirmation', 'Are you sure to quit all?'):
      root.quit()
      root2.quit()
      window.quit()
Buttonwq = Button(window,text = "Quit" , command = quitAll,font=("Arial",25), width=15,background=c6).place(x=680, y=640)
window.withdraw()
root2.withdraw()

def quit():
  root.quit()

photo1 = []
photo2 = []
photo3 = []  #global variable to plot for image_create


def home():
  secret_key = "SecretKeyForProj" #must be 16x
  iv_param = 'This is an IV456'
  usr = usrn.get()
  psw = password.get()
  #h = hashlib.sha256()
  #h1 = hmac.new('key', 'Hello, ')
  #h = hmac.sha256()
  #h.update(bytes(psw, encoding='utf-8'))
  if(len(psw)!=16):
    tkinter.messagebox.showerror("Input error", "password must be length of 16")
  aes1 = AES.new(secret_key, AES.MODE_CBC, iv_param)
  cipher_data = aes1.encrypt(psw)
  if usr == '' or cipher_data == '':
    tkinter.messagebox.showerror("Login error","Please enter your username and password")
  else:
    aes2 = AES.new(secret_key, AES.MODE_CBC, 'This is an IV456')
    pawd_result= aes2.decrypt(cipher_data)
    #print(pawd_result, pawd_result == b'1234567890123456')
    if usr =='admin' and pawd_result == b'1234567890123456':
       root.withdraw()
       root2.deiconify()
    else:
       if(usr!='admin'):
          tkinter.messagebox.askretrycancel("Input error","Your username are not existed")
       else:
          tkinter.messagebox.askretrycancel("Input error","Your password are not matched")

def mainfun():
 keyword = var.get()
 if(keyword==''):
  tkinter.messagebox.showerror("No query for search","Please give some input query")
 else:
  root2.withdraw()
  window.deiconify()

  keyword_count = keyword.split()
  if len(keyword_count) > 1:
    keyword = ''
    for i in range(len(keyword_count)):
      keyword = keyword + '+' + keyword_count[i]  
  
  
  nord_list = []
  saks_list = []
  macys_list = []


  if(v1.get()==False):
    text1.insert(1.0,"Not choosed, no output\n",'big')
  else: #todo: macy's
    macys = 'https://www.macys.com/shop/featured/'
    macys_keyword = keyword + '?ss=true'
    macysurl = macys + macys_keyword
    macys_html = getHTMLText(macysurl)
    macys_list = parse(macys_html, 2)
    #print(macys_list[1])
    if(len(macys_list[1])<=0):
        text1.insert(END,"Sorry, result not found\n",'big')
    else:
      global LINKS1
      LINKS1 = macys_list[3]
      for i in range(min(12, len(macys_list[0]))):
        response = requests.get(macys_list[1][i])
        image = Image.open(BytesIO(response.content))
        image = image.resize((40,40),Image.ANTIALIAS)
        photo1.append(ImageTk.PhotoImage(image))
        text1.image_create(float(4 * i+1),image=photo1[-1])
        text1.insert(float(4 * i+2), macys_list[0][i] + '\n',('link', str(i)))
        if(not default.get()):
            text1.insert(float(4 * i+3), '      price:   ' + macys_list[2][i] + '\n','big')
        else:
            text1.insert(float(4 * i+3), '      price:   ' + macys_list[2][i][0] + '\n','big')
        text1.tag_config('link', foreground = "blue",font =('Arial', 18))
        text1.tag_bind('link','<Button-1>',showLink1)
        text1.insert(float(4 * i+4), '-----------------------------------------------------')
        text1.insert(float(4 * i+4), '\n')
  if(v2.get()==False):
    text2.insert(1.0,"Not choosed, no output\n",'big')
  else: #todo: Nord Strom
    nord = 'https://shop.nordstrom.com/sr?contextualcategoryid=2375500&origin=keywordsearch&keyword='
    nordurl = nord + keyword
    nord_html = getHTMLText(nordurl)
    nord_list = parse(nord_html, 1)
    nord_len = len(nord_list[0])
    #print (nord_list[1])
    if(len(nord_list[1])<=0):
        text2.insert(END,"Sorry,result not found\n",'big')
    else:
      global LINKS2
      LINKS2 = nord_list[3]
      for i in range(min(12, nord_len)):
        response = requests.get(nord_list[1][i])
        image = Image.open(BytesIO(response.content))
        image = image.resize((40,40),Image.ANTIALIAS)
        photo2.append(ImageTk.PhotoImage(image))
        text2.image_create(float(4 * i+1),image=photo2[-1])
        text2.insert(float(4 * i+2), nord_list[0][i] + '\n' ,('link', str(i)))
        #print(nord_list[2][i])
        if(not default.get()):
            text2.insert(float(4 * i+3), '      price:   ' + nord_list[2][i] + '\n','big')
        else:
            text2.insert(float(4 * i+3), '      price:   ' + nord_list[2][i][0] + '\n','big')
        text2.insert(float(4 * i+4), '-----------------------------------------------------')
        text2.insert(float(4 * i+4), '\n')
      text2.tag_config('link',foreground="blue",font =('Arial', 18))
      text2.tag_bind('link','<Button-1>',showLink2)
  if(v3.get()==False):
    text3.insert(1.0,"Not choosed, no output\n",'big')
  else: #todo: Saks Fifth Ave
    saks = 'https://www.saksfifthavenue.com/search/EndecaSearch.jsp?bmForm=header-search&bmFormID=md2VBWy&bmUID=md2VBWz&bmIsForm=true&bmPrevTemplate=%2FEntry.jsp&bmArch=bmForm&bmForm=endeca_search_form_one&bmHidden=submit-search&submit-search=&bmArch=bmSingle&bmSingle=N_Dim&bmHidden=N_Dim&N_Dim=0&bmArch=bmHidden&bmHidden=Ntk&bmHidden=Ntk&Ntk=Entire+Site&bmArch=bmHidden&bmHidden=Ntx&bmHidden=Ntx&Ntx=mode%2Bmatchpartialmax&bmHidden=Ntt&Ntt='
    saks_keyword = keyword + '&bmText=SearchString&SearchString=' + keyword
    saksurl = saks + saks_keyword
    saks_html = getHTMLText(saksurl)
    saks_list = parse(saks_html, 3)
    if(len(saks_list[1])<=0):
        text3.insert(END,"Sorry, result not found\n",'big')
    else:
      global LINKS3
      LINKS3 = saks_list[3]
      for i in range(min(12, len(saks_list[0]))):
        response = requests.get('https:'+saks_list[1][i])
        image = Image.open(BytesIO(response.content))
        image = image.resize((40,40),Image.ANTIALIAS)
        photo3.append(ImageTk.PhotoImage(image))
        text3.image_create(float(4 * i+1),image=photo3[-1])
        text3.insert(float(4 * i+2), saks_list[0][i] +'\n',('link', str(i)))
        if(not default.get()):
            text3.insert(float(4 * i+3), '      price:   ' + saks_list[2][i] + '\n','big')
        else:
            text3.insert(float(4 * i+3), '      price:   ' + saks_list[2][i][0] + '\n','big')
        text3.insert(float(4 * i+4), '-----------------------------------------------------')
        text3.insert(float(4 * i+4), '\n')
      text3.tag_config('link',foreground="blue",font =('Arial', 18))
      text3.tag_bind('link','<Button-1>',showLink3)

def showLink1(event):
    idx = int(event.widget.tag_names(CURRENT)[1])
    webbrowser.open(LINKS1[idx])

def showLink2(event):
    idx = int(event.widget.tag_names(CURRENT)[1])
    webbrowser.open(LINKS2[idx])

def showLink3(event):
    idx = int(event.widget.tag_names(CURRENT)[1])
    webbrowser.open(LINKS3[idx])

v1 = IntVar()
check1 = Checkbutton(root2,variable = v1,text = "Macy's",font=("Arial",20),background=c2)
check1.place(x=90,y=300)
v2 = IntVar()
check2 = Checkbutton(root2,variable = v2,text = "Nord Strom",font=("Arial",20),background=c2)
check2.place(x=90,y=380)
v3 = IntVar()
check3 = Checkbutton(root2,variable = v3, text = "Saks Fifth Ave",font=("Arial",20),background=c2)
check3.place(x=90,y=460)

default = IntVar()
default.set(0)
radio1 = Radiobutton(root2,variable = default,value = 0,text='price low to high',font=("Arial",20),background=c2)
radio1.place(x =350,y=300)
radio2 = Radiobutton(root2,variable = default,value = 1,text='relevance',font=("Arial",20),background=c2)
radio2.place(x =350,y=380)

Button00 = Button(root,text = "Sign in",width = 6,command = home,font=("Arial",20),background=c3)
Button00.place(x=290,y=420)
Button01 = Button(root,text = "Quit",width = 5,command = quitAll,font=("Arial",20),background=c3)
Button01.place(x=390,y=420)

Button1 = Button(root2,text = "Search",width = 6,command = mainfun,font=("Arial",35),background=c3)
Button1.place(x=620,y=200)


#Button2 = Button(root,text = "Quit", width = 6,command = quitAll,font=("Arial",25),background='#71AFA4')
#Button2.place(x=620,y=250)
root.mainloop()

