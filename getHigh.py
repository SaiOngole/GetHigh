import random
print "Smoke it bitches"
while(1):
	inp = raw_input()
	if(inp != 'x' or inp =="X"):
		ran = random.random()
		if(ran>=0 and ran<0.2):
			print "Draw two bob!"
		elif(ran>=0.2 and ran<0.4):
			print "Draw four of them"
		elif(ran>=0.4 and ran<0.6):
			print "Not this time my friend!"
		elif(ran>=0.6 and ran<0.8):
			print "Reverse it"
		elif(ran>=0.8 and ran<=1):
			print "Smoke till you choke!"

	
