size = 10
hash_table = [None] * size

def insert():
    roll = int(input("Enter roll number: "))
    name = input("Enter student name: ")
    index = roll % size

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is None or hash_table[pos] == "DELETED":
            hash_table[pos] = (roll, name)
            print("Student record inserted successfully")
            return

        if hash_table[pos][0] == roll:
            print("Roll number already exists")
            return

    print("Hash table is full")


def search():
    roll = int(input("Enter roll number to search: "))
    index = roll % size

    for i in range(size):
        pos = (index + i) % size
        record = hash_table[pos]

        if record is None:
            break

        if record != "DELETED" and record[0] == roll:
            print("Student found:", record[1])
            return

    print("Student not found")


def display():
    print("\nIndex\tRoll Number\tStudent Name")

    for i in range(size):
        record = hash_table[i]

        if record is None:
            print(i, "\tEmpty")
        elif record == "DELETED":
            print(i, "\tDeleted")
        else:
            print(i, "\t", record[0], "\t\t", record[1])


def delete():
    roll = int(input("Enter roll number to delete: "))
    index = roll % size

    for i in range(size):
        pos = (index + i) % size
        record = hash_table[pos]

        if record is None:
            break

        if record != "DELETED" and record[0] == roll:
            hash_table[pos] = "DELETED"
            print("Student record deleted successfully")
            return

    print("Student not found")


while True:
    print("\n--- Student Registration System ---")
    print("1. Insert Student Record")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display Hash Table")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert()
    elif choice == 2:
        search()
    elif choice == 3:
        delete()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
