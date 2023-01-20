
# Contact Book

Python Script to perform some operation(CRUD) on contactbook.csv through CLI using csv Module

- List all contacts 
- insert new contact 
- Update existing contact 
- delete contact
- Backup (local-cloud)
## Dependencies

- python 3.10 or later
check python version (windows/linux)

```bash
  python --version
```
- boto3
```bash
    pip install boto3
```    


## Running the script
main.py our entry point 
- first line import our CRUD script from classes folder
```bash
    from classes import CRUD
```
- then using match and case to switch between user input
![alt text](https://github.com/Hawila/SWCM_Repo/blob/master/2.png?raw=true)

- CRUD.menu() print this menu and while(true) will keep printing the menu

![alt text](https://github.com/Hawila/SWCM_Repo/blob/master/1.png?raw=true)


based on user input match/case will call function from CRUD
- all function defined using Python docstrings
![alt text](https://github.com/Hawila/SWCM_Repo/blob/master/3.png?raw=true)
- defination , Parameters ,return 
![alt text](https://github.com/Hawila/SWCM_Repo/blob/master/4.png?raw=true)

before using Backup All contacts (cloud)
-
you need to set up authentication credentials for your AWS account
```bash
    aws configure
```
then edit 
```bash
    [default]
    aws_access_key_id = YOUR_ACCESS_KEY
    aws_secret_access_key = YOUR_SECRET_KEY
```
  


## check video for Examples
no validation added to check string inputs so any input considered valid and will be written to file 
