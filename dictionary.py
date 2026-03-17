# data types(ma'lumot turlari)
# string, int, float, bool, dictionary
# Dictionary - lug'at
car = {
    "brang" : "Ford",
    "model" : "Mustang",
    "color"  : "yellow",
    "price" : 45000

    }
print(car)
print(type(car))

user= {
    "fullname" : "Normetov Xayitboy",
    "email" : "xayitboynormetov02",
    "age" : 15,
    "is_student" : True,
    "favourite_books" : ['Atomic haits', "Otgan kunlar", "Dunyoni ishlari"]
}

# 1
print(user['fullname'])
print(user['favourite_books'])
print('age')

for book in user['favourite_books']:
    print(book)

# 2. Yangi key-value qo'shish
user['is_married'] = False
user['hobbies'] = ['reading a book', 'watching a football match', 'playing computer games'] 
print(user)

# 3. Value o'zgartirish
user['age'] = 15
user['email'] = "xayitboynormetov02@gmail.com"
print(user)

# 4. Bo'sh lug'at(Empty dictionary)
talaba_1 = {}

talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kursdagi student")

# 5. Key-value juftligini o'chirish
talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(talaba_0)
del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
print(talaba_0)

# 6. get() metodi
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
phone = telefonlar.get('vali') # vali kalit so'zining qiymatini olish
print(f"Alining telefoni: {phone}")
print(telefonlar.get('vali'))
print(telefonlar.get('akmal')) # mavjud bo'lmagan kalit so'z uchun None qaytaradi



# Amaliyot
# 1
otam = {'ismi':'Shuhratbek', 'tugulgan yili':1983, 'viloyat':'xorazm'}
print(f" Otam {otam['viloyat'].title()} tugulgan, Otamning ismi {otam['ismi'].title()}, Otamning tugulgan yili {otam['tugulgan yili']}")


onam = {'ismi':'Fazilat', 'tugulgan yili':1983, 'viloyat':'xorazm'}
print(f" Onam {onam['viloyat'].title()} tugulgan, Onamning ismi {onam['ismi'].title()}, Onamning tugulgan yili {onam['tugulgan yili']}")

# 2
oylam = {
    'otam':'tuxum barak',
    'onam':'osh',
    'singlim':'lavash',
    'opam':'somsa'
    
}
print(f"Otamning yoqtirgan taomi {oylam['otam']}")
print(f"Onamning yoqtirgan taomi {oylam['onam']}")
print(f"Opamning yoqtirgan taomi {oylam['opam']}")
print(f"Singlimning yoqtirgan taomi {oylam['singlim']}")
# 3
soz = {
    ' integer':'Butun son',
    'float':'Onlik son',
    'string':'Matn',
    'if':'Agar',
    'else':'Aks holda',
    
    }
print(soz)
    

