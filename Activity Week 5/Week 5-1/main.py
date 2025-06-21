from database import create_table, create_course_table
from user_manager import add_user, view_users, search_user, delete_user, advanced_search
from course_manager import add_course, search_course

def main_menu():
    while True:
        print("\n==== Main Menu ====")
        print("1. User manager")
        print("2. Course")
        print("3. Exit")
        choice = input("Select an option (1-3) : ")
        if choice == '1':
            user_menu()
        elif choice == '2':
            course_menu()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid input, please try again.")
    

def user_menu():
    while True:
        print("\n==== User Manager ====")
        print("1. Add User")
        print("2. View All Users")
        print("3. Search User by Name")
        print("4. Delete User by ID")
        print("5. Advanced search based on ID and name")
        print("6. Back to the main menu")
        choice = input("Select an option (1-6) : ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = input("Enter user ID to delete: ")
            delete_user(user_id)
        elif choice == '5':
            user_id = int(input("Enter ID (or leave it blank) : "))
            name = input("Enter name (or leave it blank) : ")
            users = advanced_search(user_id,name)
            if users:
                for user in users:
                    print(user)
            else:
                print("Invalid choice, try again.")     
        elif choice =='6':
            return
        else:
            print("Invalid choice, try again.")
    
def course_menu():
    while True:
        print("\n==== Course Manager ====")
        print("1. Add Course")
        print("2. Search Course")
        print("3. Back to the main menu")
        choice = input("Select an option (1-3) : ")
        if choice == '1':
            course_name = input("Enter the course name : ")
            course_code = input("Enter the course code : ")
            add_course(course_name, course_code)
        elif choice =='2':
            seacrh_course_name = input("Enter the course name : ")
            seacrh_course_code = input("Enter the course code : ")
            courses = search_course(seacrh_course_name, seacrh_course_code)
            if courses:
                for course in courses:
                    print(course)
            else:
                print("couldn't find the course")
        elif choice == '3':
            return
        else:
            print("Invalid coice, try again")

def main():
    create_table()
    create_course_table()
    main_menu()


if __name__ == "__main__":
    main()

