
import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 


from plg_TXT import * 
from plg_Sqlite import * 
from plg_Process_data import * 


class Process_data:

   def get_RAW_names (self, TXT_path):
   
      return read_TXT_file (TXT_path)
      
      
   def get_COOKED_names (self):
   
      return select_data_sqlite (sqlite_folder, sqlite_file)
           
      
   def get_TO_BE_names (self):
   
      return get_TO_BE ()
           
   
   def process_TO_BE_names (self):
   
      return process_TO_BE ()


