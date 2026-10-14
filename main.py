# Misol 1
n = int(input("Nechta raqam kiritasiz: n="))

sonlar = []
for _ in range(n):
    son = int(input("Son kiriting"))
    sonlar.append(son)

print("Natija:", sonlar)


# Misol 2
sonlar = input("Son kiriting: ").split()

print(f"Sonlar uzunligi {len(sonlar)}")
print(f"Ohirgisi {sonlar[-1]}")

print("Teskarisi:", end=" ")
for i in range(len(sonlar) - 1, -1, -1):
    print(sonlar[i], end=" ")


# Misol 3
sonlar = input("Son kiriting: ").split()
qidiriluvchi = input("Qidiriladigan sonni kiritsin: ")

if qidiriluvchi in sonlar:
    print("Ha, bor")
else:
    print("Bunday raqam yo'q")



# Misol 4
s = input("son kiriting").split()
del s[0], s[-1]
s.sort(key=int)
print(*s)


# Misol 5

sonlar = input("Sonlarni va cheklovchi sonni kiriting: ").split()
n = int(sonlar.pop())

for x in sonlar:
    if int(x) < n:
        print(x, end=" ")







