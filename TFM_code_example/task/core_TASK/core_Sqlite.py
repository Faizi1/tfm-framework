

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 


from plg_Sqlite import * 


class Sqlite_tasks:


   def create_sqlite_file (self, sqlite_folder, sqlite_file):
   
      return create_sqlite_file (sqlite_folder, sqlite_file)
      
      
   def create_sqlite_table (self,sqlite_folder, sqlite_file, table_name):
   
      return create_table (sqlite_folder, sqlite_file, table_name)
      
      


