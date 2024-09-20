# stock prices of abc corp [day1, day2, day3, ...]
stock_prices = [290, 333, 444, 567, 678]

# what was the price on day 3?
day_3_price = stock_prices[2]
print(day_3_price)
# look up by index, big o complexity order of 1 O(1)

# on what day price was 567?
for i in range(len(stock_prices)):
    if stock_prices[i]==567:
        print(i)

# complexity for above program will be O(n), have to do n number iterations to find a value, if the length of the list increases the time taken to find the value will aslo increase.

# Insert a new price 300 at index 1
stock_prices.insert(1, 289)


# ///////////////Home work///////////////////////

print("///////////////month_expense///////////////////////")

month_expense = [2200, 2350, 2600, 2130, 2190]

# In Feb, how many dollars you spent extra compare to January?
extra_expense_in_feb = month_expense[1] - month_expense[0]
print(extra_expense_in_feb)

# Find out your total expense in first quarter (first three months) of the year.
print(sum(month_expense) - month_expense[4])

# Find out if you spent exactly 2000 dollars in any month
print(2000 in month_expense)

# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
month_expense.append(1980)
print(month_expense)

# You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
month_expense[3] = month_expense[3] - 200
print(month_expense)

print("///////////////heros///////////////////////")

heros=['spider man','thor','hulk','iron man','captain america']

# Length of the list
print(len(heros))

# Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)

#  You realize that you need to add 'black panther' after 'hulk',   so remove it from the list first and then add it after 'hulk'
heros.pop(5)
heros.insert(3, "black panther")

# Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.
heros[1:3] = ['doctor strange']

print(heros)