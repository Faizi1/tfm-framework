
#must append ALL folder paths of the files to be imported and used
import sys
sys.path.append('core_TASK/')
sys.path.append('plg_CUSTOM/') 
sys.path.append('plg_TFM/')


from core_TXT import *
#from core_Sqlite import *
#from core_Process_data import *


#https://www.codeproject.com/Questions/5339935/How-do-I-pass-multiple-variables-from-PHP-to-Python

#pass in the values from API_get_request
#TFM_task = sys.argv[1]  
#TFM_task_action = sys.argv[2]   

#eg. http://12.242.23.23/TFM_task=TASK_1?TFM_task_action=a_0../data/raw/names.txta_1'david','peter','jon','lucy' 


TFM_task = 'TASK_1'
TFM_task_action = "a_0 ../data/raw/names.txt a_1 david,peter,jon,lucy"


'''
TFM_task = 'TASK_2'
TFM_task_action = 'a_0 ../../data/cooked/ a_1 names.db a_2 NAMES_table'
'''

'''
TFM_task = 'TASK_3'
TFM_task_action = 'a_0 ../data/raw/names.txt a_1' 
'''

'''
TXT_path = '../data/raw/names.txt'
LIST_data = ['david', 'peter', 'jon', 'lucy']

sqlite_folder = '../data/cooked/'
sqlite_file = 'names.db'
table_name = 'NAMES_table'
'''

# https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
def select_task ():

   match TFM_task: # TFM task name = includes name of the payment system  
       
       ### task 1
       case "TASK_1":
           print("this is TASK 1 - Text file tasks") #Task full name (Not abbreviated name)
           
           #use regex to extract values from TFM_task_action url parameter 
           TXT_path = re.sub(r'^.*?a_0', '', TFM_task_action.partition("a_1")[0]).strip()
           STR_data = re.sub(r'^.*?a_1', '', TFM_task_action).strip()
           LIST_data = STR_data.split(",")
           
           TASK_1 = TXT_files () #TFM task class name
           TASK_1.create_names_TXT_file (TXT_path)
           TASK_1.write_to_names_TXT (TXT_path, LIST_data)
           
       ### task 2
       case "TASK_2":
           print("this is TASK 2 - Sqlite tasks")
           
           #use regex to extract values from TFM_task_action url parameter 
           sqlite_folder = re.sub(r'^.*?a_0', '', TFM_task_action.partition("a_1")[0]).strip()
           sqlite_file = re.sub(r'^.*?a_1', '', TFM_task_action.partition("a_2")[0]).strip()
           table_name = re.sub(r'^.*?a_2', '', TFM_task_action).strip()
                   
           TASK_2 = Sqlite_tasks ()
           TASK_2.create_sqlite_file (sqlite_folder, sqlite_file)
           TASK_2.create_sqlite_table (sqlite_folder, sqlite_file, table_name)
           
       
       ### task 3
       case "TASK_3":
           print("this is TASK 3 - insert text file values into Sqlite if not already inserted")
           
           #use regex to extract values from TFM_task_action url parameter 
           TXT_path = re.sub(r'^.*?a_0', '', TFM_task_action.partition("a_1")[0]).strip()
           LIST_data = re.sub(r'^.*?a_1', '', TFM_task_action).strip()
           
                      
           TASK_3 = Process_data ()
           TASK_3.get_RAW_names (TXT_path)
           #TASK_3.get_COOKED_names()
           #TASK_3.get_TO_BE_names ()
           #TASK_3.process_TO_BE_names ()
                          
                
       case _:
           print("Please input the name of task correctly")
   

select_task ()