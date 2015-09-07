#data = ['a','b','c',['abcd','efg']]
#print(data)
#print(data[0])
#print(data[-1])
#print(data[-1][-1])
#data2 = ['ff']
#data3 = data + data2
#print(data3)
#guest=['a','b','c']
#guest[0]='h'
#guest[1]=['l','m'] #1번 인덱스에 배열 삽입
#print(guest)
#guest[1:2]=['n','o'] #1번부터 2개의 인덱스에 추가로 삽입
#print(guest)

#guest.insert(2,'e') #2번 인덱스에 삽입
#guest.append('greenjoa') #마지막에 추가

#print(guest)

guest=['a','b','c']
guest.insert(1,'23')
guest.insert(3,'24')
guest.insert(5,'25')
guest.insert(2,[1,2,3])

guest.insert(5,[1,2,3])

guest.insert(8,[1,2,3])
print(guest)

for steps in range(4): #step = 0,1,2,3
    print(guest[steps])
print('------------------')

nEntries = len(guest)
for steps in range(nEntries): #step = 0,1,2,3,...,len(guest)
    print(guest[steps])
print('------------------')

for steps in guest : #step = guest[0],guest[1],...
    print(steps)
print('------------------')

scores = [85,42,11,23,56,54,44,65,78]
scores.sort()
print(scores)
scores.reverse()
print(scores)

top5=scores[0:5]
print(top5)
