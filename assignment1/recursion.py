def rev(a):
    if len(a)==0:
        return ""
    else:
        return a[-1]+rev(a[:-1])
def rev_s(s):
    word=s.split()
    r_word=[rev(i) for i in word]
    return " ".join(r_word)
s=input()
print(rev_s(s))
