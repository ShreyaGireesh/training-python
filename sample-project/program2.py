str1 = input("Enter a string:")
vowels = 'aeiouAEIOU'
count=0
for i in str1:
    if i in vowels:
        count+=1
print(f"{str1} contains {count} vowels")