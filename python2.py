import sys

counter1 = 0
counter2 = 0
flag = True

while (flag):
 for char in sys.stdin.read(1):
  if char == '\n':
   flag = False
   break  
  else:
   if char == '(':
    counter1 = counter1 + 1
   elif char == ')':
    counter2 = counter2 + 1

if counter1 == counter2 :
 print "Ok xD !"
else:
 print "Not a mathematical expression", counter1, "(", "vs", counter2, ")"

