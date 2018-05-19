numbers=[]

def loop(i):
    while i<6:
        print(f"At the top i is {i}") # just an indicator for how the loop goes
        numbers.append(i) # adds i to the list

        i+=1
        print("Numbers now: ",numbers)
        print(f"At the bottom i is {i}") # just an indicator for how the loop goes

    print("The numbers: ")

    for num in numbers:
        print(num) # printing all the list elements

loop(0) # put any numbers in here
