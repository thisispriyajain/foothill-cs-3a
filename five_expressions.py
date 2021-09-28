# * Class: CS3A
# * Description: The objective of this assignment is to calculate 5 values based on our student ID and the number of letters in our last name.
# * Due date: Monday, June 6, 2020
# * Name: Priya Jain
# * File name: five_expressions.py

my_id = 20331247
num_let = 5

print('My family name is Jain')
print('My student ID is', my_id)
print('The number of characters in my first name is', num_let)

print('Expression 1:', my_id % 17)
print('Expression 2:', ((num_let + 17) % 11))
print('Expression 3:', float((my_id)/(num_let + 800)))
print('Expression 4:', 1+2+3+4+5)
print('Expression 5:', float(15000/(80 + ((my_id - 123456)/(num_let + 20)**2))))

#Code Output:
# My family name is Jain
# My student ID is 20331247
# The number of characters in my first name is 5
# Expression 1: 12
# Expression 2: 0
# Expression 3: 25256.207453416147
# Expression 4: 15
# Expression 5: 0.462784910753596