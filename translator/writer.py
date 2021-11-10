files = ['translator1_0', 'translator2_0']

for file in files:
	with open(f'{file}.txt', 'w') as new_file:
		with open(f'{file}.py') as source:
			data = source.read()
			new_file.write(data)
			print(f'"{file}.py" has been cloned as "{file}.txt" successfully!')

with open('README.txt', 'w') as readme:
	readme.write("Yuqoridagi .PY fayllarni ocha olmasangiz, .TXT fayllarni oching.")
	print('\n"README.txt" has been created')