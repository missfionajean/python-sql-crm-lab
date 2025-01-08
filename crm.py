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
    #
    is_on_company_menu = True
    while is_on_company_menu:
        selection = input('> ')
        if selection == '1':
            
            print("\nEnter Company Number to view all Employees or NO to exit: ")
            #show all companies ASC order
            cursor.execute('SELECT * FROM companies ORDER BY id ASC')
            all_companies = cursor.fetchall()
            
            for company in all_companies:
                print(f"{company[0]}. {company[1]}")

            is_on_individual_company = True

            while is_on_individual_company:
                #accepted values are the company_id section in the employees table
                view_employees =  input("(NO / #)> ")
                
                #simple query if there will be a match for the provided 
                if view_employees == 'NO':
                    is_on_individual_company = False
                    company_submenu()
                    #we need to exit out the company_submenu function
                    is_on_company_menu = False
                
                else:

                    #check if the provided input has a match in the companies db
                    cursor.execute('SELECT COUNT(*) FROM companies WHERE id = %s', [int(view_employees)])
                    company_found = cursor.fetchone()[0]

                    if company_found < 1:
                        print("No company correspond with that id")
                    else:
                        cursor.execute('SELECT * FROM employees WHERE company_id = %s', [int(view_employees)])
                        all_employee = cursor.fetchall()
                        
                        #get the name of the company
                        cursor.execute("SELECT name FROM companies WHERE id = %s", [view_employees])
                        company_name = cursor.fetchone()[0]

                        #if the query results into an empty list of employee
                        if not all_employee:
                            print(f"{company_name} has no employee yet")
                        else:
                            print(f"All Employees of {company_name}\n")

                            for employee in all_employee:
                                print(f"{employee[0]}. {employee[1]}")

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
            print("\nAll Companies:")
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
        elif selection == '4':
            # stores entire company table in list
            cursor.execute('SELECT * FROM companies')
            all_companies = cursor.fetchall()
            # for loop to display list in readable format
            print("All Companies:")
            for company in all_companies:
                print(str(company[0]) + '.' + ' ' + company[1])
            # asks user to select a company to be deleted
            company_id = input('Enter the # of company to be deleted: ')
            # deletes selected entry from database
            cursor.execute('DELETE FROM companies WHERE id = %s', [company_id])
            connection.commit()
            # prints success message for user
            print('Company successfully deleted!')
        elif selection == '5':
            main_menu()
            #we need to exit out the company_submenu function
            is_on_company_menu = False


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
        print('Goodbye! ')
        program_exit = True


# grabs and displays all companies from table
# cursor.execute('SELECT * FROM companies;')
# print(cursor.fetchall())

# closes connection
connection.close()