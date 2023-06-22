# try:
#     num1 = int(input('Enter a number 1:'))
#     num2 = int(input('Enter a number 2: '))
#     print(num1/num2)

# except ZeroDivisionError:
#     print("Nolga bo'lish mumukin emas")

# except ValueError:
#     print("Iltimos to'g'ri qiymat kiriting:")

# # except:
# #     print("Dasturda xatolik bor")
# except Exception as e:
#      print(e)
#      print("Dasturda xatolik bor")
# else: # qaconki try true qiymat qaytarganda  ishlaydi 
#     print("Dasturda xarolik  yo'q")


try:
    son1 = int(input('Enter a number 1:'))
    son2 = int(input('Enter a number 2:'))
    print(son1/son2)

except ZeroDivisionError:
    print("Nolga bo'lish mumukin emas")
except ValueError:
    print("Iltimos to'g'ri kiriting")
else:
    print("Har doim ishlashi kerak ")
finally:
    print(" Dasturdan foydalanganingiz uchun rahmat")

