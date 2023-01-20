# python 3.10 or higher required to run this script
# import our own lib
from classes import CRUD
from classes import s3upload as s3

# infinite loop to print the menu till q(exit) command is entered
while (True):
    # show the menu
    CRUD.menu()
    # user choice
    choice = input("Your Choice :")
    # using match and case to switch between user inputs (required python 3.10 or higher)
    match choice:
        case '1':
            print("Displaying all Contacts \n \n")
            CRUD.display_all()
        case '2':
            CRUD.insert_contact()
        case '3':
            CRUD.display_all()

            id = input("\nPlease Enter contact id: ")
            key = input(
                "\nWhich value to change(name,email,numbers,address): ")

            value = input("\n new "+key+" =")

            CRUD.update_contact(id, key, value)
        case '4':
            CRUD.display_all()
            id = input("\n Enter Contact id to delete :")
            len = CRUD.delete_contact(id)
            print("Contact deleted" if CRUD.row_numbers() ==
                  len else "contact id not found")
        case '5':
            file_name = CRUD.backup()
            print("\n File Backup Successful to "+file_name)
        case '6':
            bucket = input("Enter Bucket Name : ")
            print("\n File Backup Successful to " +
                  bucket if s3.upload_file(bucket, "contactbook.csv") else "Backup to cloud failed")
        case 'q':
            exit()
        case _:
            print('Please Enter A valid input\n')
