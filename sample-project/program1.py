# program to find the count of even and odd no in a range, 
# if any of the count reaches 3 break the loop, if a 5 occured display the message skipping 5

count_even = 0
count_odd = 0
n = int(input("Enter the range:"))
for i in range(1,n):
    if i%2 == 0:
        print(f"{i} is even")
        count_even+=1
    else:
        print(f"{i} is odd")
        count_odd+=1
    if i == 5:
        print("Skipping five")
        continue
    if count_even == 3 or count_odd==3:
        print("Count reached 3")
        break
    
print(f"Even count:{count_even}\nOdd count:{count_odd}\nExiting loop...")

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')
