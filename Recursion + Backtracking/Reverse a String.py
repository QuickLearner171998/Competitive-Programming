def storeRevStr(s, newS):
    if len(s) == 0:
        return newS
    newS = storeRevStr(s[1:], newS)
    newS += s[0]
    return newS


def revStr(s):
    return storeRevStr(s, "")


print(revStr("Hello World"))
