from sys import argv

script,filename=argv

txt=open(filename) #import the file, basically

print(f"Here's your file {filename}:")
print(txt.read()) #actually reads the file

print("Type the filename again:")
file_again=input("> ")

txt_again=open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()
# running: python3.6 ex15.py test.txt
