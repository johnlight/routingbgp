import pprint
def parseTableFile(inputFile):
	table = {}
	tableFile = open(inputFile)
	for line in tableFile:
		lineList = line.split()
		asNum,subnet,cost = lineList[0],lineList[1],lineList[2]
		##print(asNum + "\t"+subnet+"\t"+cost)
		if not asNum in table:
			table[asNum] = [{subnet:cost}]
		else:
			table[asNum].append({subnet:cost})
	tableFile.close()
	return table

def parseAddressFile(addressFile):
	addressList = []
	addressFile = open(addressFile)
	for line in addressFile:
		address = line.split()
		addressList.append(address[0])
	return addressList

def main():
	    print("************************************************************")
	    print("Welcome to the COSC3344 Networks Project")
	    ##inputFile = input("Please enter the input file.\n")
	    ##addressFile = input("Please enter the address file.\n")
	    ##outputFile = input("Please enter the output file. \n")
	    inputFile = "inputfiles/tableinputfile1FIX.txt"
	    outputFile = "inputfiles/Answers.txt"
	    addressFile = "inputfiles/addressinputfile1FIX.txt"
	    table=parseTableFile(inputFile)
	    address=parseAddressFile(addressFile)
	    pp = pprint.PrettyPrinter(indent=4)
	    pp.pprint(table)
	    pp.pprint(address)
		##route(table,address,outputFile)

main()