import pymysql
from pymysql import cursors

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'ecorp',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)


def create_table():
    with connection.cursor() as cursor:
        add_table = """
            CREATE TABLE IF NOT EXISTS e_data(      
                id INT(10) AUTO_INCREMENT NOT NULL PRIMARY KEY,
                name VARCHAR(20),
                sales BIGINT(15),
                `date` DATE
            );     
        """;
        cursor.execute(add_table)
        connection.commit()
        
# "if not exists" helps to check if a table with that name doesn't already exist
# create_table() is a static function, as it holds no args


def write_data(curr_name, curr_amount, curr_date):
    with connection.cursor() as cursor:
        add_record = f"""
            INSERT INTO e_data (name, sales, `date`)
            VALUES
            ('{curr_name}', {curr_amount}, '{curr_date}');
        """;
        cursor.execute(add_record)
        connection.commit()


def just_queries():
    with connection.cursor() as cursor:
        my_query = """
            SELECT name, SUM(sales) AS "total sales" FROM e_data GROUP BY name ORDER BY SUM(sales) DESC
            LIMIT 10;
        """
        cursor.execute(my_query)
        connection.commit()
        return cursor.fetchall()


#- calling create table NOTE: after creating migrations and called migrant function
create_table()
output = just_queries()
print(output)