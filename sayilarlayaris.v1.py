import random
yaris_list1 = []
yaris_list2 = []
sayac= 0
devam2= True
print("Sayılarla Yarış v1")   
def pist():
    print("            ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
    print(f"Oyuncu     : {yaris_list1}")
    print("             ―   ―   ―   ―   ―   ―   ―   ―   ―   ―   ―   ―   ―   ―   ―   ―   ―   ―   ―   ―")
    print(f"Bilgisayar : {yaris_list2}")
    print("            ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")

while devam2:
    print("1 - Oyunu Başlat")
    print("2- Kurallar")
    print("3- Yapımcılar")
    print("4- Çıkış")
    secim = int(input("Lütfen Seçim Yapınız(1,2,3,4)\t"))
    if(secim==1):
        devam= True 
    elif(secim == 2):
        print("Oyun Kuralları:\n1- Tahmin edilmesi gereken sayı 1'den 10'a kadar sayılar oyuncu tarafından giriş yapılır.: ")
        print("2-[1,10] aralığında tahminde bulunabilirsiniz")
        print("3-Pisti İlk bitiren yarışçı oyunu kazancaktır")
        print("4-Puanlama Sistemi tahmin edilen sayıya yakınlık derecesine göredir.")
        print("  [1,4] kadar değerler 2 puan alır.\n  [5,8] kadar değerlerde 1 puan alır\n  0 değeri alırsa 3 puan alacaktır.\n\n")
        devam= False
    elif(secim==3):
        print("Yunus AYGÜN\nFatih KOŞDAŞ\nMehmet Burak KOYUNCULAR\n")
        devam = False
    elif(secim==4):
        print("Uygulamadan çıkış yapılıyor,lütfen bekleyiniz.\n")
        devam2 = False
    else:
        print("Hatalı secim yaptınız") 
    while devam:
        a=True
        while a:
            devam3= True
            tahmin= (random.randint(1,10))  
            sayac = sayac+1
            bilgisayar = (random.randint(1,10))
            print(f"{sayac}.Tur")
            while devam3:
                oyuncu=int(input("Tahmin değerini giriniz\t\t:")) 
                a = type(oyuncu)
                if(oyuncu >=0 and oyuncu <=10 and a == int): 
                    devam3 = False 
                else:
                    print("Lütfen [0,10] aralığında tahmin yapınız.")
            print(f"Bilgsayarın tahmin degeri\t:{bilgisayar}")
            print(f"Tahmin edilmesi gereken sayı\t:{tahmin}\n")
            oyuncu_y = abs(oyuncu- tahmin) 
            pc_y = abs(bilgisayar - tahmin)  
            if(oyuncu_y < pc_y): 
                if(oyuncu_y == 0):
                    for i in range(1,4):
                        yaris_list1.append('X')
                    pist()
                elif(oyuncu_y >=0 and oyuncu_y <=4 ):
                    for i in range(1,3):
                        yaris_list1.append('X')
                    pist()
                elif(oyuncu_y >=5 and oyuncu_y <=8):
                    yaris_list1.append('X')
                    pist()
            elif(oyuncu_y > pc_y):
                if(pc_y == 0):
                    for i in range(1,4):
                        yaris_list2.append("X")
                    pist()
                elif(pc_y >=0 and pc_y <=4 ):
                    for i in range(1,3):
                        yaris_list2.append("X")
                    pist()
                elif(pc_y >=5 and pc_y <=8):
                    yaris_list2.append("X")
                    pist()
            else:
                print("*Eşit tahminde bulundunuz*\n")
                pist()
                print("\n\n")
                continue

            if (len(yaris_list1)>=15):
                a = False
                print("Tebrikler Kazandınız\n")
            elif(len(yaris_list2)>=15):
                a=False
                print("Bilgisayar Kazandı :(\nKAYBETTİNİZ\n")

        pist()
        print("\n\n")
        kontrol = input("\n Tekrar oynamak istiyor musunuz ? E/H ")
        if (kontrol == "E" or kontrol== "e"):
            sayac = 0
            yaris_list1=[]
            yaris_list2=[]
            continue
        elif(kontrol == "H" or kontrol== "h"):
            print("Oynadığınız için teşekkür ederiz :)")
            devam = False
            sayac = 0
            yaris_list1=[]
            yaris_list2=[]
        else:
            print("Hatalı karakter girdiniz")
            kontrol = input("\n Tekrar oynamak istiyor musunuz ? E/H ")
            if (kontrol == "E" or kontrol== "e"):
                sayac = 0
                yaris_list1=[]
                yaris_list2=[]
                continue
            elif(kontrol == "H" or kontrol== "h"):
                print("Oynadığınız için teşekkür ederiz :)")
                devam = False
                sayac = 0
                yaris_list1=[]
                yaris_list2=[]
            else:
                print("Tekrar hatalı giriş yaptınız, ana ekrana yönlendiriliyorsunuz...")
                devam = False

