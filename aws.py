import os
os.system("clear")
while True:
    #os.system("clear")
    os.system("tput setaf 3")
    print("\t\t=======================================================================")
    os.system("tput setaf  2")
    print("\t\t\t********************AWS Automation********************\t\t")
    os.system("tput setaf  6")
    print("\t\t=======================================================================")
    os.system("tput setaf 7")
    print("""
            \n
           \t\t\t\t Press 1 : key pair
           \t\t\t\t Press 2 : Security group
           \t\t\t\t Press 3 : EC2 instance
           \t\t\t\t Press 4 : S3 bucket
           \t\t\t\t Press 5 : EBS Volume
           \t\t\t\t Press 6 : Go to Main Menu
            """)
    global aws_choice
    aws_choice = input("\t\t\t\tEnter Your Choice: ")
    if int(aws_choice) == 1:
        os.system("python3 aws_key.py")
    elif int(aws_choice) == 2:
        os.system("python3 aws_sg.py")
    elif int(aws_choice) == 3:
        os.system("python3 aws_ec2.py")
    elif int(aws_choice) == 4:
        os.system("python3 aws_s3.py")
    elif int(aws_choice) == 5:
        os.system("python3 aws_ebs.py")
    elif int(aws_choice) == 6:
        exit()
