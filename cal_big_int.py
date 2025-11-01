int_1 =input("Enter first big integer: ")
int_2 =input("Enter second big integer: ")
f = 0
n =  0

def add(a,b,f): # a and b <= 9 

    c = int(a) + int(b)
    
    c = str(c)

    if f:
        c = str(int(c) + 1)
        f = 0


    if len(c) == 2:
        f = 1
        return c[-1] , f
    else:
        return c[0] , f


int_1_len = len(int_1)
int_2_len = len(int_2)
i = 1

new_str= ""

p1 = len(int_1)
p2 = len(int_2)

if p1 > p2:
    p = p2
    n = 1
else:
    p = p1
    n = 2


while i <= p:
    a = int_1[-i]
    b = int_2[-i]
    c,f = add(a,b,f)
    new_str = c + new_str
    i += 1


if f:
    if n == 1:
       first_num = str(int(int_1[:-p])+1)
    else:
       first_num = str(int(int_2[:-p])+1)
else:
    if n == 1:
        first_num = int_1[:-p] 
    else:

       first_num = int_2[:-p]

unb = first_num + new_str
print("The sum is   : " + unb)









