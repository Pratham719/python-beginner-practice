import json
import os

path = r"C:\Users\Pratham\OneDrive\Desktop\python\ProjectFolder\student.py"


def load_data():
    if os.path.exists("Studinfo.json"):
        with open("Studinfo.json", "r") as f:
            return json.load(f)
    else:
        return []


students = load_data()


def save_data(data):
    with open("Studinfo.json", "w") as f:
        json.dump(data, f, indent=4)


def srt(data):
    return sorted(data, key=lambda s: s["Roll no"])


def add_data():
    n = int(input("Enter Number of Students :"))

    for i in range(n):
        info = {
            "Roll no": None,
            "Name": None,
            "Marks": {"Physics": None, "Chemestry": None, "Maths": None},
            "Attendance": None,
        }

        key = input(f"Enter Student Name {i+1}:")
        while not key.isalpha():
            key = input("❌ Enter valid name (letters only): ")

        rno = int(input(f"Enter the roll no of {key} :"))
        if not isinstance(rno, int):
            rno = int(input(f"Please enter the correct Roll no of {key} :"))

        m1 = int(input("Enter the Marks of Physics :"))
        if not isinstance(m1, int):
            m1 = int(input("Please enter the correct Marks of Physics :"))

        m2 = int(input("Enter the Marks of Chemestry :"))
        if not isinstance(m2, int):
            m2 = int(input("Please enter the correct Marks of Chemestry :"))

        m3 = int(input("Enter the Marks of Maths :"))
        if not isinstance(m3, int):
            m3 = int(input("Please enter the correct Marks of Maths :"))

        ad = int(input("Add Attendance :"))
        info["Name"] = key
        info["Roll no"] = rno
        info["Marks"]["Physics"] = m1
        info["Marks"]["Chemestry"] = m2
        info["Marks"]["Maths"] = m3
        info["Attendance"] = ad
        students.append(info)
        save_data(students)
        students = srt(students)
        print("✅ Student added successfully 🎉\n")


while True:
    print("\n1.Add student ")
    print("2.Search student by Roll no ")
    print("3.View all students ")
    print("4.Delete a student data ")
    print("5.Exit \n")
    option = int(input("Enter your choice :"))
    if option == 1:
        add_data()
    elif option == 2:
        ser = int(input("Enter the Roll no to search :"))
        found = False
        for s in students:
            if s["Roll no"] == ser:
                found = True
                print(s, "\n")
                break
        if found == False:
            print(f"Student having {ser} is not found :")

    elif option == 3:
        print(students, "\n")  # viwe format updgrade
    elif option == 4:
        dlt = int(input("Enter Roll no to delete data :"))
        found = False
        for s in students:
            if s["Roll no"] == dlt:
                students.remove(s)
                save_data(students)
                found = True
                break
        if found:
            print(f"\n✅ The data of Roll No {s["Roll no"]} is successfully Deleted🎉")
        else:
            print(f"Can't found the Roll no {s["Roll no"]}")
        students = load_data()
        print(students, "\n")
    elif option == 5:
        break
    else:
        print("Invalid input")
        break
