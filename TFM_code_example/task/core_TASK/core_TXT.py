

import sys
sys.path.append('../plg_CUSTOM/') 
sys.path.append('../plg_TFM/') 

from plg_TXT import * 


class TXT_files:


   def create_names_TXT_file (self, TXT_path):
   
      return create_TXT_file (TXT_path)
      

        
   def write_to_names_TXT (self, TXT_path, LIST_data):
   
      return write_to_TXT_file (TXT_path, LIST_data)



