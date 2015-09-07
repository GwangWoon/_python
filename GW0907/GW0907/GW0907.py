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

#guest=['a','b','c']
#guest.insert(1,'23')
#guest.insert(3,'24')
#guest.insert(5,'25')
#guest.insert(2,[1,2,3])

#guest.insert(5,[1,2,3])

#guest.insert(8,[1,2,3])
#print(guest)

#for steps in range(4): #step = 0,1,2,3
#    print(guest[steps])
#print('------------------')

#nEntries = len(guest)
#for steps in range(nEntries): #step = 0,1,2,3,...,len(guest)
#    print(guest[steps])
#print('------------------')

#for steps in guest : #step = guest[0],guest[1],...
#    print(steps)
#print('------------------')
#------------------------------------------------------




#scores = [85,42,11,23,56,54,44,65,78]
#scores.sort()
#print(scores)
#scores.reverse()
#print(scores)

#top5=scores[0:5] #상위 5개 뽑기
#print(top5)
#------------------------------------------------------

#data = ['a','b','c',['abcd','efg']]

#for steps in data:
#    if isinstance(steps, list) : #이중 리스트 들어갈경우(steps가 list라면)
#        for step in steps : #steps에서 다시 돌림
#            print(step)
#    else :
#        print(steps)
#------------------------------------------------------

#scores = [85,42,11,23,56,54,23,65,78]
#num = scores.pop(2) #2번째요소를 반환하고 삭제
#print(num)
#print(scores)

#num = scores.count(23) #스코어에서 23의 갯수 반환
#print(num)

#scores.extend([50,60]) #리스트에 추가
#print(scores)
#------------------------------------------------------

t1=()
t2=(1,)
t3=(1,2,3)
print(t3)