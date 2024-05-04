from file_manager.file import File_manager

file = File_manager()

print(file.create('test.txt'))

# print(file.gettinfo('asi..xlsx', ['size']))

# print(file.update('test.txt', '\nGreat change is twoday and yesterday', 30))
# print(file.gettinfo('test.txt', ['size', 'format', 'preview']))
print(file.delete('test.txt'))