import csv  # To work with CSV file
from socket import *

serverPort = 9090
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(10)
print('DIRECTORY SERVICE is ready to receive...')

def check_mappings(client_msg, list_files):  # This function checks a file-mapping CSV file to determine whether a file exists and where it is stored.
    if '|' not in client_msg:
        pass
    else:
        filename = client_msg.split('|')[0]
        print("Filename from client message: " + filename)
        RW = client_msg.split('|')[1]

    file_row = ""
    with open(r"C:\Users\abhis\Desktop\pbl\file_mappings.csv", 'rt') as infile:  # Open the .csv file storing the mappings
        d_reader = csv.DictReader(infile, delimiter=',')  # Read file as a CSV file, taking values after commas
        header = d_reader.fieldnames  # Skip header of CSV file

        for row in d_reader:
            if not list_files:  # Check if we are not listing files (checking for file existence)
                user_filename = row['user_filename']
                primary_copy = row['primary']

                if user_filename == filename and RW == 'a+':  # Check if file inputted by the user exists (for write)
                    print("WRITING")
                    actual_filename = row['actual_filename']  # Get actual filename (eg. file123.txt)
                    server_addr = row['server_addr']  # Get the file's file server IP address
                    server_port = row['server_port']  # Get the file's file server PORT number

                    print(f"actual_filename: {actual_filename}")
                    print(f"server_addr: {server_addr}")
                    print(f"server_port: {server_port}")

                    return actual_filename + "|" + server_addr + "|" + server_port  # Return string with the file's information

                elif user_filename == filename and RW == 'r' and primary_copy == 'no':  # For read request and if primary copy is 'no'
                    print("READING")
                    actual_filename = row['actual_filename']  # Get actual filename (eg. file123.txt)
                    server_addr = row['server_addr']  # Get the file's file server IP address
                    server_port = row['server_port']  # Get the file's file server PORT number

                    print(f"actual_filename: {actual_filename}")
                    print(f"server_addr: {server_addr}")
                    print(f"server_port: {server_port}")

                    return actual_filename + "|" + server_addr + "|" + server_port  # Return string with the file's information

            else:  # List all existing files
                user_filename = row['user_filename']
                file_row = file_row + user_filename + "\n"  # Append filename to return string

        if list_files:  # If listing files, return the list of unique filenames
            file_row = "\n".join(sorted(set(file_row.splitlines())))  # Remove duplicates and sort the list
            return file_row

    return None  # If file does not exist return None

def main():
    while 1:
        connectionSocket, addr = serverSocket.accept()

        recv_msg = connectionSocket.recv(1024)
        recv_msg = recv_msg.decode()
        response = ""

        if "LIST" not in recv_msg:
            response = check_mappings(recv_msg, False)  # Check the mappings for the file
        elif "LIST" in recv_msg:
            response = check_mappings(recv_msg, True)  # List the files

        if response is not None:  # If file exists or files are listed
            response = str(response)
            print("RESPONSE: \n" + response)
            print("\n")
        else:
            response = "FILE_DOES_NOT_EXIST"
            print("RESPONSE: \n" + response)
            print("\n")

        connectionSocket.send(response.encode())  # Send the file information or non-existence message to the client
        connectionSocket.close()

if __name__ == "__main__":
    main()