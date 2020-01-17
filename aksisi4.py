#Δημιουργία συνάρτησης για άσκηση 4
def askisi4():
    # Λήψη δεδομένων από το χρήστη
    print("Give me a Letter...")
    x = input()
    #Μετατροπή γραμμάτων σε κώδικα ASCII
    asciiNum=ord(x)
    #Έλεγχος για το αν ο αριθμός είναι πρώτος
    isPrime = "είναι" #True
    divisibleBy=".Δεν διαιρείται με κανέναν αριθμό εκτός από το ένα και τον εαυτό του."
    for i in range(2,asciiNum//2):
        if(asciiNum % i) == 0:
            isPrime = " δεν ειναι" #False
            divisibleBy=".Διαιρείται με τον αριμθό " + str(i) + " ή και άλλους."
            break
    #Εμφάνηση αποτελέσματος
    print("Ο αριθμός " + str(asciiNum) +" " + isPrime + " πρώτος" + divisibleBy)

#Κλήση συνάρτησης
askisi4()