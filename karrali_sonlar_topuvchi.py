start = int(input('Boshlanish nuqtasini kiriting: '))
stop = int(input('Tugash nuqtasini kiriting: '))
step = int(input('Qadamni kiriting: '))

def first_n():
	for i in range(start, stop):
		if i%step == 0:
			return i
			break

def last_n():
	for i in range(stop-1, start, -1):
		if i%step == 0:
			return i
			break

a1 = first_n()
an = last_n()
n = int((an-start)/step+1)
s = int((a1+an)/2*n)

list = ''
for i in range(a1, an+1, step):
	list+=str(i)+', '

print(f'{start} dan {stop} gacha {step} ga karrali {n} ta son bo\'lib, ular {list}.\nUlarning yig\'indisi {s} ga teng')