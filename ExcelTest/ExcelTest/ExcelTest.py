import ExcelWrite

##텍스트 파일에서 리스트 가져오기
iskeyword=0 
while(iskeyword==0) : #찾는 값이 존재할때까지 반복
    keyword = input("찾을 자료를 입력하세요 : ")
    print('진행중...')
    fileName = "201401.txt"
    list = []

    with open(fileName, "r") as myfile :
        for content in myfile :
            (col1, col2, col3, col4) = content.strip().split("|",3) #한 행을 4개로 나눔
            if(col3==keyword) :
                col4=col4[:-1] #마지막 | 제거
                sublist=[col1,col2,col3,col4] 
                list.append(sublist)
                iskeyword=1 

    if(iskeyword==0) :
        print('자료를 찾을 수 없습니다.')


##엑셀 파일에 쓰기
ExcelWrite.excelWrite(list)
print('완료!')

##https://github.com/jmcnamara/XlsxWriter #참고