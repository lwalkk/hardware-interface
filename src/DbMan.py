import mysql.connector

class Connecter:
  def __init__(self):
    self.db = mysql.connector.connect(
      host = 'localhost',
      user = 'root',
      password = 'password',
      database = 'trucks'
    )

    self.cursor = self.db.cursor()
   
  
  def insert_new(self, phone_num, location, company):
    self.cursor.execute('SELECT * FROM drivers WHERE phone_num = %s', (phone_num,))
    data = self.cursor.fetchall()
    
    if data is not None:
      self.cursor.execute('INSERT INTO drivers (phone_num, company) VALUES(%s, %s)', (phone_num, company))
      self.cursor.execute('INSERT INTO on_site (phone_num, location, company) VALUES(%s, %s, %s)', (phone_num, location, company))
      self.db.commit()
    else:
      print('insert_new: No data')


  def insert_recurring(self, phone_num, location):
    self.cursor.execute('SELECT * FROM drivers WHERE phone_num = %s', (phone_num,))
    data = self.cursor.fetchall()
    company = 'Lafarge'
    values = (phone_num, location, company) 
    print(data)

    if data is not None: 
      self.cursor.execute('INSERT INTO on_site(phone_num, location, company) VALUES(%s, %s, %s)', values)
      self.db.commit()
    else:
      print('insert_recurring: No data')
    
  def remove(self, phone_num):
    self.cursor.execute('SELECT * FROM on_site WHERE phone_num = %s', (phone_num,))
    data = self.cursor.fetchall()

    #TODO: WRITE TO ARCHIVE
    
    if data is not None:
      self.cursor.execute('DELETE FROM on_site WHERE phone_num = %s', (phone_num,))
      self.db.commit()
    else:
      print('invalid phone number.')
