


# python string formatting

# f sting ws introdud in python 3.6, and is not the preferred way of formatting string . 
# before pytonh 3.6 we had to use the format() method.



# f-string ass lows to forrmat selected parts of a string 
# to spectiy a sting as an ffs tin g, simpley ouput an df fin sfornt the string liternal like thats

joseweden = "and he definitely still lived with his mom"

print(joseweden)

# placeholders and modifiers

# to format valeus in a na f-stirfn , add lplaceholders {} , a placeholder 
# can contain vairbale,s operators,function and modifiers to format the values, 



binary_code = 10011
syntax = f"the binary_code is {binary_code}"
print(syntax)


# a  place can also includ e amodifer to format the value \
# a modifier is incldued by adding a colon: foloowed by a legal formatiting type
# .2f which means fixed point number with 2 decimals: 

# EXAMPLE 
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


binary_code = 1010101010
syntax = f"the binary_code id {54:.2f}"
print(syntax)


 
# EXAMPLE = expensive if the power is over 490 , otherwise return " cheap":

marks = int(input(" how much marks did you get? "))
result = f"the marks are {'low' if marks> 40 else 'good'}"
print(result)


sports  = ' football'
likes  = f" i love {sports.upper()}"
print(likes)


# EXAMPLE = create your own afunctions an d can use them al so 

x = int(input(' what is the tempoerature in celcius'))
def celciustokelvin(x): 
	return x + 273

temp = f" the temperature after coverting from celcius to kelvin is {celciustokelvin(x)} kelvin"
print(temp)


# MORE MODIFIERS
# comma  - thousand separator


mars = 2342
distance  = f" the mars is {mars:,} km away from the earth "
print(distance)

# string format



#  example 
# add oa plceholder where you want to  displat the price : 


price =23
txt = "the price is {} dollars "
print(txt.format(price))


# ex

txt = "The price is {:.2f} dollars"


print(txt.format(price, itemno, count))


#  ex

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#  index numbers; 

