	# python modules
# what is a module ? 
'''
consider a module to be the same as a code library . 
a file containing a set of  fucntino you want ot include in you application . 


# create a module 

# to create a module just save the code you want in a file with the file extension . py: 
 
# exmaple 
# save this code in a a file named mymodule.py 

'''



# use a module 

import mymodules

a = mymodules.person1["age"]
print(a)


# import frm module
def greet(name):
	print(" helloi, " + name ) 

person1 ={ 
		'name' : 'john', 
		'age'  : 23, 
		'country' : "norway"
}
# Example - Import only the person1 dictionary from the module:

from mymodules import person1
print(person1["age"])


# 