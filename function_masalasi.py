from math import sin, sqrt

interval = []
results = []

beginning = int(input('Enter beginning of interval: '))
ending = int(input('Enter ending of interval: '))
step = float(input('Enter step: '))

i=beginning
while i<=ending:
	interval.append(round(i, 1))
	i+=step

for x in interval:
	if x <= 0:
		y = sin(pow(x, 2))
		results.append(f'y({x}) = {y}')
	else:
		y = sqrt(x)
		results.append(f'y({x}) = {y}')

with open('FUNCTION.TXT', 'w') as output_file:
	for item in results:
		output_file.write(f'{item}\n')

print('\nSuccessful! You can see result in \'FUNCTIONS.txt\'')