import random

# flag = 0

student_list = []

name = input("enter a name of student::")
roll_no = int(input("enter a roll_no of the student::"))
class_name = str(input("enter the class of the student::"))
phone_number = int(input("enter the mobile number of the student::"))
total_marks = int(input("enter total marks obtained by student::"))
address_student = str(input("enter a address of the student::"))

dictionary = {
    "name": name,
    "roll_no": roll_no,
    "class_name": class_name,
    "phone_number": phone_number,
    "total_marks": total_marks,
    "address_student": address_student
}

print("your dictionary look like::", dictionary)
print("unique ID", random.randint(1, 100))

student_list.append(dictionary)
print(student_list)

print("1. insert the student")
print("2. update the student")
print("3. delete the student")
print("4. view the student")

choice = int(input("choice the option from the above"))

while True:

    if choice == 1:
        print("enter the requirement::")
        name = input("enter a name of student::")
        roll_no = int(input("enter a roll_no of the student::"))
        class_name = str(input("enter the class of the student::"))
        phone_number = int(input("enter the mobile number of the student::"))
        total_marks = int(input("enter total marks obtained by student::"))
        address_student = str(input("enter a address of the student::"))
        # print(student_list)

        student_list.append(name)
        student_list.append(roll_no)
        student_list.append(class_name)
        student_list.append(phone_number)
        student_list.append(total_marks)
        student_list.append(address_student)
        print(student_list)
        break

    elif choice == 2:
        print("update the list::")
        new_id = int(input("enter the index::"))

        for new_id in student_list:
            # if student_list[new_id] == new_id:
            name = input("enter a name of student::")
            roll_no = int(input("enter a roll_no of the student::"))
            class_name = str(input("enter the class of the student::"))
            phone_number = int(input("enter the mobile number of the student::"))
            total_marks = int(input("enter total marks obtained by student::"))
            address_student = str(input("enter a address of the student::"))

            student_list.append(name)
            student_list.append(roll_no)
            student_list.append(class_name)
            student_list.append(phone_number)
            student_list.append(total_marks)
            student_list.append(address_student)

            print("your dictionary look like::", dictionary)
            print("unique data", random.randint(1, 100))
            print(student_list)
            print("updated successful")
            break

    elif choice == 3:
        print("delete the data from the student")
        index_remove = int(input("enter the value of index::"))

        del student_list[index_remove]
        print(student_list)
        break

    elif choice == 4:
        print("view the list of student::")
        print(student_list)
        break

    else:
        print("program are terminate")
        break
