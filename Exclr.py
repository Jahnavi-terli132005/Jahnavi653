string="session is going to start"
"""for word in string.split():
    if len(word)%2==0:
        print(word)
    if len(word)>3:
        print(word[0])"""
x=[i for i in string.split() if len(i)>=5]
print(x)
print(string[::-1])
for i in range(16):
    if i%3==0:
        print(i,"Bizz")
    elif i%5==0:
        print(i,"Bigg")
    elif i%3==0 and i%5==0:
        print(i,"Bizz and Bigg")
    else:
        print(i,"Not a mutiple of 3 or 5")