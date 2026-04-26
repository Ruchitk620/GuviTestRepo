
# --------- question 1 ----------------

list = [10, 501, 22, 37, 100, 999, 87, 351]
even=[]
odd=[]

for i in list:  #Loop for each number in lsit
    if i % 2 == 0:    #check if even
        even.append(i)
    else:
        odd.append(i)

print("Even numers:",even)  # print the result
print("Odd nummbers:",odd)

#-------------- Question 2 ------------------
prime = []

for j in list: #Loop for each number in lsit
    if j > 1:
        is_prime = True

        for k in range(2,j):
            if j % k == 0:  # Check divisibility
                is_prime= False
                break
        if is_prime:  # If still prime, add to list
            prime.append(j)

print("Prime numbers are:",prime)
print("Count of prime numbers:",len(prime))


#------------- Question 3 -----------------
happy = []

for i in list:  #Loop for each number in lsit
    n = i
    seen = []

    while n != 1 and n not in seen:  # Process to check happy number
        seen.append(n)

        sum_sq = 0
        while n > 0:
            digit = n % 10
            sum_sq = sum_sq + digit * digit 
            n = n // 10

        n = sum_sq

    if n == 1:
        happy.append(i)

print("Happy numbers",happy)
print("Count of happy numbers:",len(happy))


# -------------question 4 -------------
num = int(input("Enter the number")) # Take input from user

# Store original number
real_num = num

last_digit = num % 10  # last digit

# Get first digit
while num >= 10:
    num = num // 10

first_digit = num

total = first_digit + last_digit

print("First digit:", first_digit)
print("Last digit:", last_digit)
print("Sum of first and last digit:",total)



# -------------- Question 5 ------------
# Target amount
amount = 10

# Loop for each coin
for one in range(0, 11):        # 1 coin
    for two in range(0, 6):     # 2 coin
        for five in range(0, 3): # 5 coin
            for ten in range(0, 2): # 10 coin

                total = (1 * one) + (2 * two) + (5 * five) + (10 * ten)

                if total == amount:
                    print("1₹:", one, "2₹:", two, "5₹:", five, "10₹:", ten)




# -------------- Question 6 -------------
# Given lists
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
list3 = [40, 30, 70, 80]

duplicates = []

# Loop through first list
for num in list1:
    if num in list2 and num in list3:
        duplicates.append(num)

# Print result
print("Duplicates in all 3 lists:", duplicates)




#------------- Question 7 ---------------
# Given list
numbers = [1, 2, 2, 3, 1, 4]

# Loop through each element
for num in numbers:
    count = 0

    # Count occurrences
    for i in numbers:
        if num == i:
            count += 1

    # Check if non-repeating
    if count == 1:
        print("First non-repeating element:", num)
        break



# --------------- Question 8 ----------------
# Given list
numbers = [4, 5, 6, 1, 2, 3]

# Assume first element is minimum
minimum = numbers[0]

# Loop through list
for num in numbers:
    if num < minimum:
        minimum = num

# Print result
print("Minimum element:", minimum)


#-------------- Question 9 ------------------
# Given list and target
numbers = [10, 20, 30, 9]
target = 59

found = False

# Loop through all combinations
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):

            total = numbers[i] + numbers[j] + numbers[k]

            if total == target:
                print("Triplet found:", numbers[i], numbers[j], numbers[k])
                found = True

# If no triplet found
if not found:
    print("No triplet found")




#-------------- Question 10 ------------------
# Given list
numbers = [4, 2, -3, 1, 6]

found = False

# Outer loop → starting point
for i in range(len(numbers)):
    total = 0

    # Inner loop → continuous elements
    for j in range(i, len(numbers)):
        total = total + numbers[j]

        # If sum becomes 0
        if total == 0:
            print("Sublist with sum 0:", numbers[i:j+1])
            found = True
            break

    if found:
        break

# If not found
if not found:
    print("No sublist with sum 0")
