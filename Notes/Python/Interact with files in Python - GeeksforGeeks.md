Last Updated : 04 Jan, 2023

Python too supports file handling and allows users to handle files i.e., to read, write, create, delete and move files, along with many other file handling options, to operate on files. The concept of file handling has stretched over various other languages, but the implementation is either complicated or lengthy, but alike other concepts of Python, this concept here is also easy and short. The main focus of this article will be on the following topics.

-   [Creating a file][1]
-   [Reading from file][2]
-   [Writing to file][3]
-   [Moving file][4]
-   [Deleting a file][5]

## Creating a File

The first step in using a file instance is to open a disk file. In any computer language this means establishing a communication link between your code and the external file. To create a new file I/O classes provides the member function open(). **Syntax:**

```
open(filename, mode)
```

Here the mode refers to the Access Mode. Access modes govern the type of operations possible in the opened file. It refers to how the file will be used once it’s opened. These modes also define the location of the File Handle in the file. File handle is like a cursor, which defines from where the data has to be read or written in the file. There are 6 access modes in python.

-   **Read Only (‘r’):** Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises I/O error. This is also the default mode in which file is opened.
-   **Read and Write (‘r+’):** Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exists.
-   **Write Only (‘w’):** Open the file for writing. For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exists.
-   **Write and Read (‘w+’):** Open the file for reading and writing. For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
-   **Append Only (‘a’):** Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
-   **Append and Read (‘a+’):** Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

**Example:** Suppose the folder looks like this – ![creating-a-file](https://media.geeksforgeeks.org/wp-content/uploads/20191209114857/creating-a-file-input.png) 

-   Python3

`file1` `=` `open``("MyFile.txt","w``+``")`

**Output:** ![creating-a-file](https://media.geeksforgeeks.org/wp-content/uploads/20191209115002/creating-a-file-output.png) In the above example, open() function along with the access mode ‘w+’ is used to open a file in writing and reading mode but if the file doesn’t exist in the computer system then it creates the new file. **Note:** To know more about creating a file [click here][6].

## Reading from File

There are three ways to read data from a text file.

1.  **read():** Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file.

```
File_object.read([n])
```

1.  **readline():** Reads a line of the file and returns in form of a string.For specified n, reads at most n bytes. However, does not reads more than one line, even if n exceeds the length of the line.

```
File_object.readline([n])
```

1.  **readlines():** Reads all the lines and return them as each line a string element in a list.

```
File_object.readlines()
```

**Note:** ‘\\n’ is treated as a special character of two bytes. 

-   Python3

`file1` `=` `open``("myfile.txt", "w")`

`L` `=` `["This` `is` `Delhi \n", "This` `is` `Paris \n", "This` `is` `London \n"]`

`file1.write("Hello \n")` 

`file1.writelines(L)`

`file1.close()` 

`file1` `=` `open``("myfile.txt", "r``+``")`

`print``("Output of Read function` `is` `")`

`print``(file1.read())`

`print``()`

`file1.seek(``0``)`

`print``("Output of Readline function` `is` `")`

`print``(file1.readline())`

`print``()`

`file1.seek(``0``)`

`print``("Output of Read(``9``) function` `is` `")`

`print``(file1.read(``9``))`

`print``()`

`file1.seek(``0``)`

`print``("Output of Readline(``9``) function` `is` `")`

`print``(file1.readline(``9``))`

`print``()`

`file1.seek(``0``)`

`print``("Output of Readlines function` `is` `")`

`print``(file1.readlines())`

`print``()`

`file1.close()` 

**Output:**

```
Output of Read function is
Hello
This is Delhi
This is Paris
This is London


Output of Readline function is
Hello


Output of Read(9) function is
Hello
Th

Output of Readline(9) function is
Hello


Output of Readlines function is
['Hello \n', 'This is Delhi \n', 'This is Paris \n', 'This is London \n']
```

**Note:** To know more about reading from file [click here][7].

## Writing to File

There are two ways to write in a file.

1.  **write():** Inserts the string str1 in a single line in the text file. File\_object.write(str1)
2.  **writelines():** For a list of string elements, each string is inserted in the text file. Used to insert multiple strings at a single time. File\_object.writelines(L) for L = \[str1, str2, str3\]

**Note:** ‘\\n’ is treated as a special character of two bytes. 

-   Python3

`file1` `=` `open``(``'myfile.txt'``,` `'w'``)`

`L` `=` `["This` `is` `Delhi \n", "This` `is` `Paris \n", "This` `is` `London \n"]`

`s` `=` `"Hello\n"`

`file1.write(s)`

`file1.writelines(L)`

`file1.close()`

`file1` `=` `open``(``'myfile.txt'``,` `'r'``)`

`print``(file1.read())`

`file1.close()`

**Output:**

```
Hello
This is Delhi
This is Paris
This is London
```

**Note:** To know more about writing to file [click here][8].

## Moving File

This can be achieved using shutil.move() function from **shutil module**. shutil.move() method Recursively moves a file or directory (source) to another location (destination) and returns the destination. If the destination directory already exists then src is moved inside that directory. If the destination already exists but is not a directory then it may be overwritten depending on os.rename() semantics. **Example:** Suppose the directory looks like this – ![python-move-files](https://media.geeksforgeeks.org/wp-content/uploads/20191209120616/python-move-files-and-dir-7.png) **Inside G:** ![python-move-files](https://media.geeksforgeeks.org/wp-content/uploads/20191209120640/python-move-files-and-dir-8.png) 

-   Python3

`import` `shutil`

`source` `=` `"D:\Pycharm projects\gfg\Test\Test4.txt"`

`destination` `=` `"D:\Pycharm projects\gfg\Test\G"`

`dest` `=` `shutil.move(source, destination)`

**Output:** ![python-move-files](https://media.geeksforgeeks.org/wp-content/uploads/20191209120917/python-move-files-and-dir-9.png) **Note:** To know more about moving files [click here][9].

## Deleting a File

os.remove() method in Python is used to remove or delete a file path. This method can not remove or delete a directory. If the specified path is a directory then OSError will be raised by the method. **Example:** Suppose the file contained in the folder are: ![python delete file](https://media.geeksforgeeks.org/wp-content/uploads/20191125183910/python-os.remove-input.png) We want to delete the file1 from the above folder. Below is the implementation. 

-   Python3

`import` `os` 

`file` `=` `'file1.txt'`

`location` `=` `"D:``/``Pycharm projects``/``GeeksforGeeks``/``Authors``/``Nikhil``/``"`

`path` `=` `os.path.join(location,` `file``)` 

`os.remove(path)` 

**Output:** ![python delete file](https://media.geeksforgeeks.org/wp-content/uploads/20191125184203/python-os.remove-output.png) **Note:** To know more about deleting files [click here][10].

  
  

[1]: https://www.geeksforgeeks.org/interact-with-files-in-python/#create
[2]: https://www.geeksforgeeks.org/interact-with-files-in-python/#read
[3]: https://www.geeksforgeeks.org/interact-with-files-in-python/#write
[4]: https://www.geeksforgeeks.org/interact-with-files-in-python/#move
[5]: https://www.geeksforgeeks.org/interact-with-files-in-python/#delete
[6]: https://www.geeksforgeeks.org/create-an-empty-file-using-python/
[7]: https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/
[8]: https://www.geeksforgeeks.org/writing-to-file-in-python/
[9]: https://www.geeksforgeeks.org/how-to-move-files-and-directories-in-python/
[10]: https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/