import os
os.system("clear")
while True:
           # os.system("clear")
            os.system("tput setaf  6")
            print("\t\t\t\t==========================================================")
            os.system("tput setaf  5")
            os.system("tput bold")
            print("\t\t\t\t\t*******Security Group Automation*******\t\t")
            os.system("tput setaf  2")
            print("\t\t\t\t==========================================================")
            os.system("tput setaf  7")

            print("""
            \n
           \t\t\t\t Press 1 : Create new security group
           \t\t\t\t Press 2 : Delete Security group
           \t\t\t\t Press 3 : Add Ingress Rules
           \t\t\t\t Press 4 : Show Security Groups
           \t\t\t\t Press 5 : Go to Back Menu
            """)
            global sg_ch1
            sg_ch1 = input("\t\t\t\t\tEnter your choice: ")
            if int(sg_ch1) == 1:
                sg_name = input("\t\t\t\t\tEnter Security group Name: ")
                sg_des = input("\t\t\t\t\tEnter Security group description: ")
                print("\t\t\t\t\tCreating New Security group....")
                os.system("aws ec2 create-security-group --group-name {0} --description {1}".format(sg_name,sg_des))
                print("\t\t\t\t\tSuccessfully created security group....")
            elif int(sg_ch1) == 2:
                sg_id=input("\t\t\t\t\tEnter Security group id you want to delete:  ")
                print("\t\t\t\t\tDeleting Security group...")
                os.system("aws ec2 delete-security-group --group-id {}".format(sg_id))
                print("\t\t\t\t\tSuccessfully deleted Security group....")
            elif int(sg_ch1) == 3:
                sg_id = input("\t\t\t\t\tEnter Security Group ID : ")
                ip_protocol = input("\t\t\t\t\tEnter IP Protocol: ")
                port_no = input("\t\t\t\t\tEnter Port No: ")
                cidr=input("\t\t\t\t\tInput Ip Ranges : ")
                print("\t\t\t\t\tAuthorizing Security group....")
                os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(sg_id , ip_protocol , port_no , cidr))
                print("\t\t\t\t\tSucessfully authorize security group...")
            elif int(sg_ch1) == 4:
                sg_id2 = input("\t\t\t\t\tEnter group id : ")
                sg_name1 = input("\t\t\t\t\tEnter name of Security Group: ")
                os.system("aws ec2 describe-security-groups --group-ids {} --group-names {}".format(sg_id2,sg_name1))
            elif int(sg_ch1) == 5:
                exit()
