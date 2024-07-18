import random
import shutil

def write_file(file_name, line_length=1000): # modify the line length to generate number of lines needed.
    with open(file_name, 'w') as file:
        for i in range(10000): # modify the number to generate the number of characters needed in a single line of the file.
            for x in range(line_length):
                line_content = str(random.randint(0, 1))
                file.write(''+line_content)
            file.write('\n')

def multiply(file_name, dst_file, number):
    for i in range(number):
        shutil.copy(file_name, dst_file+str(i)+'.txt')
    
def main():
    file = "/users/USERNAME/documents/test.py"
    newfile = "/users/USERNAME/desktop/test"
    # set the 'USERNAME' above to whatever the user you are logged in on for mac
    write_file(file)
    multiply(file, newfile, 100000000000000000000000000000000) # modify this number to modify the number of copies generated.

if __name__ == "__main__":
    main()
