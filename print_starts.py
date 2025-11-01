line = int(input(">"))

n_str = ""

p = line - 1
l = 1


for i in range(line):

    for j in range(p):
        n_str += " "
    
    for k in range(l):
        n_str += "*"

    print(n_str)
    n_str = ""
    p -= 1
    l += 2
    


