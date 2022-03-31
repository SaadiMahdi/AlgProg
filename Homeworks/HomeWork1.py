def seq(n) :
    if n < 3 :
        return n
    else :
        return 2*seq(n-1)+3*seq(n-3)


print(seq(5))
print(seq(2))