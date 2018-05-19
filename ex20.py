from sys import argv

script,input_file=argv

def print_all(f):
    print(f.read()) # print the file

def rewind(f):
    f.seek(0) # goes back to the start of the file

def print_a_line(line_count,f):
    print(line_count,f.readline()) # read *A* line

current_file=open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape")

rewind(current_file)

print("Let's print three lines:")

current_line=1
print_a_line(current_line,current_file)
# automatically goes to the next line after function is called

current_line+=1 # add one to the variable 'current_file'
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)
