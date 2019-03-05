'''
Process Tran2 records from csv file
'''

import csv
from pathlib import Path
from io import StringIO, SEEK_SET

from MyUtils import printnl

# def Reset_Csv_Pos(a_csv_r, f):
#     f.seek(0)

io_string = '''
    1, 3, 5.63    , 89    
    25, 3, 6.22, 9
    '''
trans = str.maketrans('', '', ' \t')
strip_io_string = io_string.translate(trans)
# print(io_string, strip_io_string)
#  iostring_obj = StringIO(strip_io_string) #StringIO obj using in place of file obj
##or
##############################
iostring_obj = StringIO()
print(iostring_obj.write(strip_io_string))  #25 chars written
print(iostring_obj.tell())  #showing 25 which is the end.
# iostring_obj.seek(0, SEEK_SET)  #after write(), pos cursor at the end of StringIO obj, need seek() to the top
##############################
csv_r = csv.reader(iostring_obj, skipinitialspace=True)
for item in csv_r:
    print(csv_r.line_num, item)
iostring_obj.close()    #need to close as if file obj

# csv_filename = Path('C:\Documents and Settings\hal\Desktop\Py CSV\Tran2-20190304-check-5.csv')
#  
# with csv_filename.open(encoding='utf-8') as f:
#     csv_r = csv.reader(f)
#     for item in csv_r:
#         print(csv_r.line_num, item)
