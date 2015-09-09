#a={'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
#b=a.keys()
#print(b)

#b=list(a.keys()) #리스트 반환

#a={'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
#b=a.values()
#print(b)

#b=list(a.values())
#print(b)

##-----------------------------------
#a={'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
#b=a.items()
#print(b)

#a.clear()

#a.get('name')
#a.get('foo','bar')

#'name' in a

##-----------------------------------
#a = {'홍길동' : {'베테랑':'5.0', '암살':'4.5'},
# '고길동' : {'베테랑':'1.0', '암살':'2.5'}}

#b=a.get('홍길동')
#print(b)

#c=b.get('암살')
#print(c)

#d=a.get('홍길동').get('암살')
#print(d)

##-----------------------------------
#answer = input("would you like express shipping?")
#answer = answer.lower()

#if answer=="yes" :
#    print("That will be an extra $10")
#print("Have a nice day")
##----------------------------------------
#a=[(1,2), (3,4), (5,6)]
#for (first,last) in a :
#    print(first + last)
##----------------------------------------
#for steps in range(1,10,2):
#    print(steps)
##----------------------------------------
#for i in range(2,10):
#    for j in range(1,10):
#        k=i*j
#        print("%d" %i + "*%d" %j + "=%d " %k, end="")
#    print('')


##----------------------------------------
#import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4):
#        turtle.forward(50)
#        turtle.right(90)

##----------------------------------------
#import turtle
#nSides = 5
#for steps in range(nSides):
#    turtle.forward(100)
#    turtle.right(360 / nSides)
#    for moresteps in range(nSides):
#        turtle.forward(50)
#        turtle.right(360 / nSides)

##----------------------------------------
#import turtle
#for steps in ['red','blue','green', 'black']:
#    turtle.color(steps)
#    turtle.forward(100)
#    turtle.right(90)

##----------------------------------------
prompt = """
1.add
2.del
3.list
4.quit
enter numbber: """

number=0
while number!=4:
    print(prompt,end="")
    number=int(input())

##----------------------------------------