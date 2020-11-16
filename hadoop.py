import os
os.system("clear")

def remote_namenode():
    global y
    y = input("Enter ip of name node: ")
    print("Configuring Name Node...")
    os.system("ssh {0} rpm -ivh jdk-8u171-linux-x64.rpm".format(y))
    os.system("ssh {0} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(y))
    os.system("ansible-playbook nn1.yml")
    os.system("ssh {0} hadoop namenode -format".format(y))
def base_namenode():
    print("Configuring Name Node...")
    os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
    os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
    os.system("ansible-playbook nn.yml")
    os.system("hadoop namenode -format")
def remote_datanode():
    global y1
    y1 = input("Enter ip of data node: ")
    print("Configuring Data Node...")
    os.system("ssh {0} rpm -ivh jdk-8u171-linux-x64.rpm".format(y1))
    os.system("ssh {0} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(y1))
    os.system("ansible-playbook dn1.yml")
def base_datanode():
    print("Configuring Data Node...")
    os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
    os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
    os.system("ansible-playbook dn.yml")
while True:
                # os.system("clear")
                 os.system("tput setaf  3")
                 print("\t\t==============================================================")
                 os.system("tput setaf  3")
                 os.system("tput bold")
                 print("\t\t\t\t*******Hadoop Automation*******\t\t")
                 os.system("tput setaf  6")
                 print("\t\t==============================================================")
                 os.system("tput setaf  7")

                 print("""
                 \n
                \t\t Press 1 : Configure Namenode
                \t\t Press 2 : Start Namenode
                \t\t Press 3 : Configure Datanode
                \t\t Press 4 : Start Datanode
                \t\t Press 5 : Configure Client Node
                \t\t Press 6 : Go back to main menu
                 """)
                 global choice1
                 choice1 = input("\t\t\t\tEnter your choice: ")
                 if int(choice1) == 1:
                    global s3
                    s3 = input("\t\t\tDo you want to configure this system as name node? (y/n): ")
                    if s3 == 'n':
                       remote_namenode()
                    elif s3 == 'y':
                        base_namenode()
                 elif int(choice1) == 2:
                    global s13
                    s13 = input("\t\t\tIs your name node in base machine or remote machine? (base/remote): ")
                    if s13 == "base":
                        os.system("hadoop-daemon.sh start namenode")
                        os.system("jps")
                        os.system("hadoop dfsadmin -report")
                    elif s13 == "remote":
                        os.system("ssh {0} hadoop-daemon.sh start namenode".format(y))
                        os.system("ssh {0} jps".format(y))
                        os.system("ssh {} hadoop dfsadmin -report".format(y))
                 elif int(choice1) == 3:
                    global s4
                    s4 = input("\t\t\tDo you want to configure this system as data node? (y/n): ")
                    if s4 == 'n':
                        remote_datanode()
                    elif s4 == 'y':
                        base_datanode()
                 elif int(choice1) == 4:
                    global s14
                    s14 = input("\t\t\tIs your data  node in base machine or remote machine? (base/remote): ")
                    if s14 == "base":
                        os.system("hadoop-daemon.sh start datanode")
                        os.system("jps")
                        os.system("hadoop dfsadmin -report")
                    elif s14 == "remote":
                        y1 = input("Enter ip of data node: ")
                        os.system("ssh {0} hadoop-daemon.sh start datanode".format(y1))
                        os.system("ssh {0} jps".format(y1))
                        os.system("ssh {} hadoop dfsadmin -report".format(y1))
                 elif int(choice1) == 5:
                    ip = input("\t\t\t\tEnter your Client node ip: ")
                    os.system("ssh {} rpm -ivh jdk-8u171-linux-x64.rpm".format(ip))
                    os.system("ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip))
                    os.system("ansible-playbook client.yml")
                    os.system("ssh {} hadoop dfsadmin -report".format(ip))
                 elif int(choice1) == 6:
                     exit()

