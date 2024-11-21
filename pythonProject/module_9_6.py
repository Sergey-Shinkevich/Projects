
def  all_variants(text):
    from itertools import combinations
    for i in range (1,len(text)+1):
        result = combinations(text, i)
        for j in result:
            yield ''.join(j)

a = all_variants("abc")
for i in a:
    print(i)

