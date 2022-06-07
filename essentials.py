print("hello word", 4.5)
# # variables
hello = "tim"
word = "word"
word = hellohello = "no"
print(hello, word)
# convencion variable
hello_word = "hola"
# # input
name = input('Name: ')
print(name)
# # operaciones aritmeticas 
# # convert to integer
x = 9 
y = 3
int(x/y)

# # exponent

x**y
# # floor division

x//y

#mod

x%3

#modular  operation

(x%y) * 2

num = input ("Number: ")
print(int(num)-5)



#type func


hello = "hello"
print(type(hello))

#string methods


hello = hello.upper()
print(hello)


hello = hello.lower()

hello.capitalize()
#counts the amount of coincidences found
print(hello.lower().count("ll"))



#conditions
x = 7
y = 8
z = 0
result1 = x == y
result2 = y > x
result3 = z < x + 2

result4 = result1 or result2

x = "tim"

if x == "tim":
    print("tim is great")
elif x == "bob":
    print("bob is great")
else:
    print("You are not tim")


#list are mutable objects
x = [4, True, "hi"]
x.append("hello")
print(x)
x.extend([1,2,3,4,5,6,7])

print(x.pop(0))


print(x[1])

#tuples are immutable

y = (0,0,2,2)


#loops

for i in range(10):
   print("hello")
i = 0
while i < 10:
    print("hello1")
    i+=1  
i = 0
while True:
    print("hello2 ", i)
    i += 1
    if i == 10:
        break   
#slice operator
x = [0,1,2,3,4,5,6,7,8]    
sliced = x[0:4:2]
print(sliced)
#revert list with slice [beginning:end:step]
sliced = x[::-1]
print(sliced)
#with strings 
s = "hello world"
sliced = s[::-1]    
print(sliced)
#sets
x = set()
s = {4,32,2,2}

print(s)

# print(2 in s)

# #dictionaries
# x = {'key':4}
# x['key2 '] = "seconfd value"
# print("x: ", x)
# # functions
# def func(x,y):
#     print("Run",x,y)
#     return x*y
# print(func(5,6))  
# #several elements returned in the functio will be returned in a tuple
# def func1(x,y):
#     print("Run",x,y)
#     return x*y, x/y
# print(func1(5,6)) 
# # destructure a tuple
# r1, r2 = func1(5,6)
# print(r1, r2) 
# # unpack operator separate a list or tuple into individual elements
# def func3(*args, **kwargs):
#     print(*args)
# x = [1,23,2345,2727]
# print(*x)
# # handling exeptions
# try: 
#     x= 7/0
# except Exception as e:
#     print(e)
# finally:
#     print("finally")
# #lambda is a one line anonimous function 
# x = lambda x, y:x+y
# print(x(2, 5))
# #map applies the lambda function to each element of the list 
# x = [1,2,3,4,5,3,3,21,2,21,2,313,1,23,142,4]

# mp = map(lambda i: i+2,x)
# print(list(mp))


# #filter returns true or false base on the value of the item
# filtr = filter(lambda i: i % 2 == 0, x)
# print(list(filtr))



# #f strings

# cheers = f'hello {1+2}'
# print(cheers);
