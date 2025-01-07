# imports psycopg2 to connect to local sql DB
import psycopg2
connection = psycopg2.connect(
    database="python_sql_crm"
)

# establishes cursor variable for DB interaction
cursor = connection.cursor()

program_exit = False

# navigation functions



# main menu
while program_exit == False:
    print("""MAIN MENU

Please select from the following options:
    
1. Companies
2. Employees
3. Exit
""")
    selection = input('> ')


# grabs and displays all companies from table
cursor.execute('SELECT * FROM companies;')
print(cursor.fetchall())

# closes connection
connection.close()