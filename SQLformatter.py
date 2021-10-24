import re
import os
import sys
from utils.utils import *
from keywords.keywords import KEYWORDS


def uppercase(x): return x.group(1).upper()


re_replace = re.compile(r'\b({})\b'.format('|'.join(KEYWORDS)))


def SQLformat(sqlFile):
    """
    This function helps to uppercase the keywords used in sql file.
    param: sqlFile: File path of sql file.
    """
    try:
        with open(sqlFile) as input_sqlFile:
            content = input_sqlFile.read()

        with open(sqlFile, 'w') as output_sqlFile:
            output_sqlFile.write(re_replace.sub(uppercase, content.lower()))
            print(
                f'{SUCCESS}{BOLD}[INFO]:{END} {FILE}"{sqlFile}"{END} --> {SUCCESS}done.{END}')
    except Exception as e:
        print(
            f'{FAILURE}{BOLD}[Error]:{END} {FILE}{BOLD}"{sqlFile}"{END}\n   --> {FAILURE}', e)


if __name__ == '__main__':
    print(f'''{HEADING}{BOLD}
____ ____ _       ____ ____ ____ _  _ ____ ___ ___ ____ ____ 
[__  |  | |    __ |___ |  | |__/ |\/| |__|  |   |  |___ |__/ 
___] |_\| |___    |    |__| |  \ |  | |  |  |   |  |___ |  \ 

                                               ~ From SAPHAL
           {END}''')
    try:
        # print(len(sys.argv)-1)
        for i in range(len(sys.argv)-1):
            sql_file_path = sys.argv[i+1]
            # print(sqlFile)
            if '.sql' in sql_file_path:
                SQLformat(sql_file_path)
            elif os.path.isdir(sql_file_path):
                print(f'{SUCCESS}{BOLD}[INFO]:{END} {FILE}{BOLD}"{sql_file_path}"{END} :: directory')
                files = os.listdir(sql_file_path)
                # print(files)
                # print(len(files))
                for i in range(len(files)):
                    if '.sql' in files[i]:
                        SQLformat(sql_file_path+'/'+files[i])
                print(f'{SUCCESS}   ==> directory processed.{END}')
            else:
                print(
                    f'{FAILURE}{BOLD}[Error]:{END} {FILE}{BOLD}"{sql_file_path}"{END}\n   --> {FAILURE}Select valid SQL file path.')
        print()
    except Exception as e:
        print(f'{FAILURE}{BOLD}[Error]:{END}{FAILURE}', e, '\n')
        exit(0)
