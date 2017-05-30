# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> Command|Function
> ---|---
> pwd|show current working directory path
> mkdir	\<name\>|create the directory in the argument
> rmdir	\<name\>|remove the directory in the argument
> touch	\<name\>|create a file in the current directory
> rm \<name\>|remove a file
> mv \<name1\> \<name2\>|rename a file
> ls -a|list all files, including private/hidden ones
> cp \<name\> \<destination\>|copying a file to another file
> man \<command\>|to open the manual of a certain command
> stat \<name\>|show info about file
> sudo \<command\>|run command as super user (has all permissions)

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> Command|Function
> ---|---
> ls|list files/directories in current directory
> ls -a| list all files, also private ones
> ls -l|list files in 'long' version, i.e. with permissions, owner etc.
> ls -lh|list files in long version with size expressed in B/KB/MB/GB/PB instead of bites
> ls -lah|list all files in long version including hidden ones with B/KB/MB/GB/PB size
> ls -t|list files sorted by time modified
> ls - Glp|list files in color mode, long mode and indicate directories by adding a / at the end of their name

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> Command|Function
> ---|---
> ls -d|displays all directories
> ls -m|displays names as comma-separated list
> ls -R|displays subdirectories as well (recursive)

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> Execute arguments. This is useful when the list of arguments for a certain command is too long. Illustration:
> ```
> find . -name *.txt
> ```
> This command finds all .txt files in the current directory, and this list can be very long. If you want to remove all these .txt files, you can feed the output of `find` to `xargs`,which will split it up in smaller lists and feed it to the command specified to its right, in the case of removal, `rm`:
> ```
> find. -name *.txt | xargs rm
> ```

