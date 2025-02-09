# Example of handling files in Python

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

    
def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "Write successful."
    except Exception as e:
        return f"An error occurred: {e}"

def append_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
        return "Append successful."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
file_path = 'example.txt'
print(write_file(file_path, 'Hello, world!'))
print(append_to_file(file_path, '\nThis is an appended line.'))
print(read_file(file_path))
