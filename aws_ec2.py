import os
os.system("clear")
while True:
            #os.system("clear")
            os.system("tput setaf  6")
            print("\t\t\t\t==========================================================")
            os.system("tput setaf  5")
            os.system("tput bold")
            print("\t\t\t\t\t*******Elastic Cloud (EC2) Automation*******\t\t")
            os.system("tput setaf  2")
            print("\t\t\t\t==========================================================")
            os.system("tput setaf  7")

            print("""
            \n
            \t\t\t\t Press 1 : Create New EC2 Instance
            \t\t\t\t Press 2 : Start Specific Instance
            \t\t\t\t Press 3 : Stop Instance
            \t\t\t\t Press 4 : Terminate Instance
            \t\t\t\t Press 5 : Show all instances
            \t\t\t\t Press 6 : Go to back menu
            """)
            global ec2_ch
            ec2_ch = input("\t\t\t\t\tEnter your choice: ")
            if int(ec2_ch) == 1:
                ami = input("\t\t\t\t\tEnter AMI id to Launch Instance: ")
                instance_type = input("\t\t\t\t\tEnter Instance type: ")
                count = input("\t\t\t\t\tEnter Number of Instances to launch: ")
                subnet_id = input("\t\t\t\t\tEnter Subnet id: ")
                sg_id1 = input("\t\t\t\t\tEnter Security Group Id to attach to the Instance: ")
                key = input("\t\t\t\t\tEnter Key to attach to ec2 Instance: ")
                print("\t\t\t\t\tLaunching New EC2 Instance.....")
                os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}'.format(ami , instance_type , count ,subnet_id, sg_id1 , key))
                print("\t\t\t\t\tInstance launched Successfully......")
            elif int(ec2_ch) == 3:
                id = input("\t\t\t\t\tEnter Instance id to stop Ec2 instances: ")
                print("\t\t\t\t\tStopping Instance.......")
                os.system("aws ec2 stop-instances --instance-ids {}".format(id))
                print("\t\t\t\t\tInsatnce stopped Successfully....")
            elif int(ec2_ch) == 2:
                id = input("\t\t\t\t\tEnter Instance id to start Ec2 instances: ")
                print("\t\t\t\t\tStarting Instance.....")
                os.system("aws ec2 start-instances --instance-ids {}".format(id))
                print("\t\t\t\t\tInstance Started successfully......")
            elif int(ec2_ch) == 4:
                id = input("\t\t\t\t\tEnter Instance id to terminate Ec2 instances: ")
                print("\t\t\t\t\tTerminating instance...")
                os.system("aws ec2 terminate-instances --instance-ids {}".format(id))
                print("\t\t\t\t\tInstance terminated successfully.....")
            elif int(ec2_ch) == 5:
                print("\t\t\t\t\tShowing Instances....")
                os.system("aws ec2 describe-instances")
            elif int(ec2_ch) == 6:
                exit()
