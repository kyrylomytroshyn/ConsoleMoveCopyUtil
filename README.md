# ConsoleMoveCopyUtil


To use this util, you need to clone this repo and write in your console like the text bellow:

1. To copy all files from dir to dir:
```
 sudo main.py --copy --from "/tmp" --to "/youraddress" 
```

2. To move all files from dir to dir:
```
 sudo main.py --move --from "/tmp" --to "/youraddress" 
```

3. To copy file from dir to dir:
```
 sudo main.py --copy --from "/tmp/filename.format" --to "/youraddress" 
```

4. To move file from dir to dir:
```
 sudo main.py --move --from "/tmp/filename.format" --to "/youraddress" 
```

5. To move copy files with mask from dir to dir:
```
 sudo main.py --copy --from "/tmp/*.format" --to "/youraddress" 
```

6. To move move files with mask from dir to dir:
```
 sudo main.py --move --from "/tmp/*.format" --to "/youraddress" 
```

7. To do the copy with multithreading write something from examples with 
```
 --threading [num_of_threads]
```

All results of work you can see in "util_log.log".
