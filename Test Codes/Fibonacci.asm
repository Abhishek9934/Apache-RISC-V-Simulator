# fib(0)=0
# fib(1)=1
# fib(n) stored in register x11

addi x10,x0,10	# x10=n
addi x7,x0,1

jal x1,fib
beq x0,x0, exit

fib: addi sp,sp,-8
sw x1,0(sp)
blt x7,x10,L1
addi x11,x10,0
addi sp,sp,8
jalr x0,0(x1)

L1: addi x10,x10,-1
jal x1,fib
sw x11,4(sp)	# fib(n-1) stored in stack	

addi x10,x10,1

addi x10,x10,-2
jal x1,fib

addi x10,x10,2
lw x15,4(sp)
add x11,x11,x15	# x11=fib(n-2). so here x11=fib(n)=fib(n-1)+fib(n-2)

lw x1,0(sp)
addi sp,sp,8
jalr x0,0(x1)

exit:

