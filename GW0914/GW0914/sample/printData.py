#재귀로 불러오기
def printData(data,level=0):
    for item in data : 
        if isinstance(item,list) :
            printData(item, level+1)
                      
        else :
            print("\t"*level,item)


data = ["홍길동",["베테랑",["황정민","유아인"],"암살","앤트맨"],"고길동",["베테랑2","암살2","앤트맨2"],"김길동",["베테랑3","암살3","앤트맨3"]]
