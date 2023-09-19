input = open("input.txt","r")
output = open("output.txt","w")

n = int(input.readline())
first = 0
second = 1

for i in range(n):
    if i%2==0:
        first = first+second
    else:
        second=first+second
    
if n%2==0:
    output.write(str(first))
else:
    output.write(str(second))
