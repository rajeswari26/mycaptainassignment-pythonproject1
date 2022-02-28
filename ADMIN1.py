
import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a' , newline='')as csv_file:
        writer=csv.writer(csv_file)
       
        if csv_file.tell()==0:
            writer.writerow(["name" ,"age" ,"phone number" , "email-id","father_name","mother_name", "address"])
        writer.writerow(info_list)
if __name__=='__main__':
    condition=True
    student_num=1
    while(condition):
        student_info=input("enter the student information for student#{} in the following format(name age  phone number email-id father_name mother_name address ):".format(student_num))
        print("enter information:"+student_info)
        student_info_list=student_info.split(' ')
        print(" the splitted information is:", student_info_list)
        print("\n the entered information-\nname: {}\nage: {}\nphone number: {}\nemail-id: {}\nfahter_name: {}\nmother_name: {}\naddress: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4],student_info_list[5],student_info_list[6]))
        choice=input("is the entered information is correct?(y/n):")
        if choice=='y':
             
            write_into_csv(student_info_list)
            check=input("do you want to continue further? :")
            if check=='y':
                condition=True
                student_num+=1
            elif check=='n':
                condition=False
        elif choice=='n':
            print("check and re enter the information!")