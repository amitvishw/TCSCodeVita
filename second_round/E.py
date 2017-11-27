def baseN(num,b,numerals="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
n=int(input())
f=input()
p=int(input())
s=''
for i in range(2,37):
    t=baseN(n,i)
    #print(i,baseN(n,i))
    if len(t)>=p:
        a=t[::-1]
        if a[p]==f:
            s+=str(i)+" "
print(s)

''' 
Problem : Base, Face and Place Values  

Statement: 
Numbers  when  represented  in  decimal  system  have  Base  Value 10.  The  denominations  i.e.  Units, Tens, Hundreds, 
Thousands etc. are its Place Values. The actual numbers between 0 to 9 are the Face values.  It is easy to see that as the 
Base Value changes, both Face and Place Values will also change.  For the purpose of the program, assume bases up to 36 with 
face values one of the following:   
0  
1  
2  
. 
. 
.
9  
A (value 10 in base 10)  
B  
. 
. 
. 
Z (value 35 in base 10)

Your task is to write a program to find out base values for which a given number expressed in decimal system has the desired 
face value with a given place value 

Example: 
Find which bases represent 56 in a manner where Face Value 3 is found in Place Value 1
Inputs in decimal (N) = 56 Face Value (F) = 3 Place Value (P) =1
Base Value of 56 in given Base 
Base-2 111000 
Base-3 2002 
Base-4 320 
Base-5 211 
Base-6 132 <-
Base-7 110 
Base-8 70 
Base-9 62 
Base-10 56 
Base-11 51 
Base-12 48 
Base-13 44 
Base-14 40 
Base-15 3B <-
Base-16 38 <-
Base-17 35 <- 
Base-18 32 <-
Base-19 2I 
Base-20 2G 
Base-21 2E 
Base-22 2C 
Base-23 2A 
Base-24 28 
Base-25 26
Base-26 24 
Base-27 22 
Base-28 20 
Base-29 1R 
Base-30 1Q 
Base-31 1P 
Base-32 1O 
Base-33 1N 
Base-34 1M 
Base-35 1L 
Base-36 1K
The Rows marked are the ones where Face Value is 3 in Place Value 1. Hence Base 6, 15, 16, 17 and 18 are the required answers. 

Input Format:  
1. First line of input is decimal number N 
2. Second line of input is Face Value F. Can be a number or alphabet (in capital letter) 
3. Third line of input is Place Value P

Output Format: 
Print base values for which a given number expressed in decimal system has the desired face value with a given place value.
All output values should be delimited by whitespace character. 

Constraints:

1. 0 < N < 10^19 
2. F can be [(0-9) or (A-Z)] 
3. 0 <= P <= length of the number in base value 36

Sample Input and Output:
-------------------------------+
SNo. |  Input 	|    Output    |
-----+----------+--------------+
1    |	56      | 6 15 16 17 18|
     |	3       |              |
     |	1       |              |
-----+----------+--------------+
2    |  50      | 18 36        |
     |  E       |              |
     |  0	    |              |
-----+----------+--------------+            
'''
