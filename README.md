# password_generator
A program to generate a random string of characters, including, upper, lower, special characters, and integers, presumably used for passwords. 

The program does not primarily use `random`, but rather the more secure `secrets` module that uses data collected from the hardware. Therefore, it should be less deterministic, and more truly random. 

**Version 1.0** is a command line tool.

**Version 2.0** will be a graphical user interface tool. 
