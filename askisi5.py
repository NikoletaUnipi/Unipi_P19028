#Άνοιγμα αρχείου
with open("quiker.txt","r") as f:

    #Αποθήκευση περιεχομένων του αρχείου στη μεταβλητή fContents
    fContents=f.read()

    #Διαχωρισμός του αρχείου σε λέξεις
    letters=fContents.split()

    #Διαγραφή κομμάτων και τελίων
    for i in range(0, len(letters)):
        word=letters[i]
        word=word.replace(",","")
        word=word.replace(".","")
        letters[i]=word

    #δημιουργία λίστας με λέξεις που έχουν περισσότερα από 3 γράμματα
    lenghtOfFirstList = len(letters)
    newL=[]
    for i in range(0,lenghtOfFirstList):
        if(len(letters[i]) > 3):
            newL.append(letters[i])

    #Αφαίρεση του πρώτου γράμματος και προσθήκη αυτού στο τέλος μαζί με το ay
    newLLenght= len(newL)
    for i in range(0,newLLenght):
        word=newL[i]
        first=word[0]
        word=word[1:]
        word=word+first+'ay'
        newL[i]=word

    #Εκτύπωση λίστας με τις αλλαγμένες λέξεις
    print(newL)