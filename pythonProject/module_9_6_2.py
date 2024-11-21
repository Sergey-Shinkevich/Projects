
def  all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)):
            y = i + j + 1
            if j > len(text) or y > len(text):
                break
            yield text[j:y]

a = all_variants("abc")
for i in a:
    print(i)

