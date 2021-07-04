import random
import os
import sys
import time

con = {'lanjut', 'lagi', 'continue', 'retry', 'lanjuti', 'main', 'play', 'ya','y', 'l', 'main lagi'}

loop = [3]
nyawa = 3
hasil = ''

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

os.system('cls')
time.sleep(0.5)
print('Selamat datang di game tebak angka. \nAnda harus menebak angka 1-10 dengan 3 kesempatan')
time.sleep(0.5)
ulang = str(input('Apakah anda mau main? '))

if ulang in con:
    while ulang in con:
        os.system('cls')

        comp = random.randint(1, 10)

        while nyawa > 0:
            time.sleep(0.5)
            p = input("Masukan angka tebakan anda: ")

            if p in angka :
                nomor = int()

            nyawa -= 1

            if nyawa == 2:
                hasil = 'Masih ada 2 kesempatan lagi'
            elif nyawa == 1:
                hasil = 'Masih ada 1 kesempatan lagi'
            else:
                hasil = 'Anda gagal menebak angkanya.\nAngka yang diacak adalah ' + str(comp)

            if nyawa > 0 :
                if p == comp :
                    nyawa -= nyawa
                    os.system('cls')
                    time.sleep(0.5)
                    print('Anda BENAR. \nAngka yang dicari adalah ' + str(comp))
                elif p < comp :
                    os.system('cls')
                    time.sleep(0.5)
                    print("Terlalu RENDAH. \n" + str(hasil))
                elif p > comp :
                    os.system('cls')
                    time.sleep(0.5)
                    print("Terlalu TINGGI. \n" + str(hasil))
            else:
                if p != comp:
                    os.system('cls')
                    time.sleep(0.5)
                    print(hasil)
                else:
                    os.system('cls')
                    time.sleep(0.5)
                    nyawa += 1
                    print("Yang anda masukan bukan angka")

        time.sleep(0.5)
        ulang = input(str('lanjut / tidak? '))

        if ulang in con:
            nyawa += 3

    os.system('cls')
    time.sleep(0.5)
    print('Terima kasih sudah bermain')
else:
    os.system('cls')
    time.sleep(0.5)
    print('Terima kasih sudah bermain')
