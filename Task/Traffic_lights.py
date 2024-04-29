file = open('Data','r')
linesfile=file.readlines()[1:20000]
resultfile=[]
for x in linesfile:
    resultfile.append(x.split(',')[0:4])
result = [[int(s1), int(s2), int(s3), int(s4)] for s1, s2, s3, s4 in resultfile]
rezultatas = [sum(i) for i in zip(*result)]
print()
print("1. Find the number of red, yellow & green occurrences:")
print("Red =" , rezultatas[0])
print("Yellow =" , rezultatas[1])
print("Green =" , rezultatas[2])


result2=[]
for item in result:
    if item[0]==1:
        result2.append(item)
        rezultatas2 = [sum(i) for i in zip(*result2)]
print()
print("2. Find how long each colour was active for:")
print("Red colour =", rezultatas2[3], "seconds")

result3=[]
for item in result:
    if item[1]==1:
        result3.append(item)
        rezultatas3 = [sum(i) for i in zip(*result3)]
print("Yellow colour =", rezultatas3[3], "seconds")

result4=[]
for item in result:
    if item[2]==1:
        result4.append(item)
        rezultatas4 = [sum(i) for i in zip(*result4)]
print("Green colour =", rezultatas4[3], "seconds")
