import sys
from load_db import mysql_connection
import options as sql_options


# import student_across_exercises


def run_interface(db=None):
    ''' just run it!'''
    print('Interface will be executed for a database with the following parameters:\n %s' % (db))
    with mysql_connection(db_config) as db_conn:
        coursor = db_conn.cursor()
        main_ifc(db_conn)


def option_choice(options_dict):
    ''' dict
    Runs a function from the library of functions. For example:
    >>> option_choice({'1':'ala', '2':'kot'})
    1
    ala
    '''
    opt = input().split('.')
    #print(opt)
    # beware!
    # the function returns the 0-element, which is the function from dict and
    try:
        # print(options_dict[opt])
        return [ opt[0], options_dict[opt[0]], opt[1] ]
    except IndexError:
        return [ opt[0], options_dict[opt[0]] ]
    except KeyError:
        print('\n ! Key Error! Non existing option, try again !')
        return 'again'


def print_options_mainmenu():
    ''' '''
    print('Select an option')
    options = f"""
    0. Describe databse
    1. Describe table named 'tab': 1.'tab'
    2. Show all records in the table 'tab': 2.tab
    3. Run operations (new menu)
    Q. QUIT
    """
    print(options)


def main_ifc(db=None):
    ''' the very main options, before sub-interface '''
    options = {'0': sql_options.describe_db, '1':sql_options.describe_table, '3':operations_ifc, 'Q': 'Q'}
    i = 1
    while i > 0:
        print_options_mainmenu()
        opt = option_choice(options)
        #print(opt)
        # options for quitting should be re-done
        #if (opt != 'again') & (opt not in ['q', 'Q', 'quit', 'QUIT']):
        if opt[0] in ['0','3']:
            #print(opt[0])
            opt[1](db)
        elif opt[0] in ['1','2']:
            opt[1](db, opt[2])
        elif (opt[0] in ['q', 'Q', 'quit', 'QUIT']):
            break


def print_options_submenu():
    """ """
    print('Select an option')
    options = f"""
    1. Show student 'id' marks through exercises: 1.id
    2. Compare marks for different students in exercise 'id': 2.id
    3. Return to the main menu.
    Q. QUIT
    """
    print(options)


def operations_ifc(db=None):
    ''' Ops on the database '''
    options = {'Q': run_exit}
    i = 1
    while i > 0:
        print_options_mainmenu()
        opt = option_choice(options)
        # options for quitting should be re-done
        if (opt != 'again') & (opt not in ['q', 'Q', 'quit', 'QUIT']):
            opt(db)
        elif (opt in ['q', 'Q', 'quit', 'QUIT']):
            break

    """
    if opt in ['q','Q','quit','QUIT']: 
        run_exit()
    """


def run_exit():
    print('my job is done!')
    sys.exit(0)


if __name__ == '__main__':
    db_config = {'host': 'localhost',
                 'port': 3306,
                 'user': 'root',
                 'password': 'alamakota',
                 'database': 'students_db',  # Replace with your database name
                 }
    run_interface(db_config)
