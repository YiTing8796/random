import random

r = random.randint(1, 100)
while True :
	n = input('請輸入數字：')
	n = int(n)
	if r == n :
		print('終於猜對了')
		break
	elif r > n :
		print('比答案小')
	elif r < n :
		print('比答案大')
