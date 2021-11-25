from random import sample
COUNT_OF_NUMBERS = 1
NUMBERS = []

entering_data = input(' - Son kiriting: \n - ')
digits = input(' - Necha xonali sonlar generatsiya qilamiz?\n - ')
repetition = input(' - Raqamlar takrorlansinmi?\n\t1 - Ha\n\t0 - Yo\'q\n - ')

def logicalise(input):
	if input == 0 or input == '0' or input == '' or input == 'yo\'q':
		return False
	else: return True

def integration(input):
	if input.isdigit():
		return int(input)
	else: print('Faqat sonlar kiriting')

def from_list_to_int(arg):
	int_data = ''
	for x in arg:
		int_data+=str(x)
	return int(int_data)

entering_data = integration(entering_data)
digits = integration(digits)
repetition = logicalise(repetition)

def count(base, digit, repeat):
	global COUNT_OF_NUMBERS
	if repeat: COUNT_OF_NUMBERS = len(str(base))**digit
	else:
		INITIAL_COUNT = len(str(base))
		for n in range(digit):
			COUNT_OF_NUMBERS *= INITIAL_COUNT-n

	print(f' - {COUNT_OF_NUMBERS} ta son generatsiya qilish mumkin.')


def generate(base, digit):
	global NUMBERS
	LIST_BASE = [int(i) for i in list(str(base))]
	while True:
		n, addition = sample(LIST_BASE, digit), ''
		for i in n:
			addition += str(i)
		addition = int(addition)

		if len(NUMBERS)<COUNT_OF_NUMBERS:
			if not addition in NUMBERS:
				NUMBERS.append(addition)
		else: break

	NUMBERS.sort()

def show_numbers(list):
	print(' - ', end='')
	for number in list:
		if list.index(number)==len(list)-1:
			print(number, end='.')
		else: print(number, end=', ')

count(entering_data, digits, repetition)
generate(entering_data, digits)
want_to_see = input(' - Bu sonlarni ko\'rishni xohlaysizmi?\n\t1 - Ha\n\t0 - Yo\'q\n - ')
if want_to_see == '1':
	show_numbers(NUMBERS)

print('\n - Dastur yakunlandi :)')