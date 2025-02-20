import pickle


def load_data(filename):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}


def save_data(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


students_file = 'students.pkl'
books_file = 'books.pkl'
students = load_data(students_file)
books = load_data(books_file)


def book_issue():
    print("Issuing a book...")


def book_deposit():
    print("Depositing a book...")


def create_student_record():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    students[student_id] = student_name
    save_data(students, students_file)
    print(f"Student record for {student_name} created.")


def display_all_students():
    print("Displaying all student records...")
    for student_id, student_name in students.items():
        print(f"ID: {student_id}, Name: {student_name}")


def display_specific_student():
    student_id = input("Enter student ID to display: ")
    if student_id in students:
        print(f"ID: {student_id}, Name: {students[student_id]}")
    else:
        print("Student record not found.")


def modify_student_record():
    student_id = input("Enter student ID to modify: ")
    if student_id in students:
        student_name = input("Enter new student name: ")
        students[student_id] = student_name
        save_data(students, students_file)
        print(f"Student record for ID {student_id} modified.")
    else:
        print("Student record not found.")


def delete_student_record():
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        save_data(students, students_file)
        print(f"Student record for ID {student_id} deleted.")
    else:
        print("Student record not found.")


def create_book():
    book_id = input("Enter book ID: ")
    book_title = input("Enter book title: ")
    books[book_id] = book_title
    save_data(books, books_file)
    print(f"Book record for {book_title} created.")


def display_all_books():
    print("Displaying all books...")
    for book_id, book_title in books.items():
        print(f"ID: {book_id}, Title: {book_title}")


def display_specific_book():
    book_id = input("Enter book ID to display: ")
    if book_id in books:
        print(f"ID: {book_id}, Title: {books[book_id]}")
    else:
        print("Book record not found.")


def modify_book():
    book_id = input("Enter book ID to modify: ")
    if book_id in books:
        book_title = input("Enter new book title: ")
        books[book_id] = book_title
        save_data(books, books_file)
        print(f"Book record for ID {book_id} modified.")
    else:
        print("Book record not found.")


def delete_book_record():
    book_id = input("Enter book ID to delete: ")
    if book_id in books:
        del books[book_id]
        save_data(books, books_file)
        print(f"Book record for ID {book_id} deleted.")
    else:
        print("Book record not found.")


def administration_menu():
    while True:
        print("\n--- ADMINISTRATION MENU ---")
        print("1. CREATE STUDENT RECORD")
        print("2. DISPLAY ALL STUDENTS RECORD")
        print("3. DISPLAY SPECIFIC STUDENT RECORD")
        print("4. MODIFY STUDENT RECORD")
        print("5. DELETE STUDENT RECORD")
        print("6. CREATE BOOK")
        print("7. DISPLAY ALL BOOKS")
        print("8. DISPLAY SPECIFIC BOOK")
        print("9. MODIFY BOOK")
        print("10. DELETE BOOK RECORD")
        print("11. BACK TO MAIN MENU")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_student_record()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            display_specific_student()
        elif choice == '4':
            modify_student_record()
        elif choice == '5':
            delete_student_record()
        elif choice == '6':
            create_book()
        elif choice == '7':
            display_all_books()
        elif choice == '8':
            display_specific_book()
        elif choice == '9':
            modify_book()
        elif choice == '10':
            delete_book_record()
        elif choice == '11':
            break
        else:
            print("Invalid choice! Please try again.")


def main_menu():
    while True:
        print("\n--- MAIN MENU ---")
        print("1. BOOK ISSUE")
        print("2. BOOK DEPOSIT")
        print("3. ADMINISTRATION MENU")
        print("4. EXIT")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_issue()
        elif choice == '2':
            book_deposit()
        elif choice == '3':
            administration_menu()
        elif choice == '4':
            print("Exiting...")
            save_data(students, students_file)
            save_data(books, books_file)
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main_menu()
