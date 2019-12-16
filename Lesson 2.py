# for x in range(10):
#     print(x)
#
# for x in range(3,5):
#     print("range(3,5)",x)
#
# for x in range(3,8,2):
#     print("range(3,8,2)",x)
#
# count = 0
# while count < 5:
#     print("count", count)
#     count += 1

# count = 0
# while count < 5:
#     print("count", count)
#     count += 1
#     if count == 3:
#       print("exit break", count)
#       break
#
# for x in range(10):
#      if x == 3:
#          print("continue", x)
#          continue
#
a = 10
def print_hello():
    print("call print")
    x = 3
    y = 5
    sum = 3 + 5
    print("sum",x+y)
    global a
    a = 7
    print(a)
    return(sum)

def print_hello_2(name,age):
    sum = name + age
    print(sum)
    return(sum)

if __name__ == '__main__':
    print("main")
    print_hello()
    x = print_hello()
    print_hello_2(4, 25)
    print("from def",x)
    print(print_hello_2(4, 25))

from datetime import datetime
totime = datetime.now()
print("PC Time:", totime)


import array as arr
a = arr.array("i",[1,5,3])
print(a[0])
a[0] = 5
a.append(3)
a.insert(3,25)
print(a[0])
print(a[3])
a.pop(0)
print(a[3])
print("len array",len(a))

for temp_num in a:
    if temp_num == 5:
        print("temp_num", temp_num)
        break

for i in range(len(a)):
    if i == 5:
        print("range", a[i])


my_list = [1, "a", "b", "c"]
my_list[0] = "z"
x = my_list[1]
print(x)
my_list.append(8)
print("my_list:",my_list[2])
my_list.pop(0)
print("my_list:",my_list[0])
my_list.insert(1, 90)
print("my_list:",my_list[1])
print("my_list:",my_list)

x_tuple = 'summer', 'winter', 'spring', 'fall'
for temp_num_tuple in x_tuple:
    print("x_tuple:",temp_num_tuple)

my_dictionaty = {'a':1, 'b':2, 'c':3,}
my_dictionaty['b'] = 6
del(my_dictionaty['a'])
print("my_dictionaty:", my_dictionaty.keys(),my_dictionaty.values())
print("my_dictionaty:", my_dictionaty['b'])




