import pickle
import os
import sys

def create_rec():
    records = []
    while True:
        Prac_no = int(input("\nEnter Practical Number: "))
        Prac_name = input("Enter Practical Name: ")
        marks = float(input("Enter the marks: "))
        status = input("Enter Complete/Incomplete: ")
        
        record = [Prac_no, Prac_name.upper(), marks, status.upper()]
        records.append(record)

        ch = input("Do you want to enter more records? (Y/N) ")
        if ch.upper() != 'Y':
            break

    with open("Student1.dat", 'ab') as f:
        for record in records:
            pickle.dump(record, f)

def display_all():
    print("\n")
    try:
        with open("Student1.dat", "rb") as f:
            while True:
                try:
                    record = pickle.load(f)
                    print(record)
                except EOFError:
                    break
    except FileNotFoundError:
        print('File not found')

def append_rec():
    print("\n")
    records = []
    while True:
        Prac_no = int(input("\nEnter Practical Number: "))
        Prac_name = input("Enter Practical Name: ")
        marks = float(input("Enter the marks: "))
        status = input("Enter Complete/Incomplete: ")

        record = [Prac_no, Prac_name, marks, status]
        records.append(record)

        ch = input("Do you want to enter more records? (Y/N) ")
        if ch.upper() != 'Y':
            break

    with open("Student1.dat", 'ab') as f:
        for record in records:
            pickle.dump(record, f)

def search_Prac():
    print("\n")
    try:
        with open("Student1.dat", 'rb') as f:
            A = int(input("Enter Practical number to search: "))
            try:
                while True:
                    record = pickle.load(f)
                    if record[0] == A:
                        print("Record found")
                        print(record)
                        break
            except EOFError:
                print("Record not found")
    except FileNotFoundError:
        print("File not found")

def search_status(S):
    print("\n")
    try:
        with open("Student1.dat", 'rb') as f:
            flag = False
            try:
                while True:
                    record = pickle.load(f)
                    if record[3].upper() == S.upper():
                        flag = True
                        print(record)
            except EOFError:
                if not flag:
                    print("Record not found")
    except FileNotFoundError:
        print("File not found")

def update_rec():
    print("\n")
    try:
        with open("Student1.dat", 'rb+') as f:
            A = int(input("Enter Practical number to be updated: "))
            pos = 0
            try:
                while True:
                    record = pickle.load(f)
                    if record[0] == A:
                        f.seek(pos)
                        P = float(input("Enter the updated marks: "))
                        record[2] = P
                        pickle.dump(record, f)
                        print("Record updated")
                        break
                    else:
                        pos = f.tell()
            except EOFError:
                print("Record not found")
    except FileNotFoundError:
        print("File not found")

def delete_rec():
    print("\n")
    try:
        with open("Student1.dat", 'rb') as f1, open("TEMP.dat", 'wb') as f2:
            A = int(input("Enter Practical number to delete: "))
            found = False
            try:
                while True:
                    record = pickle.load(f1)
                    if record[0] == A:
                        found = True
                        continue
                    pickle.dump(record, f2)
            except EOFError:
                pass

        os.remove("Student1.dat")
        os.rename("TEMP.dat", "Student1.dat")
        
        if found:
            print("Record deleted")
        else:
            print("Record not found")

    except FileNotFoundError:
        print("File not found")

def exit_r():
    print("\n")
    sys.exit("\nExit from PROJECT\nThank you\n\n")

while True:
    print("\n\n")
    print("\t\tMAIN MENU")
    print("*********************************************")
    print("1. Create Record")
    print("2. Display Record")
    print("3. Append Record")
    print("4. Search Practical Number")
    print("5. Search status")
    print("6. Update Record (marks)")
    print("7. Delete Record")
    print("8. Exit from Project")
    print("*********************************************")
    choice = int(input("Enter your choice between 1 to 8----> "))
    
    if choice == 1:
        create_rec()
    elif choice == 2:
        display_all()
    elif choice == 3:
        append_rec()
    elif choice == 4:
        search_Prac()
    elif choice == 5:
        S = input("Enter status to search: ")
        search_status(S)
    elif choice == 6:
        update_rec()
    elif choice == 7:
        delete_rec()
    elif choice == 8:
        exit_r()
    else:
        print("\nWrong Choice!\n\nTry again")
