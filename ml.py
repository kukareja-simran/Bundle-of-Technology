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
                 \t\t Press 1 : Predict Salary from experience
                 \t\t Press 2 : Go back to main menu
                 """)
                 ml_ch = input("\t\t\t\tEnter your Choice: ")
                 if int(ml_ch) == 1:
                    os.system("python3 salary.py")
                    os.system("python3 salary_code.py")
                 elif int(ml_ch) == 2:
                     exit()

