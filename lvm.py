import os
os.system("clear")
ch = input("\t\t\t\tDo you want to do LVM in your Local machine or Remote Machine: ")
while True:
   # os.system("clear")
    os.system("tput setaf  3")
    print("\t\t======================================================================")
    os.system("tput setaf  2")
    os.system("tput bold")
    print("\t\t\t*******Logical Volume Management(LVM) Automation*******\t\t")
    os.system("tput setaf  6")
    print("\t\t======================================================================")
    os.system("tput setaf  7")
    if ch == "local machine": 
        print("""
                \n 
                \t\t Press 1  : Create Physical Volume
                \t\t Press 2  : Show all Physical volumes
                \t\t Press 3  : Create Volume Group
                \t\t Press 4  : Show all Volume Groups
                \t\t Press 5  : Add more Hard Disks in Volume Group
                \t\t Press 6  : Create Logical Partitions
                \t\t Press 7  : Format partitions
                \t\t Press 8  : Mount partitions on folder
                \t\t Press 9  : Extend Partitons
                \t\t Press 10 : Shrink Partitions
                \t\t Press 11 : Show all Hard Disks
                \t\t Press 12 : Show all logical volumes
                \t\t Press 13 : Remove Physical Volume
                \t\t Press 14 : Remove Volume group
                \t\t Press 15 : Remove Logical Volume
                \t\t Press 16 : Go back to main menu
                """)
        lv_ch = input("\t\t\t\tEnter your Choice: ")
        if int(lv_ch) == 1:
            n = input("\t\t\t\tEnter the number which you want to create Physical Volume: ")
            for i in range(int(n)):
                global n1
                n1 = input("\t\t\t\tEnter {} disk name: ".format(i))
                os.system("pvcreate {}".format(n1))
                os.system("pvdisplay {}".format(n1))
        elif int(lv_ch) == 2:
            os.system("pvdisplay")
        elif int(lv_ch) == 3:
            global c
            c = input("\t\t\t\tEnter the name of Volume group: ")
            os.system("vgcreate {0} {1}".format(c,n1))
            os.system("vgdisplay {0}".format(c))
        elif int(lv_ch) == 4:
            os.system("vgdisplay")
        elif int(lv_ch) == 5:
            pvname = input("\t\t\t\tEnter PV name: ")
            os.system("vgextend {0} {1}".format(c,pvname))
            os.system("vgdisplay {0}".format(c))
        elif int(lv_ch) == 6:
            s = input("\t\t\t\tEnter the size of LV: ")
            n2 = input("\t\t\t\tEnter the name of LV: ")
            vg = input("\t\t\t\tEnter name of volume group: ")
            os.system("lvcreate --size {0}G --name {1} {2}".format(s,n2,vg))
            os.system("lvdisplay {0}".format(n2))
        elif int(lv_ch) == 7:
            os.system("clear")
            while True:
                print("""
                \n
                \t\t\t Press 1 : mkfs.ext4
                \t\t\t Press 2 : resize2fs
                \t\t\t Press 3 : Go back to previous menu
                """)
                fmt_ch = input("\t\t\t\tEnter your choice: ")
                if int(fmt_ch) == 1:
                    vg = input("\t\t\t\tEnter name of volume group: ")
                    lv = input("\t\t\t\tEnter name of logical VOlume: ")
                    os.system("mkfs.ext4 /dev/{0}/{1}".format(vg,lv))
                elif int(fmt_ch) == 2:
                    vg1 = input("\t\t\t\tEnter name of volume group: ")
                    lv1 = input("\t\t\t\tEnter name of logical VOlume: ")
                    os.system("resize2fs /dev/{0}/{1}".format(vg1,lv1))
                    os.system("df -H")
                elif int(fmt_ch) == 3:
                    break
        elif int(lv_ch) == 8:
            global f1
            f1 = input("\t\t\t\tEnter the name of file: ")
            os.system("mkdir /{0}".format(f1))
            vgname = input("\t\t\t\tEnter name of Volume Group: ")
            lvname = input("\t\t\t\tEnter name of Logical Volume: ")
            os.system("mount /dev/{}/{} {}".format(vgname,lvname,f1))
            os.system("df -H")
        elif int(lv_ch) == 9:
            global s1
            s1 = input("\t\t\t\tEnter the size which you want to extend: ")
            vg = input("\t\t\t\tEnter name of volume group: ")
            lv = input("\t\t\t\tEnter name of logical VOlume: ")
            os.system("lvextend --size +{0}G /dev/{1}/{2}".format(s1,vg,lv))
        elif int(lv_ch) == 10:
            global s2
            s2 = input("\t\t\t\tEnter the size which you want to make your lv: ")
            vg = input("\t\t\t\tEnter name of volume group: ")
            lv = input("\t\t\t\tEnter name of logical Volume: ")
            filename = input("\t\t\t\tEnter name of file which you want to unmount: ")
            os.system("umount {}".format(filename))
            os.system("e2fsck -f /dev/{}/{}".format(vg,lv))
            os.system("resize2fs /dev/iiec/lv1 {}G".format(s2))
            os.system("lvreduce --size {0}G /dev/{1}/{2} -y".format(s2,vg,lv))
            os.system("mount /dev/{}/{} {}".format(vg,lv,filename))
        elif int(lv_ch) == 11:
            os.system("fdisk -l")
        elif int(lv_ch) == 12:
            os.system("lvdisplay")
        elif int(lv_ch) == 13:
            pvname = input("\t\t\t\tEnter name of Physical volume: ")
            os.system("pvremove {}".format(pvname))
        elif int(lv_ch) == 14:
            vgname = input("\t\t\t\tEnter name of Volume Group: ")
            os.system("vgremove {}".format(vgname))
        elif int(lv_ch) == 15:
            lvname = input("\t\t\t\tEnter name of LVM: ")
            vg_n = input("\t\t\t\tEnter name of Volume group: ")
            os.system("umount /dev/{}/{}".format(vg_n,lvname))
            os.system("lvremove /dev/{}/{}".format(vg_n,lvname))
        elif int(lv_ch) == 16:
            exit()
    elif ch == "remote machine":
        ip = input("\t\t\t\tEnter your IP: ")
        print("""
                \n
                \t\t\t Press 1  : Create Physical Volume
                \t\t\t Press 2  : Show all Physical volumes
                \t\t\t Press 3  : Create Volume Group
                \t\t\t Press 4  : Show all Volume Groups
                \t\t\t Press 5  : Add more Hard Disks in Volume Group
                \t\t\t Press 6  : Create Logical Partitions
                \t\t\t Press 7  : Format partitions
                \t\t\t Press 8  : Mount partitions on folder
                \t\t\t Press 9  : Extend Partitons
                \t\t\t Press 10 : Shrink Partitions
                \t\t\t Press 11 : Show all Hard Disks
                \t\t\t Press 12 : Show all logical volumes
                \t\t\t Press 13 : Remove Physical Volume
                \t\t\t Press 14 : Remove Volume group
                \t\t\t Press 15 : Remove Logical Volume
                \t\t\t Press 16 : Go back to main menu
                """)
        lv_ch = input("\t\t\t\tEnter your Choice: ")
        if int(lv_ch) == 1:
            n = input("\t\t\t\tEnter the number which you want to create Physical Volume: ")
            for i in range(int(n)):
                global n23
                n1 = input("\t\t\t\tEnter {} disk name: ".format(i))
                os.system("ssh {} pvcreate {}".format(ip,n23))
                os.system("ssh {} pvdisplay {}".format(ip,n23))
        elif int(lv_ch) == 2:
            os.system("ssh {} pvdisplay".format(ip))
        elif int(lv_ch) == 3:
            global c1
            c = input("\t\t\t\tEnter the name of Volume group: ")
            os.system("ssh {} vgcreate {} {}".format(ip,c1,n23))
            os.system("ssh {} vgdisplay {}".format(ip,c1))
        elif int(lv_ch) == 4:
            os.system("ssh {} vgdisplay".format(ip))
        elif int(lv_ch) == 5:
            pvname = input("\t\t\t\tEnter PV name: ")
            os.system("ssh {} vgextend {} {}".format(ip,c1,pvname))
            os.system("ssh {} vgdisplay {0}".format(ip,c1))
        elif int(lv_ch) == 6:
            s = input("\t\t\t\tEnter the size of LV: ")
            n2 = input("\t\t\t\tEnter the name of LV: ")
            vg = input("\t\t\t\tEnter name of volume group: ")
            os.system("ssh {} lvcreate --size {}G --name {} {}".format(ip,s,n2,vg))
            os.system("ssh {} lvdisplay {0}".format(ip,n2))
        elif int(lv_ch) == 7:
            os.system("clear")
            while True:
                print("""
                \n
                \t\t\t Press 1 : mkfs.ext4
                \t\t\t Press 2 : resize2fs
                \t\t\t Press 3 : Go back to previous menu
                """)
                fmt_ch = input("\t\t\t\tEnter your choice: ")
                if int(fmt_ch) == 1:
                    vg = input("\t\t\t\tEnter name of volume group: ")
                    lv = input("\t\t\t\tEnter name of logical VOlume: ")
                    os.system("ssh {} mkfs.ext4 /dev/{}/{}".format(ip,vg,lv))
                elif int(fmt_ch) == 2:
                    vg1 = input("\t\t\t\tEnter name of volume group: ")
                    lv1 = input("\t\t\t\tEnter name of logical VOlume: ")
                    os.system("ssh {} resize2fs /dev/{}/{}".format(ip,vg1,lv1))
                    os.system("ssh {} df -H".format(ip))
                elif int(fmt_ch) == 3:
                    break
        elif int(lv_ch) == 8:
            f1 = input("\t\t\t\tEnter the name of file: ")
            os.system("ssh {} mkdir /{0}".format(ip,f1))
            vgname = input("\t\t\t\tEnter name of Volume Group: ")
            lvname = input("\t\t\t\tEnter name of Logical Volume: ")
            os.system("ssh {} mount /dev/{}/{} {}".format(ip,vgname,lvname,f1))
            os.system("ssh {} df -H".format(ip))
        elif int(lv_ch) == 9:
            s1 = input("\t\t\t\tEnter the size which you want to extend: ")
            vg = input("\t\t\t\tEnter name of volume group: ")
            lv = input("\t\t\t\tEnter name of logical VOlume: ")
            os.system("ssh {} lvextend --size +{}G /dev/{}/{}".format(ip,s1,vg,lv))
        elif int(lv_ch) == 10:
            s2 = input("\t\t\t\tEnter the size which you want to make your lv: ")
            vg = input("\t\t\t\tEnter name of volume group: ")
            lv = input("\t\t\t\tEnter name of logical Volume: ")
            filename = input("\t\t\t\tEnter name of file which you want to unmount: ")
            os.system("ssh {} umount {}".format(ip,filename))
            os.system("ssh {} e2fsck -f /dev/{}/{}".format(ip,vg,lv))
            os.system("ssh {} resize2fs /dev/iiec/lv1 {}G".format(ip,s2))
            os.system("ssh {} lvreduce --size {0}G /dev/{1}/{2} -y".format(ip,s2,vg,lv))
            os.system("ssh {} mount /dev/{}/{} {}".format(ip,vg,lv,filename))
        elif int(lv_ch) == 11:
            os.system("ssh {} fdisk -l".format(ip))
        elif int(lv_ch) == 12:
            os.system("ssh {} lvdisplay".format(ip))
        elif int(lv_ch) == 13:
            pvname = input("\t\t\t\tEnter name of Physical volume: ")
            os.system("ssh {} pvremove {}".format(ip,pvname))
        elif int(lv_ch) == 14:
            vgname = input("\t\t\t\tEnter name of Volume Group: ")
            os.system("ssh {} vgremove {}".format(ip,vgname))
        elif int(lv_ch) == 15:
            lvname = input("\t\t\t\tEnter name of LVM: ")
            vg_n = input("\t\t\t\tEnter name of Volume group: ")
            os.system("ssh {} umount /dev/{}/{}".format(ip,vg_n,lvname))
            os.system("ssh {} lvremove /dev/{}/{}".format(ip,vg_n,lvname))
        elif int(lv_ch) == 16:
            exit()
