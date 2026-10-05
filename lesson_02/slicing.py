barcode = ("ABCE1234567")

print(barcode[0])
print(barcode[1])

print("A"+"B")

name = "Efe"
surname = "Orhan"

fullname = name + " " + surname

print(fullname)

print(barcode[0] + barcode[1]+ barcode[2])

#slicing, starting index, stopping index, stepping size
"""
barcode[starting index:stopping index:stepping size]
"""
print(barcode[3::])
print(barcode[:3:])
print(barcode[::3])