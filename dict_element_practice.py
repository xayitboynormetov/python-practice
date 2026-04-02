# Amailyot
# 1.
python_lugat = {
    'Boolean' : 'Mantiqiy qiymot',
    'Integer' : 'Butun son',
    'Float' : 'O\'nlik son',
    'String' : 'Matn',
    'List' : 'Ro\'yxat',
    'Tuple' : 'O\'zgarmas ro\'yxat',
    'Dictionary' : 'Lug\'at',
    'If' : 'Shartlarni tekshirish operatori',
    'For' : 'Takrorlash operatori',
    'While' : 'Shart bajarilguncha takrorlash operatori',
}
for k, q in sorted(python_lugat.items()):
    print(f"{k} - {q}")
# 2.
davlatlar = {
    'O\'zbekiston' : 'Toshkent',
    'Rossiya' : 'Moskva',
    'AQSH' : 'Vashington',
    'Xitoy' : 'Pekin',
    'Yaponiya' : 'Tokio',
    'Germaniya' : 'Berlin',
    'Fransiya' : 'Parij',
    'Italiya' : 'Rim',
    'Kanada' : 'Ottava',
    'Braziliya' : 'Brasiliya',
    'Hindiston' : 'Dehli',
    'Avstraliya' : 'Kanberra',
    'Misr' : 'Qohira',
}
print('Davlatlar:')
for davlat in sorted(davlatlar.keys()):
    print(davlat.upper())
print('Poytaxtlar:')
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt)


# 3.
davlat = input('Qaysi davlatning poytaxti bilishni istaysiz?: ')
if davlatlar.get(davlat) == None:
    print('Kechirasiz, bizda bu davlat haqida ma\'lumot yo\'q')
else:
    print(f"{davlat}ning poytaxti {davlatlar[davlat]}")