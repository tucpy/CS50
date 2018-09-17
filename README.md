# CS50
Notes from CS50 course: introduction to computer science

My goal is to finish this course in 25 days.Problem sets and final project is as follow.

Syllabus:(https://docs.cs50.net/2018/x/syllabus.html)

@@@ Week 0: ++ Binary: how to represent a number in binary system (Ie: 1 is 001, 2 is 010, 3 is 011, 4 is 100, 5 is 101). Letters are stored by ASCII (Ie: H is 72, I is 73). For both ASCII and RGB, the maximum value that each character or amount of one color can be is 255, because one common standard group of bits is a byte, or 8 bits. (1 byte = 8 bits ->2^8=256, max 255 ways to represent a character).
            ++ Algorithms: step-by-step instructions on how to solve a problem.
            ++ Pseudocode: layout of a block of code intended for human to read rather than machine. (draft code)
            ++ Compiler: clang xyz.c or make xyz, then run ./xyz.out  
            ++ Other concepts: Boolean expressions. Conditions. Variables. Functions. Arrays. Threads. Events.

@@@ Week 1: <LECTURE 1>
            ++ C: int main(void): main is the standard name in C to indicate that it is the default function in a program               that should be run. include is a keyword that indicates we want to include some other file in our program.                   (standard input/output library). 
            ++ for loops
            ++ functions included in the cs50.h library. (get_char, get_double, get_float, get_int, get_long_long,                       get_string)
            ++ ints.c (Integer arithmetic)
            ++ // comments
            ++ floats.c (float x = get_float("x: ");)
            ++ conditions.c ( if, else if, else)
            ++ noswitch.c (if, else if, else, ==, ||, &&)
            ++ use single quotes around characters, to distinguish them from strings, which we use double quotes to indicate
            ++ a switch is another construct in C where the value of a variable is compared to various cases, and the                   indented code beneath a matching case will be executed.
            ++  overflow.c : integer overflow, a binary number with 8 bits 1 1 1 1 1 1 1 0. we don’t have an extra bit to               the left to actually store that larger value. Number excess memory.
            <LECTURE 2>
            ++
            ++
            ++
            ++
            ++
++++++++++++++++++++++++
++++ Note from Shorts:
++++++++++++++++++++++++

++ Command line: cd, ls, pwd, mkdir (make a new folder), copy file: cp <source> <destination>, copy folder: cp -r <source> <destination>, rm -r, rename a file: mv <old name> <new name>.
Other common command: chmod, ln, touch, rmdir, man, diff, sudo, clear, telnet

++ Data types: only exist in low-level language like C. In high-level language like PHP and JavaScript, you don’t have to declare data types of a variable, it will do it for you. 
//int = 4bytes=32bits. Range from -2^31 to 2^31-1 (2 billion)
//unsigned int = a qualifier applied to double the positive range of var of that type (no negative value allowed). Range from 0 to 2^31-1 (4 billion)
//char = 1 byte=8bits. Range from -127(2^8) to 127(2^8-1). Ie: A is 65, a is 97. 0 is 48. 
//float = 4bytes =32 bits. Float has precision limitation as we only has 32 bits to work with, and a float number = 1.8374697 (int 1 and 0.8374697 float).
//double =8bytes =64 bits. Double also called real number. Store floating-point value more precise. 

++ Type: void means a function doesn’t return a value. For ex: printf (print something on the screen, don’t actually store anything). 

++ bool (in cs50.h), hold 2 value, true and false. 
++ string (in cs50.h), store a series of character (a word, a sentence)

++ create a variable : int number; // int height, width; // char letters = “H”;


++ Operators:
Arithmetic operators: +, -,*,/,%, Moduler (%): when you want to use random number generate from rand function, but only want from 0-20, you can use % to get the reminder of any huge random number generated. 

x *= 5 (x = x*5), x++ (x=x+1), x--(x=x-1)

Boolean expression: used to compare value, true or false. In C, 0 is false and non-zero is true. &&, ||, !(not), <, <=, >, >=, ==, !=, 

++ Conditional statements:
if (boolean-expression) { } 
if (boolean-expression) { }  else {}
if (boolean-expression) {} else if {} else {}

switch (need a break after every condition as if you don’t break, it will print everything regardless the user’s input (“fall through” each case)). 

int x= (expr) ? 5 : 6 // this is a short form of if else. If x==true, x=5 else x=6

++ Loops: 
while (true) {} – infinite loop, hit Ctrl+C to kill program
while (boolean-expr) {}
//while loop is pretty useful when you design a game and want your sprite to move all the time because you don’t know when the player stop playing the game.

do {} while (boolean-expr); // do something at once, then process to check the Boolean expression. 
//do while loop is useful when you prompt the user for input, until they provide what you want. 

for (int i = 0; i<50; i++) {}
for (start; expr; increment) {}

++ Debugging: help50 make file, eprintf(), debug50 ./file

++ Function: function_name(input 1, input2, inputn, output)
Why function? Organization, simplification, reusability.
Function is declared at the top of the program, even before main(). 
return-type name (argument-list);
return-type: what kind of variable the function will output 
name : name of your function
argument-list: input with comma, type and name of each input.
Ex: int add_two_ints(int a, int b);
      float multiply_two_floats (float a, float b);
      float multiply_two_floats (double a, double b);

float mult_two_floats (float a, float b);
{
	float product = x* y;
	return product;
}

float mult_two_floats (float a, float b);
{
	return  x* y;
}

int add_two_ints(int a, int b);
{ 
	Int sum; //declare variable
	Sum = a + b; //calculate input
return sum; //give result back
}




      

@@@ Week 2:

@@@ Week 3:

@@@ Week 4:

@@@ Week 5:


