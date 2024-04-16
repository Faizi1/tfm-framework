

from a0_items import * 
from plg_TXT import *
from plg_Sqlite import * 

 
''' 
TXT_path =  '../../data/raw/names.txt'
sqlite_folder = '../../data/cooked/'
sqlite_file = 'names'
table_name = 'NAMES_table'
'''
 
def get_TO_BE ():

   LIST_raw = read_TXT_file (TXT_path)
   LIST_cooked = select_data_sqlite (sqlite_folder, sqlite_file, table_name)
   
   LIST_to_be = []
   
   for raw in LIST_raw:
   
      if raw in LIST_cooked:
          
         print ("RAW in LOG or DB =>", raw)
         
      else:
      
         print ("RAW NOT in LOG or DB, to be inserted =>", raw)
         
         LIST_to_be.append(raw.strip())
          
   return LIST_to_be
   
#print(get_TO_BE ())

 
   
def process_TO_BE ():

   LIST_to_be = get_TO_BE ()
   
   for data in LIST_to_be:
   
      insert_data (sqlite_folder, sqlite_file, table_name, data)
