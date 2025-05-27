# python scope

# a vaiable is only availe form iside th regiion tit is created ,this is called scope 
# local scope


# variabl created insidea  fucntion belog ot th local of that funcitn and coan only be used inside that function 



# exmaple  a variable created insdie a funciton si avavailabe isdie that funciton  

 


def myf():
	a = 1909
	def mysf(): 
		print(a)
	mysf()
myf()


# global scope

'''
* variable - main body - global variable
'''

# example 

a  = 23
def astra():
	print(a)
astra()
print(a)



# nonlocal keyword

'''
* nonlocal - for keywords with variable inside nested function 
* nonlocla - makes available to outer functino 
 
'''
def shastra():
	name ="raam"
	def brahmastra():
		nonlocal name
		name = 'indra'
	brahmastra()
	return name

print(shastra())


