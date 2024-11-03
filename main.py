import random



maxfiy_raqam = random.randint(1, 10)
tahminlar = 0

print("Raqamni toping o'yiniga xush kelibsiz!")
print("Men 1 dan 10 gacha raqam o'yladim. Siz bu raqamni taxmin qilishingiz kerak.")


for i in range(3):
    user_input = input(f"{i + 1}-urinish: Raqamni kiriting: ")
    kiritilgan_raqam = int(user_input)
    tahminlar += 1
        
    if kiritilgan_raqam == maxfiy_raqam:
        print(f"Tabriklaymiz! Siz {tahminlar} urinishdagi raqamni taxmin qildingiz!")
        break
    elif kiritilgan_raqam > maxfiy_raqam:
            print("Yashirin raqam kichikroq.")
    else:
            print("Yashirin raqam kattaroq.")


else:
    print(f"O'yin tugadi! Yashirin raqam {maxfiy_raqam} edi.")

