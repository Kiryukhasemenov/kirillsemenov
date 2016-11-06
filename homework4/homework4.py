w=input()
a=len(w)
b=a//2
bw=w[:b-1:-1]
for index,letter in enumerate(w):
    if index<=b-1:
        print(letter)
    else:
        for index,letter in enumerate(bw):
            print(letter)
        break
