


file = open('bd.txt', 'r')
for f in file:
	string = f
	num = list(map(int, string.split(';')[0].split()))
	rez = list(map(int, string.split(';')[1].split()))
	sum_str = sum(num)
	col = len(num)
	print(string.strip('\n'), end='\t')
	if sum_str // col == rez[0] and sum_str % col == rez[1]:
		print('True')
	else:
		print('False')

file.close()

