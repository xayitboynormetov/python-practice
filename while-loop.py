# Takrorlanish operatorlari
# 1. for loop
# 2. while loop

# son = 1
# while son < 11:
#     print(son)
#     son += 1

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# break(sindirish) operatori
sonlar = list(range(1 , 11))
# for son in sonlar:
#     if  son == 5:
#         break
# print(f"{son} ning kvadrati {son**2} ga teng")

# contiunue(davom etish) operatori
# for son in sonlar:
#     if son == 7:
#         continue

#     print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)


savol = "yaxshi ko'rgan kitobingizni kiriting "
savol += "(dasturni to'xtatish uchun 'stop' deb yozing): "
kitob = ''
while kitob != 'stop':
    kitob = input(savol)
    if kitob == 'exit':
        break
    else:
        print(kitob)