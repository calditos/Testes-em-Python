import sqlite 3

connection = sqlite3.connect('tutorial.db')
c = connection.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS dados (id integer, unix real, keyword text,datestamp text, value real'))

create_table()

data_id = 4
keyword = 'Python is awesome!'
value = 4


def dataentry():
	'''
	c.execute("INSERT INTO dados VALUES(1, 136592181.288, 'python sentiments','2013-04-04 10:09:41',5)")
	c.execute("INSERT INTO dados VALUES(2, 136592181.284, 'python sentiments','2013-04-05 12:09:41',5)")
	c.execute("INSERT INTO dados VALUES(3, 136592181.285, 'python sentiments','2013-04-05 11:09:41',5)")

    '''
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H: %M: %S'))

    c.execute('INSERT INTO dados(id, unix, keyword, datestamp,value) VALUES (?,?,?,?,?)',
    	      (data_id, time.time(),keyword, date, value))


	connection.commit()
dataentry()		
