#multiple input values

# x, y,z, a = input("Please enter the number? :").split()
# print(x)
# print(y)
# print(z)
# print(a)

#multiple condition to fulfill

# subs = 2400
# likes = 200
# comment = 56
#
# conditions = [
#     subs > 150,
#     likes > 150,
#     comment > 50
# ]
#
# if all(conditions):
#     print("Print if all is true")
#
# if any(conditions)
#     print("Print if one is true")
#

#Swapping values with each other

# subs = 2400
# likes = 200
# print(subs, likes)
#
# subs, likes = likes, subs
# print(subs, likes)

#To remove duplicates

# a = [1,32424,54566,645,2,34,45,65,1,1,1,12,34,5,67,8,76,5,64,1,10,101,1,11,1,1,11,223232,2,2,22,]
#
# b = list(set(a)) #set is unique values
# print(b)
# no_repeated_most = max(set(a), key=a.count) #to find number which is there most in the list
# print(no_repeated_most)

#Odd number squares (List comprehension)

# odd_squares = [i**2 for i in range(12) if i%2==1]
# print(odd_squares)

#Reverse String
name = 'Kim Kardashian'[::-1]
print(name)