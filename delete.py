import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Tifanny Kate\PycharmProjects\pythonProject\5.17.22 Database\Database2.accdb')
    print("Connected to a Database")

    user_id = 10
    record = connect.cursor()
    record.execute('DELETE from Table1 WHERE id = ?', (user_id))
    record.commit()
    print("Data is deleted")

except pyodbc.Error as e:
    print("Error in Connection")