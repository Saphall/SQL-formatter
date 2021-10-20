import re
import sys
from utils.utils import *
from keywords.keywords import KEYWORDS


def uppercase(x): return x.group(1).upper()


re_replace = re.compile(r'\b({})\b'.format('|'.join(KEYWORDS)))


def SQLformat(sqlFile):
    try:
        with open(sqlFile) as input_sqlFile:
            content = input_sqlFile.read()

        with open(sqlFile, 'w') as output_sqlFile:
            output_sqlFile.write(re_replace.sub(uppercase, content.lower()))
            print(
                f'{SUCCESS}{BOLD}[+] Executed :{END} File Changed to correct SQL format!\n{SUCCESS}{BOLD}[+] SUCCESS !{END}')
    except Exception as e:
        print(f'{FAILURE}{BOLD}[-] Error:{END}', e,
              f'\n{FAILURE}{BOLD}[-] FAILURE !{END}')


if __name__ == '__main__':
    print(f'''{HEADING}{BOLD}
____ ____ _       ____ ____ ____ _  _ ____ ___ ___ ____ ____ 
[__  |  | |    __ |___ |  | |__/ |\/| |__|  |   |  |___ |__/ 
___] |_\| |___    |    |__| |  \ |  | |  |  |   |  |___ |  \ 

                                               ~ From SAPHAL
           {END}''')
    try:
        sqlFile = sys.argv[1]
        if '.sql' in sqlFile:
            SQLformat(sqlFile)
        else:
            print(
                f'{FAILURE}{BOLD}[-] Error:{END} Please select SQL file only!\n{FAILURE}{BOLD}[-] FAILURE !{END}')
    except Exception as e:
        print(f'{FAILURE}{BOLD}[-] Error:{END}', e,
              f'\n{FAILURE}{BOLD}[-] FAILURE !{END}')
        exit(0)
