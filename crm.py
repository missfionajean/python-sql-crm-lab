# import OS module for screen clearing between actions
import os

# call function to dynamically clear terminal based on OS
def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux
    else:
        os.system('clear')

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
    
def company_menu_text():
    print("""COMPANIES

Please select from the following options:
    
1. Show All Companies
2. Add New Company
3. Update Company
4. Delete Company
5. Back to Main Menu
""")
    
def company_submenu():
    is_on_company_menu = True
    while is_on_company_menu:
        company_menu_text()
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
                    clear_terminal()
                    company_submenu()
                    #we need to exit out the company_submenu function
                    is_on_company_menu = False
                
                else:
                    #check if the provided input has a match in the companies db
                    cursor.execute('SELECT COUNT(*) FROM companies WHERE id = %s', [int(view_employees)])
                    company_found = cursor.fetchone()[0]

                    if company_found < 1:
                        print("No company corresponds with that ID #")
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
            input('Company successfully added to database! [PRESS ENTER TO CONTINUE]')
            clear_terminal()
            company_submenu()
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
            input('Company name successfully updated! [PRESS ENTER TO CONTINUE]')
            clear_terminal()
            company_submenu()
        elif selection == '4':
            # stores entire company table in list
            cursor.execute('SELECT * FROM companies ORDER BY id ASC')
            all_companies = cursor.fetchall()
            # for loop to display list in readable format
            print("All Companies:")
            for company in all_companies:
                print(str(company[0]) + '.' + ' ' + company[1])
            # asks user to select a company to be deleted
            company_id = input('Enter the # of company to be deleted: ')

            cursor.execute('SELECT COUNT(*) FROM employees WHERE company_id = %s', [company_id])
            employee_count = cursor.fetchone()[0]

            if employee_count < 1:
                # deletes selected entry from database
                cursor.execute('DELETE FROM companies WHERE id = %s', [company_id])
                connection.commit()
                # prints success message for user
                input('Company successfully deleted! [PRESS ENTER TO CONTINUE]')
                clear_terminal()
                company_submenu()
            else:
                print("\nAll Employees must be Let go before deleting company profile\n")
                input('[PRESS ENTER TO CONTINUE]')
                clear_terminal()
            
        elif selection == '5':
            clear_terminal()
            main_menu()
            #we need to exit out the company_submenu function
            is_on_company_menu = False

def employee_menu_text():
    print("""EMPLOYEES

Please select from the following options:
    
1. Show All Employees
2. Add New Employee
3. Update Employee
4. Delete Employee
5. Back to Main Menu
""")

def employee_submenu():
    is_on_employee_menu = True
    while is_on_employee_menu:
        employee_menu_text()
        selection = input('> ')
        if selection == '1':
            cursor.execute('SELECT * FROM employees')
            all_employees = cursor.fetchall()
            print('\nALL EMPLOYEES')
            for employee in all_employees:
                # grabs/prints both employee and related company
                cursor.execute(f'SELECT name FROM companies WHERE id = {employee[2]}')
                company = cursor.fetchone()
                try:
                    company = str(company[0])
                except:
                    # does nothing if above doesn't work
                    pass
                print(f"{employee[0]}. {employee[1]}, {company}")
            input('[PRESS ENTER TO CONTINUE]')
            clear_terminal()
        elif selection == '2':
            employee_name = input('Enter employee name: ')
            employee_company_id = input('Enter company ID: ')
            cursor.execute('INSERT INTO employees (name, company_id) VALUES (%s, %s)', [employee_name, employee_company_id])
            connection.commit()
            input('Employee successfully added to database! [PRESS ENTER TO CONTINUE]')
            clear_terminal()
            employee_submenu()
        elif selection == '3':
            cursor.execute('SELECT * FROM employees')
            all_employees = cursor.fetchall()
            print("All Employees:")
            for employee in all_employees:
                print(str(employee[0]) + '.' + ' ' + employee[1])
            employee_id = input('Enter the # of the employee to be updated: ')
            employee_name = input('Enter new employee name: ')
            employee_company_id = input('Enter new company ID: ')
            cursor.execute('UPDATE employees SET name = %s, company_id = %s WHERE id = %s', [employee_name, employee_company_id, employee_id])
            connection.commit()
            input('Employee successfully updated! [PRESS ENTER TO CONTINUE]')
            clear_terminal()
            employee_submenu()
        elif selection == '4':
            cursor.execute('SELECT * FROM employees')
            all_employees = cursor.fetchall()
            print("All Employees:")
            for employee in all_employees:
                print(str(employee[0]) + '.' + ' ' + employee[1])
            employee_id = input('Enter the # of the employee to be deleted: ')
            cursor.execute('DELETE FROM employees WHERE id = %s', [employee_id])
            connection.commit()
            input('Employee successfully deleted!  [PRESS ENTER TO CONTINUE]')
            clear_terminal()
            employee_submenu()
        elif selection == '5':
            clear_terminal()
            main_menu()
            is_on_employee_menu = False

# main program loop
clear_terminal()
main_menu()
while program_exit == False:
    main_selection= '0'
    main_selection = input('> ')
    if main_selection == '1':
        clear_terminal()
        company_submenu()
    elif main_selection == '2':
        clear_terminal()
        employee_submenu()
    elif main_selection == '3':
        clear_terminal()
        print('Goodbye!')
        program_exit = True


# closes connection
connection.close()