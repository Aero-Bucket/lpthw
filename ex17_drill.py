from sys import argv
script,from_file,to_file=argv
open(to_file,'w').write(open(from_file).read())
# writing the opened to_file using the opened from_file
# running: python3.6 ex17_drill.py test.txt new_file.txt
