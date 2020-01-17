print("Γράψε έναν αριθμό : ")
num = int(input())
num= num*3 +1
print("Ο νέος αριθμός είναι o " + str(num))
sum = 1000 #Για να μπει στο loop
while sum>9:
    sum=0
    while num > 0:

         sum = num % 10 + sum
         num = num // 10

    print ("-->" + str(sum))
    num=sum