#βιβλιοθήκες
from datetime import date
from datetime import datetime

print("Δώσε μια ημερομηνία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ  και εμφανίστεί πόσες μέρες/ώρες/δευτερόλεπτα \n απέχει αυτή από την τρέχουσα ημερομηνία του υπολογιστή σου...")

#Εκχώρηση ημερωμηνίας από το χρήστη
userDate=input()
listana=userDate.split("/")
day=listana[0]
month=listana[1]
year=listana[2]

#Λήψη τρέχουσας ημερομηνίας από το υπολογιστή
today = date.today()

#Λήψη τρέχουσας ώρας από το υπολογιστή
now = datetime.now()
#Μετατροπή ημερομηνίας σε string
d3= today.strftime("%d/%m/%Y")
#Διαχωρισμός του προηγούμενου string και εκχώρηση σε λίστα
d3=d3.split("/")
currentDay=d3[0]
currentMonth=d3[1]
currentYear=d3[2]
#Υπολογιμός ημερών
d0 = date(int(year), int(month), int(day))
d1 = date(int(currentYear), int(currentMonth), int(currentDay))
delta = d0 - d1


#Μετροπή τρέχουσας ώρας σε string
time = now.strftime("%H:%M:%S")
#Διαχωρισμός του προηγούμενου string
time = time.split(":")
#Υπολογιμός ωρών(συνυπολογίζοντας τις ώρες μέχρι το τέλος της ημέρας)
hoursUntilTheEndOfTheDay= 24-int(time[0])
daysLeft=delta.days*24 + hoursUntilTheEndOfTheDay
#Υπλογιμός δευτερολέπτων(συνυπολογίζοντας τα δευτερόλεπτα μέχρι το τέλος της ημέρας)
totalsec=int(time[0])*3600+int(time[1])*60 + int(time[2])
secondsUntilTheEndOfTheDay=86400-totalsec
secondsLeft=daysLeft*3600+secondsUntilTheEndOfTheDay
#Εμφάνηση αποτελεσμάτων
print("Απέχει ",delta.days , " μέρες,")
print(daysLeft ," ωρες,")
print(secondsLeft," δευτερολεπτα")
print("Τέλος,")
#Υπολογισμός ημερών μήνα
if(int(month)!=2):
    if(int(month)<=7):
        if(int(month)%2==0):
            print("Αυτός ο μήνας έχει 30 μέρες")
        else:
            print("Αυτός ο μήνας έχει 31 μέρες")
    elif(int(month)>7):
        if (int(month) % 2 == 1):
            print("Αυτός ο μήνας έχει 30 μέρες")
        else:
            print("Αυτός ο μήνας έχει 31 μέρες")
else:
    if(int(year)%4==0):
        if(int(year)%100!=0):
            print("Αυτός ο μήνας έχει 29 μέρες")
    elif(int(year)%400==0):
            print("Αυτός ο μήνας έχει 29 μέρες")
    else:
        print("Αυτός ο μήνας έχει 28 μέρες")