import random

r = random.randint(1, 100)
count = 0
while True :
	count += 1 # count = count +1
	n = input('請輸入數字：')
	n = int(n)
	if r == n :
		print('終於猜對了')
		print('這是你猜的第', count, '次')
		break
	elif r > n :
		print('比答案小')
	elif r < n :
		print('比答案大')
    print('這是你猜的第', count, '次')
