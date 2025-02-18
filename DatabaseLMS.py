import mysql.connector

# Establish a MySQL connection
conn = mysql.connector.connect(
    host='localhost',  # e.g., 'localhost'
    user='root',  # e.g., 'root'
    password='Prashnyk@1986',  # e.g., 'password'
    database='lms'  # e.g., 'library'
)
cursor = conn.cursor()

# Create tables if not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id VARCHAR(255) PRIMARY KEY,
                    name VARCHAR(255))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id VARCHAR(255) PRIMARY KEY,
                    title VARCHAR(255))''')
conn.commit()


def book_issue():
    print("Issuing a book...")


def book_deposit():
    print("Depositing a book...")


def create_student_record():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    cursor.execute("INSERT INTO students (id, name) VALUES (%s, %s)", (student_id, student_name))
    conn.commit()
    print(f"Student record for {student_name} created.")


def display_all_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("Displaying all student records...")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")


def display_specific_student():
    student_id = input("Enter student ID to display: ")
    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
    student = cursor.fetchone()
    if student:
        print(f"ID: {student[0]}, Name: {student[1]}")
    else:
        print("Student record not found.")


def modify_student_record():
    student_id = input("Enter student ID to modify: ")
    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
    student = cursor.fetchone()
    if student:
        student_name = input("Enter new student name: ")
        cursor.execute("UPDATE students SET name=%s WHERE id=%s", (student_name, student_id))
        conn.commit()
        print(f"Student record for ID {student_id} modified.")
    else:
        print("Student record not found.")


def delete_student_record():
    student_id = input("Enter student ID to delete: ")
    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
    student = cursor.fetchone()
    if student:
        cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
        conn.commit()
        print(f"Student record for ID {student_id} deleted.")
    else:
        print("Student record not found.")


def create_book():
    book_id = input("Enter book ID: ")
    book_title = input("Enter book title: ")
    cursor.execute("INSERT INTO books (id, title) VALUES (%s, %s)", (book_id, book_title))
    conn.commit()
    print(f"Book record for {book_title} created.")


def display_all_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    print("Displaying all books...")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}")


def display_specific_book():
    book_id = input("Enter book ID to display: ")
    cursor.execute("SELECT * FROM books WHERE id=%s", (book_id,))
    book = cursor.fetchone()
    if book:
        print(f"ID: {book[0]}, Title: {book[1]}")
    else:
        print("Book record not found.")


def modify_book():
    book_id = input("Enter book ID to modify: ")
    cursor.execute("SELECT * FROM books WHERE id=%s", (book_id,))
    book = cursor.fetchone()
    if book:
        book_title = input("Enter new book title: ")
        cursor.execute("UPDATE books SET title=%s WHERE id=%s", (book_title, book_id))
        conn.commit()
        print(f"Book record for ID {book_id} modified.")
    else:
        print("Book record not found.")


def delete_book_record():
    book_id = input("Enter book ID to delete: ")
    cursor.execute("SELECT * FROM books WHERE id=%s", (book_id,))
    book = cursor.fetchone()
    if book:
        cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
        conn.commit()
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
            conn.close()
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main_menu()
