getting around------
ls - list out the contents of the current directory
cd - change to another directory
./ - short for "here"
../ - short for "the folder right above here"
~/ - short for the home folder of the currently logged in user

mv - move a file from one place to another
	mv ~/my_text.txt ~/Documents/
	mv ~/my_text.txt ~/my_doc.txt
cp - copy a file or folder from one place to another
	cp ./my_text.txt ~/Documents/
	- now there are 2 copies of my_text.txt
	one in the home folder, and one in ~/Documents/
rm - remove a file or folder
	rm ~/my_text
	- with great power comes great responsibility!
ln - create a shortcut to a file or folder

text editors-----
less
vim
nano

these all let you both read and write to files

the all-powerful pipe-----
| the "pipe" character allows you to chain commands together
command 1 | command 2
Here command 1 does soemthing, and when it is finished, like an
assembly line, it passes it completed work to the second command
for further processing

ls - a | grep .git - search for all files and then filter them
			for files matching the pattern .git

reading files-----
cat - conCATenate to files or stdout todgether
	cat November_todos.txt December_todos.txt
head - view the first few lines of a file
tail - view the last few lines at the end of a file
wc - count the number of words

samurai level bash-----
grep - pattern matching often combined with other commands
sed - stream editor allowing you to make changes to a file by pattern
awk - a mini programming language to manipulate text
regex - a pattern description mini programming language

redirection-----
> - send the output of the left side to the file on the right
	./my_text.txt > ./other_file.txt

>> - append the output to the right hand side

both > and >> can be reversed

sort < ./phone_numbers.txt

getting help-----
man <command> - bring up the manual page for a given command or program
info <command> - similar to man, only returns the info page
type <thing> - show the type of something
whatis <command> - brief description of a command
apropos <something> - search man pages for something

permissions-----
chmod - change the permissions of a file
chown - change the ownership of a file

process control-----
ps - list all processes running
top - list all top running processes
	- these are commonly filtered and sorted with other commands
bg - move a task to the background
fg - bring task to the foreground
kill - terminate a task
	- this is usually done by PID (process ID)

compression and encryption-----
*zip - compress a file using:
	- gzip, zip, or bzip
		- this yeilds a compressed .gz, .zip, or .bz file
*unzip - decompress a file
	- gunzip, unzip, bunzip
		- this takes a zip files and yeilds a decompressed file
tar - create or extract archive files containing many files
	- tar -cf archive.tar file1, file2, file3
	- tar -xf archive.tar
gpg - encrypt and decrypt files
	- gpg -c my_text.txt (encrypt)
	- gpg my_text.txt.gpg (decrypt)

shells-----
sh/bash - launches a shell or used to execute bash script files
ssh - create a encrypted remote shell session on another machine
	- ssh grant@myserver.net
scp - copies files to remote machines with encryption
ftp - copies files to remote machines without any encryption (clear text)

other helpful stuff-----
diff - show the differences between 2 files
	- diff file1 file2
df/du - shows stats about file size
history - show your recently used bash commands

finding things-----
find - locate files by pattern
locate - find the easy way

sudo - do something as the root user
su - switch user accounts
apt - package manager for Debian-based linux distributions
	- sudo apt-get update
	- sudo apt-get install
	- sudo apt-get remove

neat keyboard shortcuts-----
ctrl+e - go to the end of the line
ctrl+l - clear the screen
ctrl+a - go to the start of the line
ctrl+d - delete a character
ctrl+k - cut a line of text from the beginning
ctrl+u - uncut (paste) the text in the buffer to the current line
alt+b - go back to the beginning of a word
ctrl+w - delete the last word
alt+c - capitalize the current word
alt+f - go forward one word
