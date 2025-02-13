# x = int(input("Enter a number:"))
# if x>0:
#     print(f"{x} is a positive integer")
# elif x<0:
#     print(f"{x} is a negative integer")
# else:
#     print("Number equals zero")

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)