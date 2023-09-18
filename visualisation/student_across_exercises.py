import pandas as pd
import matplotlib.pyplot as plt
import pymysql

# Define your database connection parameters
db_config = {'host': 'localhost',
             'port': 3306,
             'user': 'root',
             'password': 'alamakota',
             'database': 'students_db',  # Replace with your database name
            }

# Replace '1' with the actual student ID you want to compare
student_id_to_compare = 1

# Replace 'b2km' with the actual course ID you want to analyze
course_id_to_analyze = 'b2km'

conn = None

# Connect to the database
try:
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    # SQL query to retrieve data for the specified student and course
    sql_query = f"""
    SELECT e.exercise_id, SUM(m.student_points) AS total_points
    FROM exercises e
    LEFT JOIN
    tasks t ON e.exercise_id = t.exercise_id
    LEFT JOIN
    marks m ON t.task_id = m.task_id
    WHERE
    e.course_id = 'b2km' 
    AND m.student_id = 1 
    GROUP BY
    e.exercise_id;
    """

    # Put data into a Pandas DataFrame
    df = pd.read_sql(sql_query, conn)
    print(df)

    # Create bar plots for each exercise
    plt.figure(figsize=(10, 6))
    plt.bar(df['exercise_id'], df['total_points'], color='blue')
    plt.title('Total Points for Each Exercise')
    plt.xlabel('Exercise ID')
    plt.ylabel('Total Points')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

except pymysql.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    if conn:
        conn.close()
