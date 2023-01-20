
import csv
from datetime import datetime, date

time_now = datetime.now()

# i used contactbook.csv as the main database for all operation(insert,delete,update,read )
#  based on user input


def row_numbers():
    """
    helper function to count rows needed in insertion

    Return id(int) : rows count used as index inside insert function when appending row
    """
    id = 0
    with open('contactbook.csv', encoding='utf-8', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        for row in filereader:
            id += 1
    return id


def id_update():
    """
    Helper function to implement  auto increment to id column by updating all rows id after delete of any contact 
    """
    with open('contactbook.csv', encoding='utf-8', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        # add all rows into list
        rows = [row for row in filereader]
    # rewrite the content of list into new file
    with open('contactbook.csv', 'w+', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(rows[0])
        for i in range(1, len(rows)):
            # rows[i][0] = id of i-th row
            rows[i][0] = i
            csv_writer.writerow(rows[i])


# insert function to insert new records
def insert_contact():
    # first step we ask for user inputs
    name = input("Enter Name: ")
    email = input("Enter Email: ")

    # numbers list
    numbers = []
    # while user did not enter no or NO will keep appending numbers in number list
    number = input("Enter Phone Number")
    while (number.upper() != "NO" or number.lower() != "no"):
        numbers.append(number)
        number = input("add another Number (Enter Number or (no/NO) to exit)")

    add = input("Enter Address: ")
    id = row_numbers()
    row = [id, name, email, numbers, add, datetime.now()]
    # second we open file in append mode so we insert data at the end
    # encoding utf-8 to handel symbols like @ & %
    file = open("contactbook.csv", encoding='utf-8', mode='a', newline='')
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(row)


# list all contact function
def display_all():
    """
    list all contact in contactbook.csv
    no arguments and return nothing
    """
    data = open("contactbook.csv", encoding='utf-8', newline="")
    # convert lines to dictionary
    csv_data = csv.DictReader(data)
    print("ID Name\t\t", "Email\t\t", "Numbers\t\t",
          "Address\t\t", "Add Time\t\t")
    for row in csv_data:
        print(row['id']+"-", row['name']+"\t", row['email']+"\t", row['numbers'] +
              "\t\t", row['address']+"\t\t", row['Time']+"\t\t")


def delete_contact(key: str):
    """
    delete function will add all records to list without the unwanted row then rewrite the list in the same file
    key depends on user input (id) or (name)

    Param:
    key (str): row id or name of contact 

    return rows length (int)
    """
    with open('contactbook.csv', encoding='utf-8', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        # adding all rows and discarding unwanted row
        rows = [row for row in filereader if (row[0] != key and row[1] != key)]
    # rewrite the content of list into file
    # w mode to overwrite the content of the file
    with open('contactbook.csv', 'w+', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(rows)
    id_update()
    return len(rows)


def update_contact(id: str, key: str, value):
    """
    -update function will update the value based on user input 
    -user choose row by id then choose which value to change (key) and the value 
    -first open the csv file in r mode and appending all rows to list while changing the value before
    appending to list if match occurred

    @Parameters
    id (str): row id

    key (str): which value to change(name,email,address,numbers)

    value (any): value to replace it accept any input to handle list in case of updating numbers 

    return: nothing 
    """
    data = open("contactbook.csv", encoding='utf-8', newline="")
    # read file lines as dictionary
    csv_data = csv.DictReader(data)
    # empty list to add all rows after updating
    updated_Rows = []
    # loop through dictionary to update the row
    for row in csv_data:
        if row['id'] == id:
            row[key] = value
        updated_Rows.append(row)
    # re-open the file in write mode
    with open('contactbook.csv', 'w+', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # as write mode truncates the file we need to add the header row first
        csv_writer.writerow(updated_Rows[0].keys())
        # then write all rows
        for dict in updated_Rows:
            csv_writer.writerow(dict.values())


def backup():
    """
    backup function will backup content of contactbook.csv to new file contactbook +today date

    return (str):backup file name
    """
    with open('contactbook.csv', encoding='utf-8', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        # add all rows into list
        rows = [row for row in filereader]
    # rewrite the content of list into new file
    with open('contactbook'+str(date.today())+'.csv', 'w+', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(rows)
    return 'contactbook'+str(date.today())+'.csv'


def menu():
    """
    display the mai menu of user interface
    """
    print("\n \n Please Choose an option (enter q to exit)")
    print("1- List All Contacts")
    print("2- Insert New Contact")
    print("3- Update existing Contact")
    print("4- Delete Contact")
    print("5- Backup All Contacts (Locally)")
    print("6- Backup All Contacts (Cloud)")
