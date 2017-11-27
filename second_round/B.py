l,a=map(str,input().split())
i=0
c=0
l=int(l)
a+='00000'
while i<l-1:
    if a[i]=='G' and a[i+1]=='G':
        i+=1
        continue
    else:
        c+=1
    i+=1
print(c)
'''
Problem : Fill the Boxes 

Statement: 
There are N horizontally adjacent boxes on a sheet. Raju has to fill them(starting from the left) by using
two colors: Red and Green. 
If he picks up Green color, he can fill one or more adjacent boxes while if he  picks up red color, he can 
fill only one box and after that he has to place the color back. It is pre­decided  that which box will be
filled with which color. You have to find the minimum no. of times Raju will have to  place the picked up 
color back in order to match the given pattern. Raju can't re­arrange the position of the  boxes.

Input Format: 
First line contains a Number and String delimited by whitespace where, 
1. First Number is number of boxes 
2. Second String is the color pattern

Output Format: 
The minimum no. of times Raju will have to place the picked up color back in order to match the given pattern. 

Constraints:
1. If he picks up Green color, he can fill one or more adjacent boxes while if he picks up red color, he can fill only one box. 
2. All the boxes will have to be filled sequentially.

Sample Input and Output:
--------------------------------------------------------------------------------------------------+
SNo. |  Input    | Output   |                    Explaination                                     |
-----+-----------+----------+---------------------------------------------------------------------+
1    |  5 RGGRR  |  3       |  First Raju picked Red color for filling and next color is          |
     |           |          |  Green so he placed red color back so count= 1 Raju picked          |
     |           |          |  Green color and filled next two boxes with Green and placed        |
     |           |          |  Green color back, now count =2 Again Raju picked Red color and     |
     |           |          |  filled the box and placed it back, now count=3 Again Raju picked   |
     |           |          |  Red color filled the box and as it is last box no need to place    |
     |           |          |  it back, so final count=3                                          |
-----+-----------+----------+---------------------------------------------------------------------+
2    |  5 RGGGG  |  1       |  First Raju picked R color for filling and next color is            | 
     |           |          |  G so he placed red color back so count= 1 Raju picked G            |
     |           |          |  color filled next 4 boxes with G color, so final count =1          |
-----+-----------+----------+---------------------------------------------------------------------+
'''