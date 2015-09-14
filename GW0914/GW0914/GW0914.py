##함수 사용해보기
#def main():
#    names = getNames()
#    printNames(names)
#    return

#def getNames():
#    names = ["Gw1","Gw2","Gw3"]
#    newName = input("Enter last guest : ")
#    names.append(newName)
#    return names

#def printNames(names):
#    for name in names:
#        print(name)
#    return

#main()

##---------------------------------
##여러개의 return값을 가지는 함수

#def sum_and_mul(a,b):
#    return a+b, a*b

#answer = sum_and_mul(10,30)
#print(answer)
#sum,mul = sum_and_mul(20,10)
#print(sum,mul)

##----------------------------------
##2중포문으로 다중 리스트 출력
##coding:cp949#해당 부분만 cp949로 인코딩하고싶다면,,
#def printData(data):
#    for item in data : 
#        if isinstance(item,list) :
#            for subitem in item :
#                print(subitem)
          
#        else :
#            print(item)


#data = ["홍길동",["베테랑",["황정민","유아인"],"암살","앤트맨"],"고길동",["베테랑2","암살2","앤트맨2"],"김길동",["베테랑3","암살3","앤트맨3"]]
#printData(data)
##----------------------------------------------------------------------------------------------------------------
#import의 두가지 형태
##1번 불러올때마다 임포트네임 입력
#import printData
#printData.printData(printData.data)

##----------------------------------------------------------------------------------------------------------------
##2번 이 함수를 앞으로 항상 printData에서 불러오겠다
#from printData import printData
#data = ["홍길동",["베테랑",["황정민","유아인"],"암살","앤트맨"],"고길동",["베테랑2","암살2","앤트맨2"],"김길동",["베테랑3","암살3","앤트맨3"]]
#printData(data)

##----------------------------------------------------------------------------------------------------------------
##배포패키지
import os

##help(os.mkdir) #함수에 대한 설명 보고싶을때
print(os.getcwd())
#os.mkdir("sample")
os.chdir(".//sample")
#print(os.getcwd())
#os.system("python setup.py sdist") #배포패키지 만들기
os.system("python setup.py install") #패키지 인스톨
#--------------------------------------------------------------------------------------------------------------------