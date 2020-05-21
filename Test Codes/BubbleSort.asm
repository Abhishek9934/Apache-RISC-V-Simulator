.data
array: .byte 123 -5 90 -78 9 56 -91
.text
auipc x4, 65536
addi x5,x0,6 # x5=n-1
addi x6,x0,0 # x6=i
addi x7,x0,0 # x7=j
addi  x3,x0,1 # x3=j+1

Loopo: sub x8,x5,x6 # x8=n-1-i 
blt x6,x5,Loopi # condition check of outer loop
bge x6,x5,exit # if outer loop condition is false, exit the program
Loopi:blt x7,x8,I # condition check of inner loop
bge x7,x8,I2 # if inner loop cond not satisfied, terminate the inner loop
I: add x14,x4,x7 # x14 stores address of array[j]
add x15,x4,x3 # x15 stores address of array[j+1]
lb x10,0(x14) #x10=array[j]
lb x11,0(x15) # x11=array[j+1]
blt x11,x10,K 	# K- swap code
bge x11,x10,S

K: addi x13,x10,0
addi x10,x11,0
addi x11,x13,0
sb x10,0(x14) # store the swapped values in the memory
sb x11,0(x15)

S:addi x7,x7,1 # j++
addi x3,x3,1 #(j+1)++
beq x0,x0, Loopi

I2:addi x6,x6,1 #i++
addi x7,x0,0 # reset j to 0 and j+1 to 1
addi x3,x0,1
beq x0,x0, Loopo

exit: 

