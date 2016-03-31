import csv
import sys
from comparer import Comparer

def main():
	file1Name = sys.argv[1]
	file2Name = sys.argv[2]
	comparisonToRun = sys.argv[3]
	
	data1 = []
	data2 = []
	
	with open(file1Name, 'rb') as csvfile:
		fileReader = csv.reader(csvfile)
		for row in fileReader:
			#print row
			data1.append(row)

	with open(file2Name, 'rb') as csvfile:
		fileReader = csv.reader(csvfile)
		for row in fileReader:
			data2.append(row)

	result = Comparer(data1, data2, comparisonToRun)

	if comparisonToRun == "totalDescription":
		result = Comparer(data1, data2, comparisonToRun)
		result.runTotalDescription()
	elif comparisonToRun == "BSL":
		result = Comparer(data1, data2, comparisonToRun)
		result.runBSL()
	elif comparisonToRun == "blockingTokens":
		result.runBlockingTokens()

	print result.evaluate(result, len(data1), len(data2))

main()
