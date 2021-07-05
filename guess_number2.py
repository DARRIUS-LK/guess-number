import random
x = random.randint(1, 100)
while True:
	u = input('guess a number from 1-100: ')
	u = int(u)
	if u == x:
		print('bingo! you win')
		break
	if u > x:
		print('the number you guess is larger than the answer, try again')
	if u < x:
		print('the number you guess is smaller than the answer, try again')
