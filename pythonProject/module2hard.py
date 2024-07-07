for n in range(3,21):
    result = ''
    for i in range(1,21):
        for j in range(i+1,21):
            if (n%(i+j)) == 0:
                result = result + str(i) + str(j)
    print(n,result)
