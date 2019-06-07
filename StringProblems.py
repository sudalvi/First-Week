s = "Suraj"
#print(len(s))
def cal(sd):
    count = 0
    for i in s:
        count += 1        
    return count
print(cal(s))

#Change  String end part

def chng(st):    
    if len(st) >= 3 and st[(len(st)-3):] == "ing":
        return st + "ly"
    elif len(st) >= 3 and st[(len(st)-3):] != "ing":
        return st + "ing"
    else:
        return st

print(chng("pi"))