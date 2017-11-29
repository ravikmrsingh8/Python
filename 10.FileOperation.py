text = "Some Text to write on File"
file = open('NewFile.txt', 'w')  # Write Mode , Append Mode
print(type(file))
file.write(text)
file.close()


file = open('NewFile.txt', 'r')
print(type(file))
file_data = file.read()

print(file_data)
file.close()

