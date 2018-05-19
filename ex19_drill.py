amount_of_cheese=int(input("How many cheeses? "))
amount_of_crackers=int(input("How many crackers? "))
# converting input string to integer for calculation

total=amount_of_cheese+amount_of_crackers
# define variable 'total' before defining the function

def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"{cheese_count} cheeses, {boxes_of_crackers} crackers, {total} things in total.")

cheese_and_crackers(amount_of_cheese,amount_of_crackers)
