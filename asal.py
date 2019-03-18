#sayının asal olup olmadığını kontrol eder
# sayının çarpanlarını gösterir

def asal(n):

    control = 0

    for i in range(2, int(n)):
        if (int(n) % i == 0):
            n=n/i
            control += 1
            print(i)
           

    if (control != 0):
        print("Sayı Asal Değil")
    else:
        print("Sayı Asal")


print(asal(13))
