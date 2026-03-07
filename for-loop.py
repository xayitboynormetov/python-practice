# Loop - sikl
# 1. for loop
# 2. while loop
# students = ['Charos' , 'Kumush', 'Akmal', 'Ozodbek', 'Farida', 'Asal']
# # print(students['Charos'])
# # print(students['kumush'])
# # print(students['Akmal'])
# # print(students['Ozodbek'])
# # print(students['Farida'])
# for student in students:
#     # print(students)
#     print(f"Hurmatli {student}, sizmi interviwga taklif qilamiz")
#     print("Hurmat bilan Al-Xorazmiy vorislari loyhasi")

# nums = list(range(1,101))
# for number in nums:
#     print(number)


# kinolar = []
# for n in range(5):
#     kino = input(f"{n + 1}- kinoni kiriting: ")
#     kinolar.append(kino)
# print(kinolar)

# inson_soni = int(input("nechta odam bolan uchrashdingiz? "))
# insonlar = []
# for n in range(inson_soni):
#     inson = input(f"{n + 1} - insonni ismini kiriting: ")
#     insonlar.append(inson)
# print(insonlar)
    
# dostlar_soni = int(input("Nechta dostingiz bor? "))
# dostlar = []
# for n in range(dostlar_soni):
#     dost = input(f"{n+1} - dostingizni ismini kiriting: ")
#     dostlar.append(dost)
# print(dostlar)


# telefonlar = []
# print("Yoqtirgan 4ta telefonningizni kiriting:")
# for n in range(4):
#     tel = input(f"{n+1} Telefonni kiriting: ")
#     telefonlar.append(tel)
# print(telefonlar)


# numbers = [69, 48, 58, 45, 57, 55, 88, 89, 85]
# min_value = min(numbers)
# results =[]
# # print(min_value)
# for number in numbers:
#     results.append( number / min_value)

# print( results)
# print(sum(numbers))
# s = 0
# for number in numbers:
#     s += number 
# print(s)

# s = 0
# for son in range(2, 51, 2):
#     s += son
# print(s)

# kopaytma = 1
# for son in range(1,11):
#     kopaytma *= son 
# print(kopaytma)

# kopaytma = 1
# yigindi = 0
# for son in range(1,20,2):
#     kopaytma *= son
#     yigindi += son

# print(kopaytma / yigindi )

# nums = [24, 50, 72, 96, 95]
# s = 0
# for son in nums:
#     s += son **2
# print(s)

# nums = [24, 50, 72, 96, 95]
# s = 0
# for son in nums:
#     s += son
#     yigindi  = s / len(nums)
# print(yigindi)

# nums = [12, -5, 15, 89, -75, -18]
# s = 0
# k = 1
# for son in nums:
#     if son > 0:
#         s  += son
#     else:
#         k *= son
# print(s)
# print(k)


# kopaytma = 1
# s = 0
# for m in range(2, 20, 2):
#     if m % 2 == 0:
#         kopaytma *= m
#     else:
#         s += n
# print(kopaytma / s)

# nums = [12, -5, 15, 89, -75, 18]
# s = 0
# for son in nums:
#     s += son
#     yigindi  = s / len(nums)
# print(yigindi)
import math


# k = 1
# nums = [12, -5, 15, 89, -75, 18]
# length = len(nums)
# for n in nums:
#     k *= n
# ortacha = math.pow(k,1 / len(nums))
# print(ortacha)

# numbers = [7, 97, -58, 90]
# s = 0
# counter = 0
# for n in numbers:
#     if n % 2 == 0:
#         s += n
#         counter += 1
# print(s / counter)


# numbers = [97, 97, -92, 14, 22]
# s = 0
# for n in numbers:
#     if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
#         s += n
# print(s) 
        
# 114
# numbers = [44, 34, 42, 83, 43, 64]
# k = 1
# for n in numbers:
#     if n % 2 == 0 or n % 5 == 0:
#         k *= n
        
# print(math.sin(k))


# 113
# numbers = [93, 64, -90, 74, 62, -83, 58, 15, -37]
# s = 0
# c = 0
# for n in numbers:
#     if n < 0:
#         s += n
#         c += 1
# print( s / c)

# 111
# m = int(input("M sonni kiriting : "))
# sonlar = [12, 88, 30, 87]
# s = 0
# for n in sonlar:
#     if n > m:
#         s += n
# print(s)


# 115
# m = int(input("M sonni kiriting : "))
# sonlar = [85, 15, 57, 68, 18, 67, 7, 45, 69, 21, 1, 5, 98, 34]
# s = 0
# for n in sonlar:
#     if m > n:
#         s += n **2
# print(s)

# 118
# nums = [76, 12, 51, 50, 98]
# c = 0
# for num in nums:
#     if num % 2 == 1:
#         s += num
#         c += 1

# print(s / c)

# 122
# numbers = [44, 59, -75, 73]
# k = 1
# s = 0
# for n in numbers:
#     s += n
#     k += n **2
# ortacha = (s / len(numbers))
# print(k)
# print(ortacha)

# 126
# numbers = [7, 24, -5, 23, 99, -3, 24, 51]
# s = 0
# for n in numbers:
#     s += n
# c = (s / len (numbers))
# log_value = math.log(c)
# print(log_value)

# for index in range(len(numbers)):
#     if numbers[index] < 0:
#         numbers[index] = log_value

# print(numbers)

# 127
# numbers = [46, 23, -52, 34, 6, -18, 52]
# min_value = min(numbers)
# for index in range(len(numbers)):
#     if numbers[index] < 0:
#         numbers[index] = min_value ** 2

# print(*numbers)

# 110
# k = int(input("k sonni kiriting: "))
# m = int(input("m sonni kiriting: "))
# numbers = [7, 11, 83, 18, 31]
# kopaytma = 1
# for n in numbers:
#     if k == n or m == n:
#         kopaytma *= n
# print(kopaytma)

# 104
# sonlar = [74, 0, 1, 33]
# min_value = min(sonlar)
# last_element = sonlar[-1]
# min_index = sonlar.index(min_value)
# sonlar [min_index], sonlar [-1] =  last_element, min_value
# sonlar[-1] = min_value
# print(sonlar)

# 124
# numbers = [29, 50, -14, 4, 27, -56]
# k = int(input("Element ornini kiriting: "))
# max_value = max(numbers)
# max_index = numbers.index(max_value)
# numbers[max_index] = numbers[k - 1]
# numbers[k - 1] = max_value
# print(numbers)


