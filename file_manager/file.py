from file_manager.extension import isformat
import os


class File_manager:
    """_summary_: Create file, delete, update
    """
    def __init__(self):
        pass

    def create(self, filename):
        """_summary_: create file

        Args:
            filename (str): file name to be created with extension [.csv, json, xlsx, .txt]
        """
        self.filename = filename

        if isformat(self.filename):
            try:
                f = open(self.filename, 'x')
                f.close()
                print(f'{filename} created!')
            except:
                print('Something went wrong')
        else:
            print('file extension is not acceptable')

    def write(self, filename, content):
        """_summary_

        Args:
            filename (_type_): _description_
            content (_type_): _description_
        """
        self.filename = filename

        if isformat(self.filename):
          try:
            with open(filename, 'w') as f:
              f.write(content)
          except:
            print('An error occurred') 
        else:
          print('file extension is not acceptable')
       
    def gettinfo(self, filename):
        """_summary_

        Args:
            filename (_type_): _description_
        """
        self.filename = filename

        try:
           return f'{os.stat(self.filename)}'
        except:
          print('Something went wrong')
    
    def update(self, filename, updates, position):
      """_summary_

      Args:
          filename (_type_): _description_
          update (_type_): _description_
          position (_type_): _description_
      """
      self.filename = filename
      self.updates = updates
      self.position = position

      if isformat(self.filename):
          with open(self.filename, '+a') as f:
            if self.position:
                f.seek(self.position)
                f.write(self.updates)
                f.close()
            else:
                with open(self.filename, '+a') as f:
                    f.writelines(self.updates)
                    f.close()
      else:
          print('Filename is not acceptable')
        

    def delete(self, filename):
        """_summary_

        Args:
            filename (_type_): _description_
        """
        self.filename = filename
        if isformat(self.filename):
            try:
               os.remove(self.filename)
               print(f'{self.filename} deleted!')
            except:
               print('Something went wrong when deleting file')
        else:
            print('File type not supported!')