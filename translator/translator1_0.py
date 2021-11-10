"""
OLD METHOD - 52 lines - this can translate numbers that smaller than 10,000
"""

birliklar = ['bir', 'ikki', 'uch', 'to\'rt', 'besh', 'olti', 'yetti', 'sakkiz', 'to\'qqiz']
onliklar = ['o\'n', 'yigirma', 'o\'ttiz', 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', 'to\'qson']
output = ''

def lower_10(number):
    return birliklar[number-1]

def lower_100(number):
    if str(number).endswith('0'): return f'{onliklar[int(list_number[0])-1]}'
    else: return f'{onliklar[int(list_number[0])-1]} {birliklar[int(list_number[1])-1]}'

def lower_1000(number):
    str_number = str(number)
    
    if str_number[1] == '0' and str_number.endswith('0'): return f'{birliklar[int(list_number[0])-1]} yuz'
    elif str_number.endswith('0'): return f'{birliklar[int(list_number[0])-1]} yuz {onliklar[int(list_number[1])-1]}'
    elif str_number[1] == '0': return f'{birliklar[int(list_number[0])-1]} yuz {birliklar[int(list_number[2])-1]}'
    else: return f'{birliklar[int(list_number[0])-1]} yuz {onliklar[int(list_number[1])-1]} {birliklar[int(list_number[2])-1]}'

def lower_10000(number):
    str_number = str(number)

    if str_number[-1]=='0' and str_number[-2]=='0' and str_number[-3]=='0': return f'{birliklar[int(list_number[0])-1]} ming'
    elif str_number[-1]=='0' and str_number[-2]=='0': return f'{birliklar[int(list_number[0])-1]} ming {birliklar[int(list_number[1])-1]} yuz'
    elif str_number[-2]=='0' and str_number[-3]=='0': return f'{birliklar[int(list_number[0])-1]} ming {birliklar[int(list_number[3])-1]}'
    elif str_number[-1]=='0' and str_number[-3]=='0': return f'{birliklar[int(list_number[0])-1]} ming {onliklar[int(list_number[2])-1]}'
    elif str_number[-1]=='0': return f'{birliklar[int(list_number[0])-1]} ming {birliklar[int(list_number[1])-1]} yuz {onliklar[int(list_number[2])-1]}'
    elif str_number[-2]=='0': return f'{birliklar[int(list_number[0])-1]} ming {birliklar[int(list_number[1])-1]} yuz {birliklar[int(list_number[3])-1]}'
    elif str_number[-3]=='0': return f'{birliklar[int(list_number[0])-1]} ming {onliklar[int(list_number[2])-1]} {birliklar[int(list_number[3])-1]}'
    else: return f'{birliklar[int(list_number[0])-1]} ming {birliklar[int(list_number[1])-1]} yuz {onliklar[int(list_number[2])-1]} {birliklar[int(list_number[3])-1]}'

def translate(number):
    if number.isdigit():
        number = int(number)

        if number == 0: output = 'nol'
        elif number <= 9: output = lower_10(number)
        elif number <= 99: output = lower_100(number)
        elif number <= 999: output = lower_1000(number)
        elif number <= 9999: output = lower_10000(number)
        elif number > 9999: output = 'Dastur 10000 dan kichik sonlar uchun mo\'ljallangan'

    else: output = 'Faqat son kiriting!'

    return output

while True:
    input_number = input('\nTarjima qilish uchun son yozing:  ')
    if bool(input_number):
        list_number = list(str(input_number))
        print(translate(input_number).capitalize())
    else: break