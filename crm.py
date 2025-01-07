# imports psycopg2 to connect to local sql DB
import psycopg2
connection = psycopg2.connect(
    database="python_sql_crm"
)

# establishes cursor variable for DB interaction
cursor = connection.cursor()

program_exit = False

# navigation functions

def main_menu():
    print("""MAIN MENU

Please select from the following options:
    
1. Companies
2. Employees
3. Exit
""")


def company_submenu():
    print("""COMPANIES

Please select from the following options:
    
1. Show All Companies
2. Add New Company
3. Update Company
4. Delete Company
5. Back to Main Menu
""")
    while True:
        selection = input('> ')
        if selection == '1':
            cursor.execute('SELECT * FROM companies')
            print(cursor.fetchall())
        elif selection == '2':
            company_name = input('Enter company name: ')
            cursor.execute('INSERT INTO companies (name) VALUES (%s)', [company_name])
            connection.commit()
            print('Company successfully added to database!')
        elif selection == '3':
            # stores entire company table in list
            cursor.execute('SELECT * FROM companies')
            all_companies = cursor.fetchall()
            # for loop to display list in readable format
            print("All Companies:")
            for company in all_companies:
                print(str(company[0]) + '.' + ' ' + company[1])
            # asks user for required update info
            company_id = input('Enter the # of the company to be updated: ')
            company_name = input('Enter new company name: ')
            # commits update to sql database in back end
            cursor.execute('UPDATE companies SET name = %s WHERE id = %s', [company_name, company_id])
            connection.commit()
            # prints success message for user
            print('Company name successfully updated!')
        # elif selection == '4':

        elif selection == '5':
            main_menu()


def employee_submenu():
    print("""EMPLOYEES

Please select from the following options:
    
1. Show All Employees
2. Add New Employee
3. Update Employee
4. Delete Employee
5. Back to Main Menu
""")
    while True:
        selection = input('> ')
        if selection == '1':
            cursor.execute('SELECT * FROM employees')
            print(cursor.fetchall())


# main program loop
main_menu()
while program_exit == False:
    selection = input('> ')
    if selection == '1':
        company_submenu()
    elif selection == '2':
        employee_submenu()
    elif selection == '3':
        program_exit = True


# grabs and displays all companies from table
cursor.execute('SELECT * FROM companies;')
print(cursor.fetchall())

# closes connection
connection.close()