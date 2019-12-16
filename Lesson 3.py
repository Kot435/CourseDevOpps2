# My_file = open("F:\DevOpps\Lesson3.txt", 'r', encoding = 'utf8')
# content = My_file.read()
# print(content)
# content.close()
# content.write("F")
# content.seek(0)
# content = My_file.read()
# print(content)
# content.close()

# My_file = open("F:\DevOpps\Lesson3.txt", 'r+', encoding = 'utf8')
# print(My_file.read())
# My_file.close()
My_file = None
try:
    My_file = open("F:\\DevOpps\\Lesson3.txt", 'r+', encoding = 'utf8')
    print(My_file.read())
except  IOError as x:
    print("Error: ", x)
finally:
    if My_file!= None:
        print("finnaly")

