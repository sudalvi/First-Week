import operator
d = {2:6,3:7,1:5,4:8,5:9}
sorted_value = sorted(d.items(), key=operator.itemgetter(0))
print(sorted_value)
sorted_value = dict(sorted(d.items(), key=operator.itemgetter(0), reverse=True))
print(sorted_value)