def write_file(file_name, file_content):
    #Add the .txt extension
    #Open the file in write mode and write the content
    with open(f'{file_name}.txt', 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    #Add the .txt extension
    #Open the file in append mode and append the content
    with open(f'{file_name}.txt', 'a') as file:
        file.write(append_content)
    

def read_file(file_name):
    #Add the .txt extension
    #Open file in read mode and return the content
    with open(f'{file_name}.txt', 'r') as file:
        return file.read()
