# CS50
Notes from CS50 course: introduction to computer science

My goal is to finish this course in 25 days (Goal change, problem sets are too difficult so it took me more time than expected -> awesome revised plan, 40 days may be??). Problem sets and final project is as follow.

Syllabus:(https://docs.cs50.net/2018/x/syllabus.html)

@@@ Week 0: ++ Binary: how to represent a number in binary system (Ie: 1 is 001, 2 is 010, 3 is 011, 4 is 100, 5 is 101). Letters are stored by ASCII (Ie: H is 72, I is 73). For both ASCII and RGB, the maximum value that each character or amount of one color can be is 255, because one common standard group of bits is a byte, or 8 bits. (1 byte = 8 bits ->2^8=256, max 255 ways to represent a character).
            ++ Algorithms: step-by-step instructions on how to solve a problem.
            ++ Pseudocode: layout of a block of code intended for human to read rather than machine. (draft code)
            ++ Compiler: clang xyz.c or make xyz, then run ./xyz.out  
            ++ Other concepts: Boolean expressions. Conditions. Variables. Functions. Arrays. Threads. Events.

@@@ Week 1: <LECTURE 1>
            ++ C: int main(void): main is the standard name in C to indicate that it is the default function in a program that should be run. include is a keyword that indicates we want to include some other file in our program. (standard input/output library).
            ++ for loops
            ++ functions included in the cs50.h library. (get_char, get_double, get_float, get_int, get_long_long, get_string)
            ++ ints.c (Integer arithmetic)
            ++ // comments
            ++ floats.c (float x = get_float("x: ");)
            ++ conditions.c ( if, else if, else)
            ++ noswitch.c (if, else if, else, ==, ||, &&)
            ++ use single quotes around characters, to distinguish them from strings, which we use double quotes to indicate
            ++ a switch is another construct in C where the value of a variable is compared to various cases, and the indented code beneath a matching case will be executed.
            ++  overflow.c : integer overflow, a binary number with 8 bits 1 1 1 1 1 1 1 0. we don’t have an extra bit to the left to actually store that larger value. Number excess memory.

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

++ Variables and Scope:
Local variable (created inside a function and can only be accessed by that function).
Global variable (can be accessed by any function in the program). Declare them outside of any function, but be careful as the global variable is manipulated by a function and change it value, before it gets into the second function. Function will use a copy of local variable to perform the calculation.

++ Array:


++ Command Line Arguments: to collect cmmand line argumetns from the users
int main (int argc, string argv[]) -> 2 arguments
 interger called argc and an array of string inside [].
Argc (argument count): will store the number of command-line arguments the user typed when the program was excecuted. (It detect the space and tab between argument.
Ie: ./greedy.c -> argc =1
./greedy.c 1029 cs50 -> argc = 3
Argv (argument vector):
This array of strings stores one string per element. First element can be accessed through argv[0], the last one is argv[argc -1 ]. (because we index from 0). Argv always stores string (even the input is interger) so you need to use atoi from <stdlib.h> library to convert them.
If you tried to acess argv[3], don’t know what is really there.




        <LECTURE 3>: Algorithms
        ++ Strings: write initials.c to extract initials from a string (array of characters), assuming that the initials is capital letter. Max 3 initials, the 4th will be NUL character (\0). Use the for loop to iterate through the string, and store the capital letters in "initials" array.
        We need a length variable to keep track of characters we have seen already, so we can store each character in the right index of initials and terminate it correctly.

        ++ Searching: find a number in a random ordered number array.

        //Linear search: open randomly each door, it would take n step to find it (n was the numbers of number in our array). Pseudocode look like this:
        for each element in array
              if element you're looking for
              return true
        return false

        //Binary search: look at the middle and start searching in haft left or haft right. We are dividing the problem in half each time, so we will have fewer steps before we find our number, or complete the algorithm.

        look at middle of sorted array
        if element you're looking for
            return true
        else if element is to left
            search left half of array
        else if element is to right
            search right half of array
        else
            return false


        ++ Sorting:
        //insertion sort algorithm: at each step, we look at the a pair of numbers, one at at time, and swap them if they are in the wrong order.

        for i from 1 to n-1
              call 0'th through i-1'th elements the "sorted side"
              remove i'th element
              insert it into sorted side in order

        //bubble sort algorithm:

        repeat until no swaps
            for i from 0 to n-2
                if i'th and i+1'th elements out of order
                    swap them

        //selection sort algorithm:

        for i from 0 to n-1
          find smallest element between i'th and n-1'th
          swap smallest with i'th element

        ++ Running Time:

        ++ Merge Sort:







@@@ Week 2: <LECTURE 3>:



++++++++++++++++++++++++
++++ Note from Shorts:
++++++++++++++++++++++++

++ Computational Complexity: need to understand algorithms and how they process data. With an efficient algorithm, we can minimize the amount of resources we have to deal with it. (write clean code, as short as possible. Since dataset is getting bigger and bigger -> require more RAM, CPU to deal with it).
Complexity of an algorithm: worst-case scenario (O) and best-case scenario (Ω). As we add more data point to the array, how much time it take to actually finish the algorithm?

O(1): constant time
O(log n): logarithmic time
O(n): linear time
O(n log n): linearithmic time
O(n^2): quadratic time
O(n^c): polynomial time
O(c^n): exponential time
O(n!): factorial time
O(∞): infinite time


++ Selection sort: sort left to right
Algorithm: find the smallest unsort element and add it to the end of the sorted list.
Pseudocode: 
-	Repeat until no unsorted elements remain:
* Search for the unsorted part of the data to find the smallest value
* Swap the smallest found value with the first element of the unsorted part
Worst-case scenario (O(n^2)): we have to iterate over each of the n elements of the array (to find the smallest unsorted element) and we must repeat this process n times, since only one element get sorted on each pass. 

Best-case scenario (Ω(n^2)): same as worst-case as we can only sure the array is sorted if we go through this process for all the elements.

++ Bubble sort: sort right to left
Algorithm: move higher valued elements generally towards the right and lower value elements generally toward the left.
Pseudocode: 
-	Set swap counter to a non-zero value
-	Repeat until the swap counter is 0:
* Reset swap counter to 0
* Look at each adjacent pair
	//If two adjacent elements are not in order, swap them and add one to the swap counter

Worst-case scenario (O(n^2)): the array is in reverse order; we have to “bubble” each of the n elements all the way across the array, and since we can only fully bubble one element into position per pass, we must do this n times.
Best-case scenario (Ω(n)): the array is already perfectly sorted, and we make no swaps on the first pass.

++ Insertion sort: 
Algorithm: build your sorted array in place, shifting elements out of the way if necessary to make roomsas you go.
Pseudocode:
-	Call the first element of the array “sorted”
-	Repeat until all element are sorted:
// Look at the next unsorted element. Insert into the “sorted” portion by shifting the requisite number of elements.  

Worst-case scenario (O(n^2)): the array is in reverse order; we have to shift each of the n elements n position each time we make an insertion. 
Best-case scenario (Ω(n)): the array is already perfectly sorted, and we simply keep moving the line between “unsorted” and “sorted” as we examine each element.

++ Linear sort: 
Algorithm: iterate across the array from left to right, searching for a specified element.
Pseudocode:
-	Repeat, starting at the first element
•	If the first element is what you are looking for (the target), stop.
•	Otherwise, move to the next element. 

Worst-case scenario (O(n)): we have to look through the entire array of n elements, either because the target element is the last element of the array or doesn’t exist in the array at all. 
Best-case scenario (Ω(1)): the target element is the first element of the array, so we can stop looking immediately after we start.

++ Binary search: 
Algorithm: divide and conquer, reducing the search area by haft each time, trying to find target number. In order to leverage this power, however, our array must first be sorted, else we can’t make assumptions about the array’s contents.

Pseudocode:
-	Repeat until the (sub) array is of size 0:
•	Calculate the middle point of the current (sub) array
•	If the target is at the middle, stop
•	Otherwise, if the target < the one at middle, repeat, changing the end point to be just in the left of the middle.
•	Otherwise, if the target > the one at middle, repeat, changing the end point to be just in the right of the middle.

Worst-case scenario (O(log(n)): have to divide a list of n elements in haft repeatedly to find the target element, either because the target element will be found at the end of the last division or doesn’t exist in the array at all.

Best-case scenario (Ω(1)): the target is at the midpoint -> stop immediately after we start.

++ Algorithm summary:
a.	Selection sort: find the smallest unsorted element in the array and swap it with the first unsorted of that element of that array.
b.	Bubble sort: swap adjacent pairs of elements if they are out of order, effectively “bubbling” larger elements to the right and the smaller ones to the left.
c.	Insertion sort: process once through the array from left to right, shifting elements as necessary to insert each element into its correct place.
d.	Merge sort: split the full array into subarray, then merge those subarrays back together in the correct order.
e.	Linear seach: iterate across the array from left to right, trying to find the target element.
f.	Binary search: given a sorted array, divide and conquer by systematically eliminating haft of the remaining elements in the search for targeted element. 


++ Recursion: a function that calls itself as part of the execution. So it make the code look elegant and short.
Factorial func (n!)
Fact(n) = n * fact(n-1)
Recursive definition: you need a base case to stop the recursion, otherwise it will run forever. Then recursive case.
// Example is single base case 
int fact (int n)
{
	// base case (fact(1)
	// recursive case (n * fact(n-1))
}

// Example is multiple base cases: Fibonacci number
// Example of multiple recursive cases: Collatz conjecture 



++ Merge sort:
Pseudocode:
-	Sort the left haft of the array (assuming n>1)
-	Sort the right haft of the array (assuming n>1)
-	Merge the two halves together.
Worst-case scenario (O(n log n)): we have to split n elements up and then recombine them, effectively doubling the sorted subarrays as we build them up. (combing sorted 1-element arrays into 2-element arrays, combining sorted 2-element arrays into 4-element arrays…)

Best-case scenario (Ω(n log n)): the array is already perfectly sorted. But we still have to split and recombine it back together with this algorithm. 


++ GDB (the GNU DeBugger): If you work in the command line
-	Type gdb <program name>
-	b [function name, line number] (to pause at certain line and wait for further input)
-	 r [command – line arguments]

n: step forward one block of code
s: step forward one line of code
p[var]: prints out the value of the variable given
info locals: prints out the value of all local variables
bt: shows you what series of function calls have led you to the current point in the program. (backtrace).
q: quit


@@@ Week 3:

@@@ Week 4:

@@@ Week 5:
