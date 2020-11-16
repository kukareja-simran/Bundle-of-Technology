import os
os.system("clear")
remote_ip=input("\t\t\t\t\tEnter remote OS IP: ")
while True:
                #os.system("clear")
                os.system("tput setaf 3")
                print("\t\t=======================================================================")
                os.system("tput setaf  2")
                print("\t\t\t********************Linux Automation********************\t\t")
                os.system("tput setaf  6")
                print("\t\t=======================================================================")
                os.system("tput setaf 7")

                print("""
                \n
                \t\t\t Press 1 : Date
                \t\t\t Press 2 : Calender
                \t\t\t Press 3 : Linux Command
                \t\t\t Press 4 : Configure WebServer
                \t\t\t Press 5 : Parition
                \t\t\t Press 6 : Go back to main Menu
                """)
                cmd2=input("\t\t\t\t\tEnter your Choice: ")

                if cmd2=='1':
                    os.system("ssh {} date".format(remote_ip))

                elif cmd2=='2':
                    os.system('ssh {} cal'.format(remote_ip))

                elif cmd2=='3':
                    linux_cmd = input('Enter Linux Command :-   ')
                    os.system('ssh {} {}'.format(remote_ip ,linux_cmd))

                elif cmd2=='4':
                    os.system('ssh {} yum install httpd -y'.format(remote_ip))
                    os.system('ssh {} systemctl start httpd'.format(remote_ip))
                    os.system('ssh {} systemctl start httpd'.format(remote_ip))
                    os.system('scp index.html {}:/var/www/html'.format(remote_ip))
                    os.system("ssh {} systemctl stop firewalld".format(remote_ip))
                    os.system("ssh {} setenforce 0".format(remote_ip))

                elif cmd2=='5':
                    os.system('ssh {} fdisk -l'.format(remote_ip))
                    hd_name = input("Enter the name of Hard Disk: ")
                    os.system('ssh {} fdisk {}'.format(remote_ip,hd_name))
                    os.system('ssh {} mkfs.ext4 {}'.format(remote_ip,hd_name))
                    dirname = input('Enter name of Directory to mount the HDs:')
                    os.system('ssh {} mkdir {}'.format(remote_ip , dirname))
                    os.system('ssh {} mount {} {}'.format(remote_ip ,hd_name, dirname))
                    os.system('ssh {} df -h'.format(remote_ip))
                elif cmd2=='6':
                    exit()

                else:
                    print('Select options as mention')

