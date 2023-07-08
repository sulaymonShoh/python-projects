from random import *

def son_top(x=10):
	taxminlar=0
	print(f"\nMen 1dan {x}gacha bir son o'yladim. Topa olasizmi?")
	tasodifiy_son=randint(1,x)

	while True:
		taxminlar+=1
		taxmin = int(input())
		if taxmin>tasodifiy_son:
			print("Men o'ylagan son bundan kichikroq. Qayta urinib ko'ring.")
		elif taxmin<tasodifiy_son:
			print("Men o'ylagan son bundan kattaroq. Qayta urinib ko'ring.")
		else: break

	print(f"Tabriklayman! {taxminlar} taxminda topdingiz!\n")
	return taxminlar

def son_top_pc(x=10):
	input(f"1 dan {x}gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
	quyi=1
	yuqori=x
	taxminlar_pc=0
	while True:
		taxminlar_pc+=1
		if quyi != yuqori:
			taxmin = randint(quyi, yuqori)
		else: taxmin=quyi
		javob = input(f"Siz {taxmin} sonini o'ylagansiz: to'g'ri - (t), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())

		if javob == "-":
			yuqori = taxmin-1
		elif javob == "+":
			quyi = taxmin+1
		else: break
	print(f"Topdim! Men {taxminlar_pc} taxmin bilan topdim.\n")
	return taxminlar_pc

def play(x=10):
	yana = True
	while yana:
		taxminlar_user=son_top(x)
		taxminlar_pc=son_top_pc(x)

		if taxminlar_user>taxminlar_pc: print("Men yutdim!")
		elif taxminlar_user<taxminlar_pc: print("Siz yutdingiz!")
		else: print("Durrang!")
		yana =int(input("\nYana o'ynaysizmi? (ha - 1, yo'q - 0)"))
play()