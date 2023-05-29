#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
amount = 0
for w in range(x):
try:
print(f"{my_list[w]}", end="")
amount += 1

expect IndexError:
break
print()
return(amount)
