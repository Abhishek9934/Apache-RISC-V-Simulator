import lexical_analyzer
import Instruct_nd_Variable_Names


def main():
    
    instruct_list, data_list = lexical_analyzer.main()
    l = Instruct_nd_Variable_Names.Instruct_names
    fileObject2 = open(r'BasicCode.txt','w+')

    for i in instruct_list:
        if i.operation== 'add' or i.operation== 'and' or i.operation== 'or' or i.operation== 'mul' or i.operation== 'div' or i.operation== 'rem' or i.operation== 'xor' or i.operation== 'sub' or i.operation== 'srl' or i.operation== 'sra' or i.operation== 'sll' or i.operation== 'slt':
            fileObject2.write(f"{i.operation} x{i.reg1} x{i.reg2} x{i.reg3}\n")
        elif i.operation == 'addi' or i.operation == 'andi' or i.operation == 'ori' or i.operation == 'jalr' or i.operation == 'lb' or i.operation == 'lh' or i.operation == 'lw' or i.operation == 'ld':
            fileObject2.write(f'{i.operation} x{i.reg1} x{i.reg2} {i.immediate}\n')
        elif i.operation == 'sb' or i.operation == 'sh' or i.operation == 'sw' or i.operation == 'sd':
            fileObject2.write(f'{i.operation} x{i.reg1} x{i.reg2} {i.immediate}\n')
        elif i.operation == 'beq' or i.operation == 'blt' or i.operation == 'bge' or i.operation == 'bne':
            x = l[i.jumptolabel] - int(i.address,16)
            fileObject2.write(f'{i.operation} x{i.reg1} x{i.reg2} {x}\n')
        elif i.operation == 'lui' or i.operation == 'auipc':
            fileObject2.write(f'{i.operation} x{i.reg1} {i.immediate}\n')
        elif i.operation == 'jal':
            x = l[i.jumptolabel] - int(i.address, 16)
            fileObject2.write(f'{i.operation} x{i.reg1} {x}\n')

    fileObject2.close()

