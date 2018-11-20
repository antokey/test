#!/usr/bin/python3
import subprocess
import sys

dir_check = 0
file_check = 0
filename = sys.argv[1]

p = subprocess.Popen(["ls", "-aFl", filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out = p.communicate()[0].decode('utf_8')

read = str(out)
line = read.splitlines()

temp = line[1:]
#print(temp)
#a = temp[0]
#print(a[0])

for i in temp:
    if i[0] == "d": dir_check = dir_check + 1
    elif i[0] == '-': file_check = file_check + 1
    k = i.split()
    print(k[8], k[4], k[0])

print("directory : " + str(dir_check) + " , file : " + str(file_check))
