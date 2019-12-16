#1
# a = 1/0
# print(a)
# ZeroDivisionError: division by zero

#2
try:
    a = 1 / 0
except:
    print("except")

#3
try :
    x = 1
finally :
    print("finally")
#Yes the code legal, try, expet or finnaly

#4
# Except: block lets you handle the error
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement

#5
#?? לא הבנתי כל כך

#6
# Except IOError - I/O input output exceptions
# Except ZeroDivisionError - Python indicates that the second argument used in a division (or modulo) operation was zero.

#7
# Create a text file named “words.txt”
# programmatically
# file = open("F:\\DevOpps\\Lesson3.txt",'w')
# file.close()

#8
# Write your name into the file
# file = open("F:\\DevOpps\\Lesson3.txt",'w')
# file.write("Kostya")
# file.close()

#9
# Read your file content and print it
# file = open("F:\\DevOpps\\Lesson3.txt",'r')
# fromfile = file.read()
# print("fromfile:",fromfile)
# file.close()

#10
# Write Hebrew content into your text file and
# print its content programmatically.
# file = open("F:\\DevOpps\\Lesson3.txt",'w', encoding='utf-8')
# file.write("קוסטיה")

# file = open("F:\\DevOpps\\Lesson3.txt",'r', encoding='utf-8')
# fromfile = file.read()
# print("fromfile:",fromfile)
# file.close()

#11 Challenge
# Create an image from code (png file) Hint:
# use Pillow
#pip install Pillow
from PIL import Image
img = Image.new('RGB', (60, 30), color='red')
img.save('F:\DevOpps\red.png')



