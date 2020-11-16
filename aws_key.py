import os
os.system("clear")
while True:
           # os.system("clear")
            os.system("tput setaf  6")
            print("\t\t\t\t=====================================================")
            os.system("tput setaf  5")
            os.system("tput bold")
            print("\t\t\t\t\t*******Key-pair Automation*******\t\t")
            os.system("tput setaf  2")
            print("\t\t\t\t=====================================================")
            os.system("tput setaf  7")

            print("""
            \n
           \t\t\t\t Press 1 : Create Key pairs
           \t\t\t\t Press 2 : Delete Key pair
           \t\t\t\t Press 3 : Show key pair
           \t\t\t\t Press 4 : Go to Back Menu
            """)
            global key_ch
            key_ch = input("\t\t\t\t\tEnter your Choice: ")
            if int(key_ch) == 1:
                global new_name
                new_name = input("\t\t\t\tEnter name of key: ")
                print("\t\t\t\tCreating Key-pair.......")
                os.system("aws ec2 create-key-pair --key-name {0}".format(new_name))
                print("\t\t\t\tSuccessfully Created key_pair.....")
            elif int(key_ch) == 2:
                global del_name
                del_name = input("\t\t\t\tEnter name of key: ")
                print("\t\t\t\tDeleting Key-pair.....")
                os.system("aws ec2 delete-key-pair --key-name {}".format(del_name))
                print("\t\t\t\tKey-pair deleted successfully.....")
            elif int(key_ch) == 3:
                key_name = input("\t\t\t\tEnter name of key: ")
                os.system("aws ec2 describe-key-pairs --key-name {0}".format(key_name))
            elif int(key_ch) == 4:
                exit()
