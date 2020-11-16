import os
os.system("clear")
while True:
            #os.system("clear")
            os.system("tput setaf  6")
            print("\t\t\t\t==========================================================")
            os.system("tput setaf  5")
            os.system("tput bold")
            print("\t\t\t\t\t*******Storage(S3) Automation*******\t\t")
            os.system("tput setaf  2")
            print("\t\t\t\t==========================================================")
            os.system("tput setaf  7")

            print("""
            \n
            \t\t\t\t Press 1 : Create New S3 Bucket
            \t\t\t\t Press 2 : Delete S3 bucket
            \t\t\t\t Press 3 : Upload object in S3 bucket
            \t\t\t\t Press 4 : Delete object in S3 bucket
            \t\t\t\t Press 5 : Delete S3 bucket
            \t\t\t\t Press 6 : Go back to main menu
            """)
            bucket_ch = input("\t\t\t\t\tEnter your Choice: ")
            if int(bucket_ch) == 1:
                s3_name = input("\t\t\t\t\tEnter S3 bucket name that must be unique: ")
                #region = input("\t\t\t\t\tEnter name of region: ")
                print("\t\t\t\t\tCreating S3 Bucket.....")
                os.system('aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1'.format(s3_name))
                print("\t\t\t\t\tS3 bucket created successfully....")
            elif int(bucket_ch) == 2:
                s3_name = input("\t\t\t\t\tEnter S3 Bucket name: ")
                print("\t\t\t\t\tDeleting S3 bucket...")
                os.system("aws s3api delete-bucket --bucket {} --region ap-south-1".format(s3_name))
                print("\t\t\t\t\tSuccessfully deleted S3 bucket.....")
            elif int(bucket_ch) == 3:
                object_name = input("\t\t\t\t\tEnter Object name to put inside S3 bucket: ")
                s3_name = input("\t\t\t\t\tEnter S3 Bucket name: ")
                print("\t\t\t\t\tUploading object....")
                os.system('aws s3 cp /root/my-workspace-main/{} s3://{} --acl public-read'.format(object_name , s3_name))
                print("\t\t\t\t\tSuccessfully uploaded object in S3 bucket...")
            elif int(bucket_ch) == 4:
                s3_name = input("\t\t\t\t\tEnter S3 bucket name: ")
                object_name = input("\t\t\t\t\tEnter object name: ")
                print("\t\t\t\t\tDeleting object....")
                os.system('aws s3 rm s3://{}/{}'.format(s3_name , object_name))
                print("\t\t\t\t\tSuccessfully deleted object...")
            elif int(bucket_ch) == 5:
                s3_name = input("\t\t\t\t\tEnter name of bucket: ")
                region = input("\t\t\t\t\tEnter region name: ")
                print("\t\t\t\t\tDeleting S3 Bucket....")
                os.system("aws s3api delete-bucket --bucket {} --region {}".format(s3_name,region))
                print("\t\t\t\t\tSuccessfully S3 bucket successfully....")
            elif int(bucket_ch) == 6:
                exit()
