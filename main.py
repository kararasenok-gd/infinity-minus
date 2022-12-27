num = int(input('Введите число: '))
num2 = int(input('Введите второе число: '))

ex_num_now = 0

file = open(f'{num}.txt', 'a')
while num > 0:
	ex_num_now = ex_num_now + 1
	num_last = num
	num = num - num2
	print(f'{ex_num_now} | {num_last} - {num2} = {num}')
	file.write(f'{ex_num_now} | {num_last} - {num2} = {num}\n')

file.close()
input(f'Получилось: {ex_num_now} действий | Нажми Enter для закрытия')