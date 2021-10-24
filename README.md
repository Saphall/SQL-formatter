# SQL-formatter
```diff
+        ____ ____ _       ____ ____ ____ _  _ ____ ___ ___ ____ ____           +
+        [__  |  | |    __ |___ |  | |__/ |\/| |__|  |   |  |___ |__/           +
+        ___] |_\| |___    |    |__| |  \ |  | |  |  |   |  |___ |  \           +
+                                                                               +
+                                                        ~ From SAPHAL          +
```

This python script helps to format SQL queries at first phase **i.e. uppercase** all the keywords used in the sql file.

> ## Commands:

**| Multiple SQL files :**
```python
python SQLformatter.py  SQL_FILE_PATH_1  SQL_FILE_PATH_2  ...
```

**| Select all SQL files :**
```python
python SQLformatter.py  *.sql
```
**| Directories containig SQL files :**
```python
python SQLformatter.py  DIRECTORY_PATH_1  DIRECTORY_PATH_2  ...  
```
Combination of `SQL_FILE_PATH` and `DIRECTOEY_PATH` as arguments works fine.

## Caution:

If the column names are used same as keywords (dtype), those column names might change as well. 
e.g. 
```sql
date Date 
``` 
might change to : 
``` sql 
DATE DATE
```
and `time Time` might change to `TIME TIME`. So, try avoiding them.

## What's next:

- [x]  Multiple file_paths
- [x]  Choose directories/folders to format all contining sql files
- [ ]  Simple GUI : tkinter
- [ ]  Proper indentation

