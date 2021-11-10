from tkinter import *

window = Tk()
window.title('Translator2.1')
window.config(bg = '#f0f0f0')
window.geometry('900x400')
FONT = 'Consolas'

heading = Label(window, text="Butun son kiriting:", pady=5, font=(FONT, 15)).grid(row=0, column=0)

def translate(number):
	on = ['', 'o\'n', 'yigirma', 'o\'ttiz', 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', 'to\'qson']
	bir = ['', 'bir', 'ikki', 'uch', 'to\'rt', 'besh', 'olti', 'yetti', 'sakkiz', 'to\'qqiz']
	list_number = list(str(number))

	if number.isdigit():
		number = int(number)
		LIMIT = 12

		if len(list_number) > 3 and list_number[-3] == '0': yuz = ''
		else: yuz = 'yuz'

		def error():
			return f'Dastur hozircha faqat {LIMIT} xonali sonlar uchun mo\'ljallangan'

		if len(list_number) > LIMIT: error()
		elif number == 0: return 'nol'
		elif number <= 9: return f'{bir[number]}'
		elif number <= 99: return f'{on[int(list_number[0])]} {bir[int(list_number[1])]}'
		elif number <= 999: return f'{bir[int(list_number[0])]} yuz {on[int(list_number[1])]} {bir[int(list_number[2])]}'
		elif number <= 9999: return f'{bir[int(list_number[0])]} ming {bir[int(list_number[1])]} {yuz} {on[int(list_number[2])]} {bir[int(list_number[3])]}'
		elif number <= 99999: return f'{on[int(list_number[0])]} {bir[int(list_number[1])]} ming {bir[int(list_number[2])]} {yuz} {on[int(list_number[3])]} {bir[int(list_number[4])]}'
		elif number <= 999999: return f'{bir[int(list_number[0])]} yuz {on[int(list_number[1])]} {bir[int(list_number[2])]} ming {bir[int(list_number[3])]} {yuz} {on[int(list_number[4])]} {bir[int(list_number[5])]}'
		elif number <= 9999999: return f'{bir[int(list_number[0])]} million {bir[int(list_number[1])]} yuz {on[int(list_number[2])]} {bir[int(list_number[3])]} ming {bir[int(list_number[4])]} {yuz} {on[int(list_number[5])]} {bir[int(list_number[6])]}'
		elif number <= 99999999: return f'{on[int(list_number[0])]} {bir[int(list_number[1])]} million {bir[int(list_number[2])]} yuz {on[int(list_number[3])]} {bir[int(list_number[4])]} ming {bir[int(list_number[5])]} {yuz} {on[int(list_number[6])]} {bir[int(list_number[7])]}'
		elif number <= 999999999: return f'{bir[int(list_number[0])]} yuz {on[int(list_number[1])]} {bir[int(list_number[2])]} million {bir[int(list_number[3])]} yuz {on[int(list_number[4])]} {bir[int(list_number[5])]} ming {bir[int(list_number[6])]} {yuz} {on[int(list_number[7])]} {bir[int(list_number[8])]}'
		elif number <= 9999999999: return f'{bir[int(list_number[0])]} milliard {bir[int(list_number[1])]} yuz {on[int(list_number[2])]} {bir[int(list_number[3])]} million {bir[int(list_number[4])]} yuz {on[int(list_number[5])]} {bir[int(list_number[6])]} ming {bir[int(list_number[7])]} {yuz} {on[int(list_number[8])]} {bir[int(list_number[9])]}'
		elif number <= 99999999999: return f'{on[int(list_number[0])]} {bir[int(list_number[1])]} milliard {bir[int(list_number[2])]} yuz {on[int(list_number[3])]} {bir[int(list_number[4])]} million {bir[int(list_number[5])]} yuz {on[int(list_number[6])]} {bir[int(list_number[7])]} ming {bir[int(list_number[8])]} {yuz} {on[int(list_number[9])]} {bir[int(list_number[10])]}'
		elif number <= 999999999999: return f'{bir[int(list_number[0])]} yuz {on[int(list_number[1])]} {bir[int(list_number[2])]} milliard {bir[int(list_number[3])]} yuz {on[int(list_number[4])]} {bir[int(list_number[5])]} million {bir[int(list_number[6])]} yuz {on[int(list_number[7])]} {bir[int(list_number[8])]} ming {bir[int(list_number[9])]} {yuz} {on[int(list_number[10])]} {bir[int(list_number[11])]}'

	else: return 'Faqat sonlarni kiriting!!!'

input_text = Entry(window, width=20, font=(FONT, 15), justify = CENTER)
input_text.grid(row=0, column=1)

result = Label(window, bg='yellow', height=1, font=(FONT, 15))

def provide_number():
    result.configure(text=None)
    data=translate(input_text.get()).capitalize()
    result.configure(text=data)
    result.grid(row=1, column=0, columnspan=3)

submit = Button(window,background = '#ddd',foreground = '#000',text = 'Yuborish',font = (FONT, 12),padx=10,pady=0,command = provide_number).grid(row=0, column=2)

window.grid_columnconfigure(0, minsize=300)
window.grid_columnconfigure(1, minsize=300)
window.grid_columnconfigure(2, minsize=300)
window.grid_rowconfigure(0, minsize=80)
window.grid_rowconfigure(1, minsize=80)

window.mainloop()