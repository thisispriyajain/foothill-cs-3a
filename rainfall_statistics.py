'''
* Program #5: Rainfall Statistics
* Programmer: Priya Jain
* Due: August 3, 2020
* CS 3A, Summer 2020
* Description: This assignment will calculate and display data based on monthly rainfall. 
'''

'''This function will find the total rainfall for the year.'''
def totalRainfall(rainList):
	total = 0
	for month in rainList:
		total += month
	return total

'''This function will find the average monthly rainfall.'''
def averageRainfall(rainList):
	total = 0
	for month in rainList:
		total += month
	average = total/len(rainList)
	return average

def main():

	rainfall = []

	JanRain = float(input("Enter the rainfall for January: "))
	rainfall.append(JanRain)

	FebRain = float(input("Enter the rainfall for February: "))
	rainfall.append(FebRain)

	MarRain = float(input("Enter the rainfall for March: "))
	rainfall.append(MarRain)

	AprRain = float(input("Enter the rainfall for April: "))
	rainfall.append(AprRain)

	MayRain = float(input("Enter the rainfall for May: "))
	rainfall.append(MayRain)

	JunRain = float(input("Enter the rainfall for June: "))
	rainfall.append(JunRain)

	JulRain = float(input("Enter the rainfall for July: "))
	rainfall.append(JulRain)

	AugRain = float(input("Enter the rainfall for August: "))
	rainfall.append(AugRain)

	SeptRain = float(input("Enter the rainfall for September: "))
	rainfall.append(SeptRain)

	OctRain = float(input("Enter the rainfall for October: "))
	rainfall.append(OctRain)

	NovRain = float(input("Enter the rainfall for November: "))
	rainfall.append(NovRain)

	DecRain = float(input("Enter the rainfall for December: "))
	rainfall.append(DecRain)

	totalRain = totalRainfall(rainfall)
	print('Total rainfall: ', totalRain)

	averageRain = averageRainfall(rainfall)
	print('Average rainfall: ', averageRain)

	print('Highest rainfall: ', max(rainfall))
	print('Lowest rainfall: ', min(rainfall))

main()


# Enter the rainfall for January: 10
# Enter the rainfall for February: 20
# Enter the rainfall for March: 30
# Enter the rainfall for April: 40
# Enter the rainfall for May: 50
# Enter the rainfall for June: 60
# Enter the rainfall for July: 70
# Enter the rainfall for August: 80
# Enter the rainfall for September: 90
# Enter the rainfall for October: 100
# Enter the rainfall for November: 110
# Enter the rainfall for December: 120
# Total rainfall:  780.0
# Average rainfall:  65.0
# Highest rainfall:  120.0
# Lowest rainfall:  10.0
