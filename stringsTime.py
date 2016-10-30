#!/usr/bin/python3


string1 = "hello Yashwanth!"
string2 = "Hello Southwest!"

print("The string1 value is", string1)
print("The 7th character in string1 is", string1[6])
print("Concat string1 and string2 ", string1+string2)
print("string 1 is %s and string 2 is %s" % (string1, string2))

if 'Y' in string1:
    print('Yashwanth')
elif 'S' in string2:
    print('SWA')
else:
    print('Nothing worked!')

print(".......String Operations.........")

print("String capitalization ", string1.capitalize())
print("String center", string2.center(100, 'Z'))
print("String count", string1.count("wan", 6, 15))

