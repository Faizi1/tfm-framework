

from a0_items import *


#TXT_path = ../../data/raw/names.txt
#LIST_data = ['david', 'peter', 'jon', 'lucy']


def create_TXT_file (TXT_path):


   if os.path.exists (TXT_path):

      print (TXT_path + ' already exists')
      
      os.remove(TXT_path)
      
      print (TXT_path + ' is removed')
            
  
   else:

      with open(TXT_path, 'w') as f:
           pass

      print (TXT_path + ' NOT exists, is created')
      
          
#create_TXT_file (TXT_path)      



def write_to_TXT_file (TXT_path, LIST_data):


   print ('writing to the newly created TXT file')

   for data in LIST_data:
        
      with open(TXT_path, 'a+') as f:
         f.write(data)
         f.write('\n')      


#write_to_TXT_file (TXT_path, LIST_data)




def read_TXT_file (TXT_path):

   print ('read from TXT file')

   with open(TXT_path, 'r') as f:
      lines = f.readlines()
      
   return lines       
   
   
#print (read_TXT_file ('../../data/raw/names.txt'))