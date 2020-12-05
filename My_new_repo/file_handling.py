# File handling with python
# To check existance of file ==> os.path.isfile(fname)

import os
import sys

file_name = "first1_file.txt"
if os.path.isfile(file_name):
    print("File Exists", file_name)
    f = open("first_file.txt", "a+")
    data = "Hello there, this is first_file\n"
    f.writelines(data)
    print(f.tell())
    f.seek(0)
    data_read = f.read()
    print("Read_data : ", data_read)
    f.close()
else:
    print("File does not exists : ", file_name)
    sys.exit(0)  # To terminate program 0-Normal termination
