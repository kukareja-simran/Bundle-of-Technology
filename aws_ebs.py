import os
os.system("clear")
while True:
           # os.system("clear")
            os.system("tput setaf  6")
            print("\t\t\t\t================================================================")
            os.system("tput setaf  5")
            os.system("tput bold")
            print("\t\t\t\t\t*******Elastic Block Volume (EBS) Automation*******\t\t")
            os.system("tput setaf  2")
            print("\t\t\t\t================================================================")
            os.system("tput setaf  7")

            print("""
            \n
           \t\t\t\t Press 1 : To Create new Volume
           \t\t\t\t Press 2 : Attach Volume to Specific Instance
           \t\t\t\t Press 3 : Dettach Volume
           \t\t\t\t Press 4 : Delete Volume
           \t\t\t\t Press 5 : Show Volumes
           \t\t\t\t Press 6 : Mount and Partition
           \t\t\t\t Press 7 : Go to Back menu
            """)
            vol_ch = input("\t\t\t\t\tEnter your Choice: ")
            if int(vol_ch) == 1:
                az = input("\t\t\t\t\tEnter Availablity Zone to Create EBS Volume: ")
                ebs_size = input("\t\t\t\t\tEnter Size to create EBS Volume: ")
                print("\t\t\t\t\tCreating New Volume ....")
                os.system('aws ec2 create-volume --availability-zone {} --size {}'.format(az , ebs_size))
                print("\t\t\t\t\tNew Volume Created Successfully....")
            elif int(vol_ch) == 2:
                ebs_vid = input("\t\t\t\t\tEnter EBS Volume ID to Attach to EC2 Instance: ")
                ec2_id = input("\t\t\t\t\tEnter EC2 Instance ID to attach EBS Volume: ")
                print("\t\t\t\t\tAttaching Volume to instance.....")
                os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(ebs_vid , ec2_id))
                print("\t\t\t\t\tSuccessfully Volume attached to the instance.......") 
            elif int(vol_ch) == 3:
                v_id = input("\t\t\t\t\tEnter volume id: ")
                print("\t\t\t\t\tDetaching Volume.......")
                os.system("aws ec2 detach-volume --volume-id {}".format(v_id))
                print("\t\t\t\t\tVolume Dettached Successfully.....")
            elif int(vol_ch) == 4:
                 v_id = input("\t\t\t\t\tEnter volume id: ")
                 print("\t\t\t\t\tDeleting Volume....")
                 os.system("aws ec2 delete-volume --volume-id {}".format(v_id))
                 print("\t\t\t\t\tSuccessfully deleted Volume...")
            elif int(vol_ch) == 5:
                os.system("aws ec2  describe-volumes")
            elif int(vol_ch) == 6:
               ip = input("\t\t\t\t\tEnter Public IP of EC2: ")
               ky = input("\t\t\t\t\tEnter Private Key Name For Login Into EC2 : ")
               os.system('ssh -l ec2-user {} -i {}.pem sudo fdisk -l'.format(ip , ky))
               na = input("\n\t\t\t\t\tEnter Partition Name: ")
               nb = input("\t\t\t\t\tEnter directory name: ") 
               os.system("ssh -l ec2-user {} -i {}.pem sudo mkdir {}".format(ip,ky,nb))
               os.system('ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 {}'.format(ip , ky , na))
               os.system('ssh -l ec2-user {} -i {}.pem sudo mount {}  {}'.format(ip , ky , na,nb))
               os.system('ssh -l ec2-user {} -i {}.pem sudo df -hT'.format(ip , ky))
            elif int(vol_ch) == 7:
                exit()
