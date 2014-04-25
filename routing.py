def parseTableFile(inputFile):
	table = {}
	tableFile = open(inputFile)
	for line in tableFile:
		lineList = line.split()
		for lineAspect in lineList:
			print(lineAspect)


def main():
	    print("************************************************************")
	    print("Welcome to the COSC3344 Networks Project")
	    ##inputFile = input("Please enter the input file.\n")
	    ##addressFile = input("Please enter the address file.\n")
	    ##outputFile = input("Please enter the output file. \n")
	    inputFile = "inputfiles/tableinputfile1FIX.txt"
	    table = parseTableFile(inputFile)
		##address= parseAddressFile(addressFile)
		##route(table,address,outputFile)

main()