import os
os.system("clear")
while True:
                 #os.system("clear")
                 os.system("tput setaf 3")
                 print("\t\t=======================================================================")
                 os.system("tput setaf  2")
                 print("\t\t\t********************Python Automation********************\t\t")
                 os.system("tput setaf  6")
                 print("\t\t=======================================================================")
                 os.system("tput setaf 7")

                 print("""
                 \n
                \t\t\t Press 1 : Container
                \t\t\t Press 2 : Base Machine
                \t\t\t Press 3 : Go to main menu
                 """)
                 global choice
                 print("\t\t\t\t\tWhere you want to launch Python Interpreter ?")
                 choice = input("\t\t\t\t\tEnter your choice: ")
                 if int(choice) == 2:
                    print("\t\t\t\t\tLaunching Python Interpreter....")
                    os.system("python3")
                 elif int(choice) == 1:
                    print("\t\t\t\t\tLaunching Python Interpreter....")
                    con_name = input("\t\t\t\tEnter Container Name: ")
                    image_name = input("\t\t\t\tEnter Image Name: ")
                    port = input("\t\t\t\tEnter Port Number to Expose the WebServer running on the top of Docker: ")
                    os.system('docker run -dit --name {} -p {}:80 {}'.format(con_name , port , image_name))
                    print("\t\t\t\t\tLaunching OS....")
                    os.system('docker exec -it {} yum install python3 -y'.format(con_name))
                    os.system('sudo docker exec -it {} python3'.format(con_name))
                 elif int(choice) == 3:
                    exit()
