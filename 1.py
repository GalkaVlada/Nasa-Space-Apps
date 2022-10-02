from tkinter import*
import tkinter as tk
from PIL import Image, ImageTk
import requests
import time
import matplotlib.pyplot as plt 
import requests 
 

#Работа с данными
a = requests.get('https://services.swpc.noaa.gov/text/rtsw/data/plasma-1-day.i.json').text.replace('"', '').replace('[', '').replace(']', '').split('\n')[::] 
b = [] 
for i in range(22): 
  b.append(a[i]) 
a = b 
del b 
b=[] 
for i in a[1:]: 
  i = i[len('2022-10-01 15:16:00,'):-7] 
  i = i.split(',') 
  i = list(map(float, i)) 
  i = list(map(int, i)) 
  b.append(i[0]) 





t = time.localtime(time.time())
t = t[3]*3600+t[4]*60+t[5]

k = time.localtime(time.time())
if k[3]*3600+k[4]*60+k[5] - t > 21*60:
	t = k
	fl = True



root = tk.Tk()
root.title('Space weather')
#root.geometry("300x300")
root.resizable(width=False, height=False)
root.configure(bg='#111441')
menu = tk.Menu(root, bg="#111111")

root.geometry('320x170-0-650')




#внутренности
photo1 = PhotoImage(file="T1.png")
w = Label(root, image=photo1,bg='#111441' )
w.grid(row=1, column=1)


photo2 = PhotoImage(file="S1.png")
w2 = Label(root, image=photo2,bg='#111441' )
w2.grid(row=1, column=2)


photo3 = PhotoImage(file="D.png")
w3 = Label(root, image=photo3,bg='#111441')
w3.grid(row=1, column=3)


#температура
lbl_1 = Label(root, text="T °K",font='Courier 18', fg='white',bg='#111441')
lbl_1.grid(row=2, column=1,padx=10, pady=0)

infoT = Label(root, text=i[2], bg='#111441', fg='white',font=40)
infoT.grid(row=3, column=1,padx=20, pady=0)

#скорость 
lbl_2 = Label(root, text="S km/c",font='Courier 18', fg='white',bg='#111441')
lbl_2.grid(row=2, column=2,padx=10, pady=0)



infoS = Label(root, text=i[0], bg='#111441',fg='white', font=40)
infoS.grid(row=3, column=2,padx=20, pady=0)
#концентрация
lbl_3 = Label(root, text="D 1/cm³",font='Courier 18', fg='white',bg='#111441')
lbl_3.grid(row=2, column=3,padx=10, pady=0)

infoD = Label(root, text=i[1], bg='#111441',fg='white', font=40)
infoD.grid(row=3, column=3,padx=20, pady=0)

lbl_3.grid()
lbl_2.grid()
lbl_1.grid()





infoS.grid()
infoT.grid()
infoD.grid()
#запуск вікна
root.mainloop()