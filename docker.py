import os

#os.system("yum install docker-ce --nobest -y")
os.system("systemctl start docker")
os.system("clear")
while True:
    #os.system("clear")
    os.system("tput setaf 3")
    print("\t\t=======================================================================")
    os.system("tput setaf  2")
    print("\t\t\t********************Docker Automation********************\t\t")
    os.system("tput setaf  6")
    print("\t\t=======================================================================")
    os.system("tput setaf 7")
    print("""
    \n
    \t\t\t\t Press 1  : Pull image from Docker hub
    \t\t\t\t Press 2  : Launch new Container
    \t\t\t\t Press 3  : Show all Container
    \t\t\t\t Press 4  : Remove Container
    \t\t\t\t Press 5  : Show all images
    \t\t\t\t Press 6  : Info of Docker
    \t\t\t\t Press 7  : Configure webserver inside the container
    \t\t\t\t Press 8  : Start container
    \t\t\t\t Press 9  : Stop Container
    \t\t\t\t Press 10 : Go back to main menu
    """)
    d_ch = input("\t\t\t\tEnter your Choice: ")
    if int(d_ch) == 1:
        image_name = input("\t\t\t\tEnter name of Image: ")
        print("\t\t\t\tImage Downloading....")
        os.system("docker pull {}".format(image_name))
        print("\t\t\t\tImage Sucessfully downloaded....")
    elif int(d_ch) == 2:
        value=input("\t\t\t\tEnter Container Name: ")
        image=input("\t\t\t\tEnter Image Name: ")
        print("\t\t\t\tLaunching New OS......")
        os.system("docker run -dit --name {} {}".format(value, image))
        print("\t\t\t\tNew OS Launched Successfully")
    elif int(d_ch) == 3:
        os.system("docker ps -a")
    elif int(d_ch) == 4:
        value=input("\t\t\t\tEnter name to remove docker Container: ")
        print("\t\t\t\tRemoving Container....")
        os.system("docker rm -f {}".format(value))
        print("\t\t\t\tContainer Removed Successfully....")
    elif int(d_ch) == 5:
        os.system("docker images")
    elif int(d_ch) == 6:
        os.system("\t\t\t\tInformation of Docker....")
        os.system("docker info")
    elif int(d_ch) == 7:
        con_name = input("\t\t\t\tEnter Container Name: ")
        image_name = input("\t\t\t\tEnter Image Name: ")
        port = input("\t\t\t\tEnter Port Number to Expose the WebServer running on the top of Docker: ")
        print("\t\t\t\tConfiguring Webserver.....")
        os.system('docker run -dit --name {} -p {}:80 {}'.format(con_name , port , image_name))
        os.system('docker exec -it {} yum install httpd -y'.format(con_name))
        os.system('sudo docker cp /root/my-workspace-main/index.html {}:/var/www/html/'.format(con_name))
        os.system('sudo docker exec -it {} /usr/sbin/httpd'.format(con_name))
        print("\t\t\t\tWebserver Configured Successfully....")
    elif int(d_ch) == 8:
        c_name = input("\t\t\t\tEnter name of container: ")
        print("\t\t\t\tStarting Container....")
        os.system("docker start {}".format(c_name))
        print("\t\t\t\tContainer Started Sucessfully...")
    elif int(d_ch) == 9:
        c_name = input("\t\t\t\tEnter name of container: ")
        print("\t\t\t\tStopping Container....")
        os.system("docker stop {}".format(c_name))
        print("\t\t\t\tContainer Stopped successfully....")
    elif int(d_ch) == 10:
        os.system("clear")
        exit()
