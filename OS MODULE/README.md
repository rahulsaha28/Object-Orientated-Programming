# OS MODULE


| NAME| MEAN |
|:-----:|:----:|
|os.getcwd()| current working directory|
|os.chdir(str)| change directory |
|os.listdir()| get the file name in the directory|
|os.makedirs(str)| creating more directory in the current directory |
|os.removedirs(str)| remove directory from the current directory|
|os.rename(str1, str2)| rename the str1 to str2|
|os.stat(str)| return an object about detail of dir str |
|os.walk(str)| return three value (dir_path, dir_name, file_name) of str dir|
|os.environ| return an obj of all environment variable|
|os.environ.get(str1)| return the string of the specific environment variable of str1|
|os.path.join(str1, str2)| join two path|
|os.path.basename('prog/p/main.py')| return main.py|
|os.path.dirname('prog/p/main.py')| return prog/p/|
|os.path.exists(str1)| check if the str1 path is exist or not|
|os.path.isdir(str)| check the str is directory or not|
|os.path.isfile(str) | check the str is file or not |



# OS module

| function name| return | get|
|:----:|:-----:|:------:|
|os.getcwd()| get current working directory ||
|os.mkdir()|make a directory | diectory name(str)|
|os.rename()|rename a directory| previous directory name(str), new name(str)|
|os.rmdir|remove a directory| directory name (str)|
|os.chdir()| change the directory from on to another | directory name(str)|
|os.listdir()| return an array of list of item in the current directory||
|os.makedirs()| create multiple directory |directory name(str)|
|os.stat()| return the information of the file in the stat()| file name(str)|
|os.walk()| return three value directory path, directory name, file name| pass directory name(str)|
|os.environ| return dictonary ||
|os.basename()| return the base name of the given name| take a file path name(str)|
|os.dirname()| return the directory name| take a file path name(str) |
|os.path.split()|return an tupple of directory name and base name |take a file path name(str)|
|os.path.exist()| return true or false if given file path is exist or not| take a file path name(str)|
|os.path.splitext()| return an tupple of file directory and file extension| take a file path name(str)|

