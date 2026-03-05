# List Bilan Ishlas
# List methods
# 1. list.append(element)
# 2. list.insert(index, element)
# 3. list.remove(element)
# 4. list.pop(index?)
# 5. list.sort()
cars = ['bmw','Mercedes Benz', 'volvo', 'Damas', 'general motors', 'tesla', 'audi']
# cars.sort() # alifbo(englsh) ketma-ketlik bo'yicha tartiplasgh
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# sorted_list = sorted(cars)
# reversedsorted_list = sorted(cars, reverse=True)
# print(cars)
# print(sorted_list)

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))

fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)
# # link() funksiyasi
# user = ['akmal', 'Farida' , 'shodlik']
# students = list(('jamol', 'asal', 'kamol'))




# range() funksiyasi - ma'lum oraliqdagi sonlarni shakillantirish uchun ishlatiladi
# range(start, stop, step)
# range(0,10)
# sonlar = list(range(0, 10))
# juft_sonlar = list(range(2, 21, 2))
# print(sonlar)
# print(juft_sonlar)
                                                                                                                                                                     
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# # RO'YXATNI KESISH
# techs = ['AI', ' Robot', 'Python', 'DB', 'Chat GPT', 'Web']
# my_techs = techs[2:5]
# print(my_techs)
# print(techs[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(techs[2:]) # 2-indexdagi elementdan boshlab ro'yxat oxirigacha kesib oladi



# Amaliyot
# davlatlar = ['Uzbekiston', 'Turkiya', 'Rassiya', 'USA']
# print(davlatlar)

# print(len(davlatlar))

# print(sorted(davlatlar))

# print(sorted(davlatlar, reverse=True))

# print(davlatlar)

# davlatlar.reverse()
# print(davlatlar)

# davlatlar.sort()
# print(davlatlar)

# davlatlar.sort(reverse=True)
# print(davlatlar)

sonlar = list(range(120,1200,2))
print(sum(sonlar))
print(max(sonlar) - min(sonlar))

print(len(sonlar))

print(sonlar[:20])
print(sonlar[-20:])
length = len(sonlar)
start_index = length // 2 - 10
end_index = length // 2 + 10
print(sonlar[start_index : end_index])

# taomlar = ['polov','somsa','lavash','shashlik','barak']

# nonushta = taomlar[:]
# nonushta.remove('barak')
# nonushta.remove('somsa')
# nonushta.remove('shashlik')
# nonushta.append('bilinchik')
# nonushta.append('qaymoq')

# print(taomlar)
# print(nonushta)

# nonushta = tuple(nonushta)



# people = ['Kumush', 'Akmal', 'Ozodbek', 'Farida', 'Gulchehra']
# print(people[-3])
# print(people[-2])
# print(people[-4 : -2])
# print(people[-3 : ])

# # royxatdan nusxa olish
# sonlar = list(range(1,6))
# sonlar2 = sonlar
# # print(sonlar)
# # print(sonlar2)
# # shallow(sayoz) copy
# sonlar2.append(6)
# sonlar2.append(7)
# print(sonlar2)
# print(sonlar)
# # deep(chuqur) cupy
# sonlar = [1, 2, 3, 4, 5] 
# sonlar3 = sonlar[:]
# sonlar3.append(6)
# sonlar3.append(7)
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar3 ro'yxati:", sonlar3)

# # Tuples ozgarmas ro'yxat
# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])
