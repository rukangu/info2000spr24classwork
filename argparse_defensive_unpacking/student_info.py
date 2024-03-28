# demonstrates argparse and sys for commandline arguments

import sys
import time
import argparse

def logrow(data:str, filename:str = "student_details.txt")->None:
    ''' Logs one row at a time and adds a timestamp'''
    with open(filename, 'a') as f:
        # create the timestamp
        t = time.ctime(time.time())
        f.write(f"{t}, {data}\n")

# # to print the arguments each in it's own line
# for item in sys.argv:
#     print(item)
# # print the number of arguments
# print(f"You passed in {len(sys.argv)-1}")


# use arguments passed through the commandline to gather information

# if len(sys.argv)==1:
#     name = input("Name: ")
#     major = input("Major: ")
#     logrow(f'{name},{major}')
# #python student_info.py -n 3
# elif len(sys.argv)==3 and sys.argv[1] == '-n':
#     number = int(sys.argv[2])
#     for _ in range(number):
#         name = input("Name: ")
#         major = input("Major: ")
#         logrow(f'{name},{major}')
# else:
#     print("Usage: python student_info.py -n N")
        

# create a parser
parser = argparse.ArgumentParser(description="Gets information from students and stores it in file")
parser.add_argument('-n',type=int, help="Number of students to get info from", required=True)
parser.add_argument('-f', '--filename', required=False, default='students.txt', help = "file to save")
args = parser.parse_args()

for _ in range(args.n):
    name = input("Name: ")
    major = input("Major: ")
    logrow(f'{name},{major}', args.filename)

