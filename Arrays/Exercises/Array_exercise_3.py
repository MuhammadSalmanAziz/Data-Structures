# Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

max_number = int(input("Enter the Max Number : "))
odd_numbers = []

for i in range(1,max_number):
    if i%2 == 1:
        odd_numbers.append(i)
print("Odd Numbers : ",odd_numbers)