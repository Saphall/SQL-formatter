# SQL-formatter
```diff
+        ____ ____ _       ____ ____ ____ _  _ ____ ___ ___ ____ ____           +
+        [__  |  | |    __ |___ |  | |__/ |\/| |__|  |   |  |___ |__/           +
+        ___] |_\| |___    |    |__| |  \ |  | |  |  |   |  |___ |  \           +
+                                                                               +
+                                                        ~ From SAPHAL          +
```

This python script helps to format SQL queries at first phase i.e. uppercase the all keywords used in the sql file.

> ### Commands:

**| Multiple SQL files :**
```python
python SQLformatter.py SQL_FILE_PATH_1 SQL_FILE_PATH_2 ...
```

**| Select all SQL files :**
```python
python SQLformatter.py *.sql
```

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
- [ ]  Choose folder to format all contining sql files
- [ ]  Simple GUI : tkinter
- [ ]  Proper indentation

