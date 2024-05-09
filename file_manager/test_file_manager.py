from file import File_manager

file = File_manager()
 
print(file.create('test.txt'))


print(file.update('test.txt', '\nGreat change again 3', 2))
print(file.gettinfo('test.txt'))
# print(file.delete('test.txt'))