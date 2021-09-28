houseIncome = int(input('What is the household income (-1 to quit)? '))
children = int(input('How many children? '))
while (houseIncome != -1):       
	financialHelp()
if (houseIncome = 1):
	break                 

def financialHelp():       
	if((houseIncome >= 30000 and houseIncome <= 40000) and children >= 3):          
		assistanceAmount = 1000 * children            
		print('The assistance amount is ', assistanceAmount)      
	if((houseIncome >= 20000 and houseIncome <= 30000) and children >= 2):        
		assistanceAmount = 1500 * children            
		print('The assistance amount is ', assistanceAmount)       
	if(houseIncome <= 20000):           
		assistanceAmount = 2000 * children           
		print('The assistance amount is ', assistanceAmount)