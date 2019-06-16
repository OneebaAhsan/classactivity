#----------- TYPE 4 excercise   Tell whether a number is even or odd
def num(n):
    if n%2==0:
        print("Number is even")
    else:
        print("Number is odd") 

    return (n)

a = int(input('Enter a number:  '))
output = num(a)
print(output) 

# OR

def num(n):
    if n%2==0:
        s=0
        return s
    else:
        s=1
        return s

    return (n)

a = int(input('Enter a number:  '))
output = num(a)
if output==0:
    print('Number is even ')
else: 
    print('Number is odd')