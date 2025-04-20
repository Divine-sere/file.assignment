def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile read successfully!")
    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
        return
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
        return
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Write to a new file
    new_filename = f"modified_{filename}"
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"\nModified content written to '{new_filename}' successfully!")
    except Exception as e:
        print(f"❌ Error writing to the new file: {e}")

if __name__ == "__main__":
    main()
