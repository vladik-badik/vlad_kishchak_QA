# str1 = "abc"        ## доказ того що стрігна змінюється
# print(id(str1))
# str1 += "def"
# print(id(str1))
################################


# str1 = "0123456789"
# str2 = str1 [:4] + "q" + str1[5:]
# print (str2)


##########
# str1 = "0123456789"
# print (str1[1:3])
# print (str1[-3:-1])
# print ("q" + str1[6:2]+ "q")
# print(str1[::2])
# print(str1[1::2])
# print(str1[1:6:2])
# print(str1[::-1])
# print(str1[-6:-1:2])
###########

# str1= "line1\nline2"
# print(str1)

############

# "my name is John"
# name= "john"
# age = 30
#
# print( "my name is " + name+ ". I am " + str(age) + "years old" )
#
# ##https://prnt.sc/A9UhK9DA5F5u
#
# print (f"My name is {name}.I am {age} years old") ##цим зручно користуватися
#
# print(f"value: {age * 2} {12345}") ## цим зручно користуватися
#
#
# Raw string
# path  = r"C:\temp\file.txt"
# print(path)
#
# path  = "C:\\temp\\file.txt"
# print(path)

# Bait string
str1= b'Qwerty'
print(str1)

str2= "qwerty"
print(str2.encode("ascii"))

str3= "Привіт"
print(str3.encode("UTF-8"))


