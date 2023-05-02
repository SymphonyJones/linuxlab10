import argparse
import sys
pars = argparse.ArgumentParser()
pars.add_argument('shift_value', type=int, help='Shift value for Caesar Cipher')
args = pars.parse_args()

shift_val = args.shift_value % 26  # ensure shift value is between 0-25

output = ""  # holder for encoded w/o formatting

# if you are taking input from stdin to record encoded w/o formatting
for l_1 in sys.stdin:
    for l_2 in l_1.upper():
        if l_2.isalpha():
            encoded_ascii = chr((ord(l_2) - ord('A') + shift_val) % 26 + ord('A'))
            output += encoded_ascii

# print encoded data with formatting
l_2count = 0
for i in output:
    l_2count += 1
    if l_2count % 5 != 0:
        print(i, end="")
    elif l_2count % 50 == 0:
        print(i, end=" \n")
    else:
        print(i, end=" ")
print("\n")
