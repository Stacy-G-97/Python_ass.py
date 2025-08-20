# Ask user for filename
filename = input("Enter the file name: ")

try:
    # Open and read file
    with open(filename, "r") as file:
        content = file.read()

    # Modify content (example: uppercase)
    modified_content = content.upper()

    # Write to a new file
    with open("newFile.txt", "w") as new_file:
        new_file.write(modified_content)

    print("File has been read and modified into 'newFile.txt'.")

except FileNotFoundError:
    print("File not found, please check filename.")
except PermissionError:
    print("You don’t have permission to read this file.")
