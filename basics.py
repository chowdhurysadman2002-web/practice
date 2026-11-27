# def a2(): 
#     n = int(input ("enter number:")) 
#     total = 0 
#     for i in range (1 ,n+1):
#         total += i
        
#         print("sum of the numbers :",total)  
# a2()


# def a3():
    
#     hr = int(input("enter hours:"))
#     total = 0
    
#     if hr <= 2 : total = hr * 50
#     elif hr <= 5 : total = (2 * 50) + ((hr - 2) * 30)   
#     else: total = (2 * 50) + 3 * 30 + (hr-5)*20
#     print("total cost : total tk",total)
# a3()


# **************************
# # marks = []
# # for i in range (1, 6):
# #     mark = float(input(f"enter the marks: "))
# #     marks.append(mark)

# # print(" marks : ",marks)

# # three=marks[:3]
# # two=marks[-2:]
# # print("first three subject marks:",three)
# # print("last two subject marks:",two)


# # print("highest marks:",max(marks))
# # print("lowest marks:",min(marks))

# # count=0

# # for m in marks:
# #     if  m>80:
# #         count += 1
# #         print("subjects with amrks > 80:",count)  
# ******************

# def s1():

#     n=int(input("enter a number: "))

#     even_sum = 0
#     odd_sum = 0
#     even_count = 0
#     odd_count = 0
    
#     for i in range(1, n+1):
        
#         if i%2 == 0:
#             even_sum += i
#             even_count += 1

#         else:
#             odd_sum += i
#             odd_count += 1
            
#     print(f"Even Sum: {even_sum}")
#     print(f"Odd Sum: {odd_sum}")
#     print(f"Even Count: {even_count}")
#     print(f"Odd Count: {odd_count}")
    
# s1()    

# Take an integer n and print its multiplication table from using for loop.***
# def series():
   
#    n = int(input ("enter the number : "))
#    for i in range (1, 10):
#        result = n * i
#        print(f"{n} * {i} = {result}")
       
# series()
    
# Take a nonnegative integer n. Calculate n! using a while loop. Assume 0! = 1.

# n = int(input("Enter a nonnegative integer: "))
# factorial = 1
# i = n

# while i > 1:
#     factorial *= i
#     i -= 1
# print(f"Factorial: {factorial}")


# Take a positive integer. Using a while loop, count its digits, calculate the sum of its digits, and print its last digit.

# n = int(input("Enter a positive integer: "))
# temp = n
# count = 0
# total_sum = 0
# last_digit = n % 10

# while temp > 0:
#     digit = temp % 10
#     total_sum += digit
#     count += 1
#     temp //= 10

# print(f"Total Digits: {count}")
# print(f"Sum of Digits: {total_sum}")
# print(f"Last Digit: {last_digit}")


# Take marks of 6 subjects and store them in a list. Print the complete list, first 3 and last 3 marks using
# slicing, total, average (2 decimal places), and count of subjects with marks ≥ 50.

# marks = []

# for i in range(1, 7):
#     mark = float(input("Enter mark for subject " + str(i) + ": "))
#     marks.append(mark)

# print("First 3:", marks[:3])
# print("Last 3:", marks[-3:])

# total = sum(marks)
# average = total / 6

# passed = 0
# for m in marks:
#     if m >= 50:
#         passed = passed + 1

# print("Total:", total)
# print("Average:", round(average, 2))
# print("Passed Subjects:", passed)

# Take 8 integers into a list. Using a loop and if-else statements, count positive numbers, negative numbers,
# and zeros.
# numbers = []

# for i in range(1, 9):
#     num = int(input("Enter integer " + str(i) + ": "))
#     numbers.append(num)

# pos_count = 0
# neg_count = 0
# zero_count = 0

# for num in numbers:
#     if num > 0:
#         pos_count = pos_count + 1
#     elif num < 0:
#         neg_count = neg_count + 1
#     else:
#         zero_count = zero_count + 1

# print("Positive:", pos_count)
# print("Negative:", neg_count)
# print("Zero:", zero_count)


# Take a list of 8 integers. Using slicing, print the first 4 elements, last 4 elements, every second element
# starting at index 0, and the reversed list.

# numbers = []
# for i in range(1, 9):
#     numbers.append(int(input(f"Enter integer {i}: ")))

# print("First 4:", numbers[:4])
# print("Last 4:", numbers[-4:])
# print("Alternate:", numbers[::2])
# print("Reversed:", numbers[::-1])

    
# Take 5 integers into a list. Using a for loop (without max() or min()), find the largest, smallest, and their
# difference.

# numbers = []
# for i in range(1, 6):
#     numbers.append(int(input(f"Enter integer {i}: ")))

# largest = numbers[0]
# smallest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num

# difference = largest - smallest

# print(f"Largest: {largest}")
# print(f"Smallest: {smallest}")
# print(f"Difference: {difference}")
    
    
    
# Take a string containing only English letters. Using a loop, count vowels (a, e, i, o, u) and consonants; print
# the reversed string using slicing.

# text = input("Enter a string: ")
# vowels_count = 0
# consonants_count = 0
# vowels = "aeiouAEIOU"

# for char in text:
#     if char.isalpha():
#         if char in vowels:
#             vowels_count += 1
#         else:
#             consonants_count += 1

# print(f"Vowels: {vowels_count}")
# print(f"Consonants: {consonants_count}")
# print(f"Reversed: {text[::-1]}")
     
     
     
#      Take a positive integer n. Use nested for loops to print a right-angled star triangle with n rows.
     
#     n = int(input("Enter positive integer n: "))
# for i in range(1, n + 1):
# print("*" * i)


# Take a positive integer n. Use nested loops to print an inverted star triangle with n rows.

# def star():
#     n = int(input("Enter positive integer n: "))
#     for i in range(n, 0, -1):print("*" * i)
        
# star()    


# Take a positive integer n. Use nested loops to print increasing sequences from 1 to the row number.

# def repeated():
#     n = int(input("Enter positive integer n: "))
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(j, end="")
#         print()
# repeated()



# Take a positive integer n. Use nested loops to print each row number repeated that many times.

# def repeated_times():
#     n = int(input("Enter positive integer n: "))
#     for i in range(1, n + 1):
#         print(str(i) * i)
# repeated_times()


# Take the number of products n, then input each product price using a loop and store prices in a list.
# Calculate the total using a loop and count prices greater than 500 taka. Apply discounts: total below 1000
# → 0%; 1000 to below 3000 → 5%; 3000 or above → 10%. Print total, count, discount amount, and final
# bill.

# n = int(input("Number of Products: "))
# prices = []
# for i in range(1, n + 1):
#     p = float(input(f"Price of product {i}: "))
#     prices.append(p)

# total_bill = sum(prices)
# above_500_count = sum(1 for p in prices if p > 500)

# if total_bill < 1000:
#     discount_rate = 0.0
# elif total_bill < 3000:
#     discount_rate = 0.05
# else:
#     discount_rate = 0.10

# discount_amount = total_bill * discount_rate
# final_bill = total_bill - discount_amount

# # Format outputs as integers if they are whole numbers
# print(f"Total Bill: {int(total_bill) if total_bill.is_integer() else total_bill}")
# print(f"Products Above 500: {above_500_count}")
# print(f"Discount: {int(discount_amount) if discount_amount.is_integer() else discount_amount}")
# print(f"Final Bill: {int(final_bill) if final_bill.is_integer() else final_bill}")












