from pystray import MenuItem as item
from pystray import Icon
import tkinter as tk
from PIL import Image, ImageDraw, ImageFilter, features
import threading
import time
import random
import math
import requests
import ctypes

r = requests.get('https://services.swpc.noaa.gov/text/rtsw/data/plasma-1-day.i.json').text.replace('"', '').replace('[', '').replace(']', '').split('\n')[::]

b = []
p = []
sta = True
for i in range(22):
	b.append(r[i])
r = b
del b
for i in r[1:]:
	i = i[len('2022-10-01 15:16:00,'):-7]
	i = i.split(',')
	i = list(map(float, i))
	i = list(map(int, i))
	p.append(i)

for i in range(len(p)):
	if p[i][1] == 0:
		p[i] = int(p[i][2]/p[i][0]*3)
	else:
		p[i] = int(p[i][2]/p[i][1]/p[i][0]*3)

t = time.localtime(time.time())
t = t[3]*3600+t[4]*60+t[5]

window = tk.Tk()
window.withdraw()

def quit_window(icon, item):
    icon.stop()
    window.destroy()

def show_window(icon, item):
    icon.stop()
    window.after(0,window.deiconify)

image = Image.open("image.ico")
menu = (item('Show', show_window), item('Quit', quit_window))
icon = Icon("name", image, "ЗАГЛУШКА", menu)

def withdraw_window():
    icon.run()


a = threading.Thread(target=withdraw_window, args=())
a.start()

minv = 200

fl = True
while True:
	k = time.localtime(time.time())
	if k[3]*3600+k[4]*60+k[5] - t > 21*60 or sta:
		t = k
		r = requests.get('https://services.swpc.noaa.gov/text/rtsw/data/plasma-1-day.i.json').text.replace('"', '').replace('[', '').replace(']', '').split('\n')[::]
		b = []
		p = []
		for i in range(22):
			b.append(r[i])
		r = b
		del b
		for i in r[1:]:
			i = i[len('2022-10-01 15:16:00,'):-7]
			i = i.split(',')
			i = list(map(float, i))
			i = list(map(int, i))
			p.append(i)
		for i in range(len(p)):
			if p[i][1] == 0:
				p[i] = int(p[i][2]/p[i][0]*3)
			else:
				p[i] = int(p[i][2]/p[i][1]/p[i][0]*3)
		fl = True

	if fl:
		b = Image.new(mode="RGBA", size=(1920, 1080), color = (37, 35, 59, 255))
		dr = ImageDraw.Draw(b)
		for i in range(random.randrange(10, 40)):
			sx = random.randrange(10, 1910)
			sy = random.randrange(200, 1080)
			r = random.randrange(0, 5)
			dr.ellipse((sx, sy, sx +r, sy + r), fill = (255,255,255,255))
		p.reverse()
		tm = []
		for i in range(0,len(p[:10]),2):
			for j in range(193):
				j = j/192
				t1x = i*192 + 192*j
				t2x = (i+1)*192 + 192*j
				bx = t1x + (t2x-t1x)*j
				t1y = p[i] + (p[i+1]-p[i])*j
				t2y = p[i+1] + (p[i+2]-p[i+1])*j
				by = t1y + (t2y-t1y)*j
				t3y = p[i+10] + (p[i+11]-p[i+10])*j
				t4y = p[i+11] + (p[i+12]-p[i+11])*j
				b2y = t3y + (t4y-t3y)*j
				if by > b2y:
					o = by - b2y
					dr.rectangle([bx, b2y, bx+1, b2y+o/3], fill=(0, 33, 138, 255))
					dr.rectangle([bx, b2y+o/3, bx+1, b2y+o*2/3], fill=(11, 168, 146, 255))
					dr.rectangle([bx, b2y+o*2/3, bx+1, b2y+o], fill=(14, 240, 254, 255))
				if b2y > by:
					o = b2y - by
					dr.rectangle([bx, by, bx+1, by+o/3], fill=(0, 33, 138, 255))
					dr.rectangle([bx, by+o/3, bx+1, by+o*2/3], fill=(11, 168, 146, 255))
					dr.rectangle([bx, by+o*2/3, bx+1, by+o], fill=(14, 240, 254, 255))
		b = b.transpose(Image.Transpose.ROTATE_180)
		b = b.filter(ImageFilter.BoxBlur(1))
		b.save('1.png')
		im2 = Image.open("forest.png")
		b.paste(im2, mask = im2)
		del im2
		b.save('1.png')
		ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:\Users\termi\Desktop\1.png', 0)
		fl = False
		time.sleep(60*21)
icon.stop()
exit()