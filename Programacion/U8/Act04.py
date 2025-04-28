'''
aceptaelreto.com
Problema 522 La desconfianza de la ASALE
'''
abc=['a','b','c','ch','d','e','f','g','h','i','j','k','l','ll','m','n','ñ','o','p','q','r','s','y','u','v','w','x','y','z']

p1=input("Escribe la primera palabra: ")
p2=input("Escribe la segunda palabra: ")

if len(p1)<len(p2):
    pCorta=p1
else:
    pCorta=p2

for i in range(len(pCorta)):
    for letra in abc:
        if False:
            pass
        elif p1[i]==letra and p2[i]!=letra:
            print(p1,", ",p2)
            exit()
        elif p2[i]==letra and p1[i]!=letra:
            print(p2,", ",p1)
            exit()
        elif p1[i]=="c" and (p1[i+1] is not None and p1[i+1]=="h"):
            print(p1,", ",p2)
            exit()
            i+=1
        elif p1[i]=="l" and (p1[i+1] is not None and p1[i+1]=="l"):
            if p2[i]=="l" and (p2[i+1] is not None and p2[i+1]!="l"):
                print(p2,",  ",p1)
                exit()
            elif p2[i]=="l" and (p2[i+1] is not None and p2[i+1]=="l"):
                pass
            else:
                print(p1,", ",p2)
                exit()
            i+=1
        # elif p2[i]=="c" and (p2[i+1] is not None and p2[i+1]=="h"):
        #     print(p2,", ",p1)
        #     exit()
        #     i+=1
        # elif p2[i]=="l" and (p2[i+1] is not None and p2[i+1]=="l"):
        #     print(p2,", ",p1)
        #     exit()
        #     i+=1
print(pCorta)
