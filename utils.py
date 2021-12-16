def printList(label: str, list: list):
	if label:
		print(label)
	for row in list:
		print(row)

def calculateMean(dataset: list) -> list:
	means = [0 for i in range(len(dataset[0]))]
	for i in range(len(means)):
		columnValue = [row[i] for row in dataset]
		means[i] = sum(columnValue) / float(len(dataset))
	return means