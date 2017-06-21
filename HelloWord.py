'''
print('Hello')
print("World")
'''
#Number and math
'''
# a = 5
print(a**2) # 5*5
print(7/4) #  =1.75
print(7//4) # =1

print("They are %s and %s" %("Nam", "Phan"))
print("""
Hello, how are you today ?
I'm fine. Thank you !
	""")
print("A\a\a\a")
'''

#Asking question
'''
a = int(input("Enter A: "))
b = int(input("Enter B: "))
print(a, " + ", b, " = ", a+b)
'''

#file
'''
from os.path import exists
input_file = open("ex15_sample.txt", "r+")
indata = input_file.read()

output_file_name = input("Enter output file ")
print(exists(output_file_name))

output_file = open(output_file_name, 'w')
output_file.write(indata)
input_file.close()
output_file.close()
'''

'''
#function and files
def print_all(file):
	print(file.read())

def rewind(file):
	file.seek(0)

def print_by_line(line_count, file_name):
	with open(file_name) as f:
		for line in f:
			line_count += 1
			print(line_count, " : " , line)

input_file = open("ex15_sample.txt", "r")
print_all(input_file)
rewind(input_file)
print_by_line(0, 'ex15_sample.txt')
'''

#Even more practice
def break_words(stuff):
	worlds = stuff.split(' ')
	return worlds

print(break_words("Hello I am there")[3])
