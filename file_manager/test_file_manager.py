from file import File_manager

file = File_manager()

# print(file.create('test.txt'))

# print(file.gettinfo('asi..xlsx', ['size']))

print(file.update('test.txt', '\nGreat change', 3))
# print(file.gettinfo('test.txt', ['size', 'format', 'preview']))
# print(file.delete('test.txt'))