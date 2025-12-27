def rs(s):
    if len(s)==0:
        return s
    return rs(s[1:]) + s[0]

s = "Praveen"
print(rs(s))