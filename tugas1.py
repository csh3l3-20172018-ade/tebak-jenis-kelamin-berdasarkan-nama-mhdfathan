nama = input("masukkan nama: ") #memasukkan sebuah nama

def laki(n): #menghitung kemunculan huruf yg biasanya pada laki - laki
    x=0
    for i in range(0,len(nama)):
        if (n[i]=="b" or n[i]=="B"):
            x +=1
        elif (n[i]=="d" or n[i]=="D"):
            x+=1
        elif (n[i]=="o" or n[i]=="O"):
            x+=1
        elif (n[i]=="m" or n[i]=="M"):
            x+=1
#"x+=1" incremental dari penghitungan banyaknya munculnya huruf tersebut
    return x

def perempuan(n): #fungsi untuk menghitung kemunculan huruf yg biasa nya terdapat di nama perempuan
    x = 0
    for i in range(0,len(nama)):
        if (n[i] == "a" or n[i] == "A"):
            x += 1
        elif (n[i] == "u" or n[i] == "U"):
            x += 1
        elif (n[i] == "e" or n[i] == "E"):
            x += 1
        elif (n[i] == "t" or n[i] == "T"):
            x += 1
        elif (n[i] == "l" or n[i] == "L"):
            x += 1
        elif (n[i] == "i" or n[i] == "I"):
            x += 1

    return x

#pembuatan keputusan apakah nama tersebut laki- laki atau perempuan
#keputusan diambil dari mana yg lebih sering muncul hurufnya
if laki(nama)>perempuan(nama):
    print("lelaki nih")
elif perempuan(nama)>laki(nama):
    print("perempuan ini mah")
elif perempuan(nama)==laki(nama):
    print("waduh kelamin ganda hehe")
else:
    print("UnDefined")
    
#kesimpulan = cara tersebut dapat digunakan namun untuk beberapa nama sangatlah tidak akurat
