import os.path
import ipaddress
print("Hello and welcome to Networking Project 3")
tableInputFile = input("First please enter the file location for your table input file:\n")
if os.path.isfile(tableInputFile):
	f = open(tableInputFile)
	line = f.readline()
	ipNetwork = []
	networkCost = []
	asNum = []
	while line:
		variables = line.split()
		asNum.append(variables[0])
		ipNetwork.append(ipaddress.ip_network(variables[1]))
		networkCost.append(int(variables[2]))
		line = f.readline()
	
	addrInput = input("Table input file has been accepted, please enter your address input file:\n")
	if os.path.isfile(addrInput):
		f = open(addrInput)
		line = f.readline().strip()
		cost = 6
		asn = "X"
		while line:
			line = ipaddress.ip_address(line)
			for x in range(0,len(ipNetwork)):
				if(line in ipNetwork[x]):
					if(networkCost[x]<cost):
						asn = asNum[x]
						cost = networkCost[x]
			print(str(line) + " " + asn)
			asn = "X"
			cost = 6
			line = f.readline().strip()
	else:
		print("The input address file that you have enter is not valid, check your records then run the program again")
			
else:
	print("The table input filepath you entered does not exist, please check you records then run the program again")


