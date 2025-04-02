#client
import sys                              # to read input from command line
import client_lib                       #uses helper functions for the file operations
from datetime import datetime           #generates unique client id using timestamps 
from time import gmtime, strftime       #string format time

def main():

    print ("\n")
    client_lib.instructions()                               #for printing usage instructions
    client_id = strftime("%Y%m%d%H%M%S", gmtime())          #gmtime is used here to avoid localtime conflicts, as returns the current UTC (Coordinated Universal Time) time instead of the local system time.
    file_version_map = {}

    while True:
        
        client_input = sys.stdin.readline() #waits for user command (<write>, <read>, <list>, <quit>)
            
        if "<write>" in client_input:
            while not client_lib.check_valid_input(client_input):                        # error check the input
                 client_input = sys.stdin.readline()
            
            filename = client_input.split()[1]                                           # get the filename from the input
            response = client_lib.handle_write(filename, client_id, file_version_map)    # handle the write request
            if response == False:
                print("File unlock polling timeout...")
                print("Try again later...")
            print ("Exiting <write> mode...\n")
            

        elif "<read>" in client_input:
            while not client_lib.check_valid_input(client_input):                        # error check the input
                 client_input = sys.stdin.readline()

            filename = client_input.split()[1]                                           # get file name from the input
            client_lib.handle_read(filename, file_version_map, client_id)                # handle the read request 
            print("Exiting <read> mode...\n")
        
        elif "<list>" in client_input:
            client_socket = client_lib.create_socket()
            client_lib.send_directory_service(client_socket," ",'w', True)
            client_socket.close()

        #elif "<create>" in client_input:
        #    while not client_lib.check_valid_input(client_input):       # error check the input
        #         client_input = sys.stdin.readline()
        #    filename = client_input.split()[1]
        #    client_lib.create_file(filename)

        elif "<instructions>" in client_input:
            client_lib.instructions()


        elif "<quit>" in client_input:
            print("Exiting application...")
            sys.exit()

        elif "<end>" in client_input:
            print("first do a <write> operation ...")

        else :
            print("Invalid Input !! Enter the commands from the given menu only.")
            client_lib.instructions()
if __name__ == "__main__":
    main()