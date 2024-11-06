array=[]
sum=0
j=int(input("Dime cuantos numeros vas a sumar: "))
for i in range(0,j):
    print("Dime el",i+1,"º numero")
    num=int(input())
    array.append(num)

for i in array:
    sum=sum+i

print(sum)