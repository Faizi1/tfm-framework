

import sqlite3

###################################################################################################
### plugins - folders & sqlite file 
####################################################################################################

def create_folder (folder_path):
  
  if not os.path.isdir(folder_path):
     
     os.makedirs(folder_path)#if folder not exists, create it  
     print (folder_path + ' folder NOT exists, is created')     
                   
  else:
          
     #shutil.rmtree(folder_path)#if folder exists, remove it   
     print (folder_path + ' folder exists') 


#create_folder (folder_path)

 
  
#create db file   
def create_sqlite_file (folder_path, sqlite_file):
  
   conn = sqlite3.connect (folder_path + '/'+ str(sqlite_file) + '.db')