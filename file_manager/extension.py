def isformat(filename):
    ext = ['.json', '.csv','.txt','.xlsx']
    if filename and type(filename) == str:
        for item in ext:
            if filename.endswith(item):
                return True
            else:
                continue
    elif filename == '':
        print('Filename is empty')
        return False    
    else:
        print('Filename is not a string')
        return False