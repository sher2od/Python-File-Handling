file_name = 'Input/students.txt'

# Fayldan ismlar ro'yxatini olish
with open(file_name, 'r') as f:
    names = [line.strip() for line in f]

# Foydalanuvchidan ism kiritishni so'rash
user_name = input("Ism kiriting: ")

# Tekshirish
if user_name in names:
    print(f"{user_name} faylda mavjud.")
else:
    print(f"{user_name} faylda yo‘q.")
