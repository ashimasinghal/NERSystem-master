crimefile = open('covid_sym_tracker.txt', 'r')
yourResult = [line.split('\n') for line in crimefile.readlines()]

inList = []
for item in yourResult:
	inList.append(item[0])

#print (inList)

inList2 = [i for i in inList if i != "****************************************"]
inList2 = list(set(inList2))
with open("covid_sym_track.txt", 'w') as output:
    for row in inList2:
        output.write(str(row) + '\n')