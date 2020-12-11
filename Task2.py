

def brilliant(number):
	if number > 0 and number % 2:
		center = (number // 2) + 1
		i = 1
		for col in range(1, number, 2):
			print(' ' * (center - i - 1) , '*' * col)
			i += 1
		print('*' * number)
		for col in range(number, 1, -2):
			print(' ' * (center - i) , '*' * (col - 2))
			i -= 1


brilliant(15)





