try:
    file = open('Argument.txt')
    for line in file:
        print(line, end='')
except IOError:
    print("Couldn't Open Argument.txt file")
finally:
    if 'file' in locals():
        file.close()
