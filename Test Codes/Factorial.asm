addi x10,x0, 9	# x10=7=n
addi x7,x0, 1	# x7=1

jal x1,fact
beq x0,x0, exit

fact: addi sp,sp,-8
sw x1,4(sp)	# return address of fact that called this fact
sw x10,0(sp)
blt x7,x10,L1
addi x11,x0,1	# x11-	return value
addi sp,sp,8
jalr x0,0(x1)

L1: addi x10,x10,-1
jal x1,fact

# TAIL STARTS HERE
lw x10,0(sp)
mul x11,x11,x10
lw x1,4(sp)
addi sp,sp,8
jalr x0,0(x1)

exit: