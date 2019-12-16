# #a
# x = 4
# y = 8
# if x > y:
#     print("BIG")
# elif x < y:
#     print("small")
#
# #B
# for x in range(5):
#     print("Loop range:",x)
#
# #C
# season = 3
# if season == 1:
#     print("Summer")
# elif season ==2:
#     print("Winter")
# elif season ==3:
#     print("Autumn")
# elif season == 4:
#     print("Spring")
#
# #D
# count = 1
# while count < 11:
#     print("count:", count)
#     count = count + 1
#
#     count: 1
#     count: 2
#     count: 3
#     count: 4
#     count: 5
#     count: 6
#     count: 7
#     count: 8
#     count: 9
#     count: 10
# #E
# age = 37
# letter = "F"
# currency = 3.49
# flew = True
# apartment_number = 20
# print("My Age:",age)
# print("First letter of your last name:",letter)
# print("$:",currency)
# print("Did you flew abroad:",flew)
# print("Your apartment number:",apartment_number)
# print("currency+age:",currency+age)
#
# #D
# number = input("Please Enter your phone number: ")
# print("Phone number is:", number)

# #G
# def printHello():
#     print("hello")
#
# def calculate():
#     print(5+3.2)
#
# if __name__ == '__main__':
#     printHello()
#     calculate()
#
# #H
# def print_name(name):
#     print(name)
#
# def div_number(num):
#     print(num/2)
#
# if __name__ == '__main__':
#     print_name("kostya")
#     div_number(4)
#
# #I
# def sum_num(x,y):
#     return x+y
#
# def space_string(strng_one, strng_two):
#     return strng_one + " " + strng_two
#
# if __name__ == '__main__':
#     print(sum_num(5,10))
#     print(space_string("My Name", "Kostya"))

#j
# import array as arr
# a = arr.array("i",[1,5,3])
# for temp_num in a:
#         print(temp_num)

#K
# for i in range(0, 5):
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("\r")

#L
# num = 7
# for i in range(num):
#     for j in range(num):
#         if (i == j) or ((num - j -1) == i):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')

#M
num = int(input("Input numbers: "))
x = num//10
print(x)
y = num%10
print(y)
total = x + y
print("The total sum is:","input",num,x,"+",y,"=",total)




