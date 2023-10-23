import pandas as pd

def describe_db(db_conn):
    ''' mysql connect -> print pandas dataframe
    Describe database tables
    '''
    sql_query =  f"""SHOW TABLES"""
    df = pd.read_sql(sql_query, db_conn)
    print(df)
    print()


def describe_table(db_conn, tab_name):
    ''' mysql connect -> print pandas dataframe
    Describe database tables
    '''
    sql_query =  f"""DESCRIBE %s""" %(tab_name)
    df = pd.read_sql(sql_query, db_conn)
    print(df)
    print()
