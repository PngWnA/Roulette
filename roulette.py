import random
import time

pair = []
winner = []
tmp = []
result = []
tickets = 0
currSum = 0
peoples = 0
rounds = 0

print("[*]      ---Usage---     [*]")
print("1. put people and number")
print("2. put 'end'")
print("3. put # of ticket")
print("----------------------------")


while True:
	if "end" in raw:
		break

	try:
		first, second = raw.split(" ")
		if first in tmp:
			continue
	except:
		print("[-] Invalid input")
	

	pair.append([first, int(second)])
	tmp.append(first)

peoples = len(pair)
print ("[+] Result", "\n", pair)

while True:
	raw = input("(# of ticket)> ")
	try:
		ticket = int(raw)
		break

	except:
		print("[-] Invalid input")	

print ("[+] # of ticket -> ", ticket)
tickets = ticket

while True:
	currSum = 0
	rounds += 1
	print("========== [*] Round ", rounds, "==========")
	tmp = pair
	winner = []
	result = []
	while True:
		index = random.randrange(0, peoples)
		first, second = tmp[index][0], tmp[index][1]
		if first not in winner:
			winner.append(first)
			result.append([first, second])
		else:
			continue
		print("[+] Winner =>", first, "(", second, ")")
		currSum += second
		print("[*] Current tickets = ", currSum)
		time.sleep(0.1)
		if currSum > tickets:
			print ("[-] Sum > # of tickets. Restarting...\n\n")
			time.sleep(2)
			break
		elif currSum == tickets:
			print ("[+] Sum = # of tickets. End\n\n")
			print ("========== Winner ==========")
			for i in result:
				print (i[0], i[1])
			exit()
