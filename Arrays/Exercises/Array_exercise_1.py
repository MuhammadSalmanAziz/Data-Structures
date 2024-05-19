#/Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190
#Create a list to store these monthly expenses and using that find out

monthly_expenses = [2200 , 2350, 2600 , 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
extra_dollar_in_feb = monthly_expenses[1] - monthly_expenses[0]
print("Extra Dollars spent in Febraury as compare to January are :",extra_dollar_in_feb )

# 2. Find out your total expense in first quarter (first three months) of the year.

first_quarter_expense = monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]
print("First quarter expense is : ",first_quarter_expense)

# 3. Find out if you spent exactly 2000 dollars in any month

print("Did I spent 2000$ in any month? ", 2000 in monthly_expenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

monthly_expenses.append(1980)
print(monthly_expenses)

# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
monthly_expenses[3] = monthly_expenses[3] - 200

print(monthly_expenses)