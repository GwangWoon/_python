##coding:cp949
#fileName = "GW.txt"
#with open(fileName, "w+") as myfile :
#    myfile.write("201111258 ����\n")
#    myfile.write("201111258 �迵��\n")
#    myfile.write("201111258 ���м�\n")



#fileName = "GW.txt"
#with open(fileName, "r") as myfile :
#    content = myfile.read()
#    print(content)



#fileName = "GW.txt"
#with open(fileName, "r") as myfile :
#    content = myfile.readlines()
#    for line in content :
#        print(line)

#fileName = "��������¿���1.txt"
#fileName2 = "Monica.txt"
#with open(fileName, "r") as myfile, open(fileName2, mode="w") as monica:
#    for content in myfile :
#        (role, etc) = content.strip().split(":")
#        print (role)
#        if(role=="Monica") :
#            print (etc)
#            monica.write(etc+"\n")



import pickle
fileName = "��������¿���2.txt"
fileName2 = "Monica.txt"
list = []
with open(fileName, "r") as myfile, open(fileName2, mode="wb") as monica:
    for content in myfile :
        (role, etc) = content.strip().split(":",1)
        print (role)
        list.append(role)
        #if(role=="Monica") :
        #    print (etc)
        #    monica.write(etc+"\n")

    pickle.dump(list,monica)
    
with  open(fileName2, mode="rb") as monica :
    result = pickle.load(monica)
    print (result)