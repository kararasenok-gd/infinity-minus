num = int(input('Введите число: '))
num2 = int(input('Введите второе число: '))
ms = 0
ms_total = 0
ms_up = 0.44
s = 0
m = 0
h = 0

ex_num_now = 0

file = open(f'{num}.txt', 'a')
while num > 0:
	ex_num_now += 1
	num_last = num
	num = num - num2
	ms += ms_up
	ms_total += ms_up
	if ms/1000 > 1:
		s += 1
		ms = 0
	if s/59 > 1:
		m += 1
		s = 0
		ms = 0
	if m/59 > 1:
		h += 1
		m = 0
		s = 0
		ms = 0
	print(f'{ex_num_now} | {num_last} - {num2} = {num} | {h}:{m}:{s}')
	file.write(f'{ex_num_now} | {num_last} - {num2} = {num} | {h}:{m}:{s}\n')

file.write(f'Всего действий: {ex_num_now}\nДоведено до нуля за {h}:{m}:{s}\n---------------------------------------------------------------------------------------------------------\n')
file.close()
input(f'Получилось: {ex_num_now} действий | Было доведено до нуля за {h}:{m}:{s} (или за {ms_total} милисекунды) | Нажми Enter для закрытия')
