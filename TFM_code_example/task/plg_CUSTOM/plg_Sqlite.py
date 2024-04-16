
from a0_items import *


'''
TFM_task_action = 'a_0 ../../data/cooked/ a_1 names a_2 NAMES_table'

sqlite_folder = re.sub(r'^.*?a_0', '', TFM_task_action.partition("a_1")[0]).strip()
sqlite_file = re.sub(r'^.*?a_1', '', TFM_task_action.partition("a_2")[0]).strip()
table_name = re.sub(r'^.*?a_2', '', TFM_task_action).strip()

print (sqlite_folder)
print (sqlite_file)
print (table_name)
'''

#create db file  (./ => same folder, ../ => outside current folder)
def create_sqlite_file (sqlite_folder, sqlite_file):

   if os.path.isfile(sqlite_folder + '/'+ str(sqlite_file) + '.db'):
   
      print (sqlite_folder + '/'+ str(sqlite_file) + '.db' + ' alraedy exists')
      
   else:
  
      conn = sqlite3.connect (sqlite_folder + '/'+ str(sqlite_file) + '.db')
     
      print (sqlite_folder + '/'+ str(sqlite_file) + '.db' + ' NOT exists, is created!')



#create_sqlite_file (sqlite_folder, sqlite_file)




# https://stackoverflow.com/questions/5801170/python-sqlite-create-table-if-not-exists-problem

def create_table (sqlite_folder, sqlite_file, table_name):

   conn = sqlite3.connect(sqlite_folder + sqlite_file)
   c = conn.cursor()

   sql = "create table if not exists " + table_name + " (ID integer primary key autoincrement, name text)"
     
   c.execute(sql)

   conn.commit()
   
   print (table_name + ' table is created')


#create_table (sqlite_folder, sqlite_file, table_name= 'NAMES_table')




def insert_data (sqlite_folder, sqlite_file, table_name, data):

   conn = sqlite3.connect(sqlite_folder + sqlite_file)
   c = conn.cursor()

   sql = "INSERT INTO " + table_name + "(name) VALUES (?)"
   
   c.execute(sql,(data,)) #must include , at the end of data variable -- https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
   
   conn.commit()

#insert_data (sqlite_folder, sqlite_file, table_name, data)



def delete_table ():

   conn = sqlite3.connect(Sqlite_file)
   c = conn.cursor()

   sql = 'drop table ' + table_name
   c.execute(sql)

   conn.commit()




def select_data_sqlite (sqlite_folder, sqlite_file, table_name):

   LIST_sqlite_data = []

   conn = sqlite3.connect(sqlite_folder + sqlite_file)
   c = conn.cursor()
   
   sql = "SELECT * FROM " + table_name

   c.execute(sql)

   LIST_sqlite_data = c.fetchall()   
   
   return LIST_sqlite_data
   
   
#print (select_data_sqlite (sqlite_folder= '../../data/cooked/', sqlite_file= 'names.db', table_name = 'Names_table'))