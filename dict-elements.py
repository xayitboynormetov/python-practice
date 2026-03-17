# Dictonary elementlari bilan ishlash
phone = {
    'brand': 'Apple',
    'model': 'iPhone 17 Pro Max',
    'color': 'Silver',
    'storage': '256GB',
    'price': '$1500'
}

# # get ()metodi - kalit so'z qiymatini olish
# print(phone.get('model'))  # iPhone 17 Pro Max 
# print(phone.get('price'))  # $1500 
# print(phone.get('battery'))  # None, chunki 'battery' kaliti mavjud emas
# print(phone.get('battery', 'Kalit topilmadi'))  # Kalit topilmadi, chunki 'battery' kaliti mavjud emas

# # items() metodi - lug'at elementlarini (kalit-qiymat juftlarini) olish)
# print(phone.items())  # dict_items([('brand', 'Apple'), ('model', 'iPhone 17 Pro Max'), ('color', 'Silver'), ('storage', '256GB'), ('price', '$1500')])
# for key, value in phone.items():
#     print(f"Kalit:: {key}")
#     print(f"Qiymat:: {value}")

telefonlar ={
    'ali' : 'iPhone 17 Pro Max',
    'vali' : 'Samsung Galaxy S23 Ultra',
    'olim' : 'Xiaomi Mi 13 Pro',
    'sardor' : 'Google Pixel 7 Pro'
}

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# # keys() metodi - lug'atning barcha kalitlarini olish
# print(phone.keys())  # dict_keys(['brand', 'model', 'color', 'storage', 'price'])
# print(telefonlar.keys())  # dict_keys(['ali', 'vali', 'olim', 'sardor'])

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

# print(mahsulotlar.keys())

# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# in operatori
# 1.List elementlari orasida qiymat mavjudligini tekshirish
# 2.lug'atda kalit mavjudligini tekshirish
bozorlik = ['anor','uzum','non','baliq']
# print('anor' in bozorlik)  # True
# print('olma' in bozorlik)  # False

# mahsulotlar =  input("Qaysi mahsulotni sotib olmoqchisiz? ")
# if mahsulotlar in bozorlik:
#     print(f"{mahsulotlar.title()} do'konimizda bor.")
# else:   
#     print(f"{mahsulotlar.title()} do'konimizda yo'q.")

# mahsulotlar bu lug'at
for mahsulot in mahsulotlar:
    # print(mahsulot) # mahsulotlar lug'atining kalitlari
    print(f"{mahsulot.title()} do'konimizda bor.")
else:   
    print(f"{mahsulot.title()} do'konimizda yo'q.")

# LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
print("Do'konimizdagi mahsulotlar:")    
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

# value() metodi - lug'atning qiymatlarini list sifatida olish
print(mahsulotlar.values())  # dict_values([10000, 20000, 40000, 25000, 30000])
print("Do'konimizdagi mahsulotlarning narxlari:")
for narx in mahsulotlar.values():
    print(narx)