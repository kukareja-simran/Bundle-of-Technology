import os
os.system("clear")
while True:
                 #os.system("clear")
                 os.system("tput setaf 3")
                 print("\t\t=============================================================================")
                 os.system("tput setaf  2")
                 print("\t\t\t********************Search Algorithm Automation********************\t\t")
                 os.system("tput setaf  6")
                 print("\t\t=============================================================================")
                 os.system("tput setaf 7")

                 print("""
                 \n
                 \t\t\t Press 1 : Linear Search
                 \t\t\t Press 2 : Binary Search
                 \t\t\t Press 3 : Go back to main menu
                 """)
                 sh_ch = input("\t\t\t\t\tEnter your choice: ")
                 if int(sh_ch) == 1:
                     print("\n\t\t\t\t\tThis is Basic application of Student Database.\n\t\t\t\t\tHere information of student is retrieving using Linear search")
                     os.system("python3 Linear_search.py")
                 elif int(sh_ch) == 2:
                     print("\n\t\t\t\t\tThis is Basic application of US Election Database.\n\t\t\t\t\tHere information of student is retrieving using Binary search")
                     os.system("python3 Binary_search.py")
                 elif int(sh_ch) == 3:
                     exit()

