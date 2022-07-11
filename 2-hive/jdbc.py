from pyhive import hive



connection = hive.Connection(host='192.168.170.100',port=10000)
cursor = connection.cursor()
cursor.execute('show databases')

print(cursor.fetchall())