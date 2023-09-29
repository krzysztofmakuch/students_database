import sys
import student_across_exercises


def run_interface():
    ''' just run it!'''
    main_ife()



def main_ife():
    ''' the very main options, before sub-interface '''
    
    print('Select a option')
    options = f"""
    0. Describe databse
    1. Describe table named 'tab': 1.'tab'
    2. Show all records in the table 'tab': 2.tab
    2. Run operations (new menu)
    Q. QUIT
    """
    opt = input(options)
    if opt in ['q','Q','quit','QUIT']: 
        run_exit()

def operations_ife():
    ''' Ops on the database '''
    print('Select a option')
    options = f"""
    1. Show student 'id' marks through exercises: 1.id
    2. Compare marks for different students in exercise 'id': 2.id
    3. Return to the main menu.
    Q. QUIT
    """
    opt = input(options)
    if opt in ['q','Q','quit','QUIT']: 
        run_exit()

def run_exit():
    print('my job is done!')
    sys.exit(0)


if __name__ == '__main__':
    run_interface()


