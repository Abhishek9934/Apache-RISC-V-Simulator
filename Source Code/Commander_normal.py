# exec(open(r"mcgenerator.py").read())        # generate the machine code into mc file

import register_file
import PC
import memory_normal
import decoder_normal
import configme
from PyQt5.QtWidgets import QApplication
instructions_executed = 0
check_on_step = 0

def initializereg():
    for i in range(32):
        if i == 2: register_file.store_in_register(i,0x7ffffff0)
        elif i == 3: register_file.store_in_register(i,0x10000000)
        else:   register_file.store_in_register(i,0)
    memory_normal.code_stop = 0x0
    PC.PC = 0x0
    global instructions_executed,check_on_step
    instructions_executed = 0
    check_on_step = 0
    memory_normal.memory_map.clear()
    fO = open('console.txt','w+')
    fO.write(f'Everything is reset!\n')
    fO.close()

def run_button():
    initializereg()

    exec(open(r"parent_normal.py").read())  # This puts all the data and code into the memory_normal.
    PC.PC = 0x0
    global instructions_executed
    # print(memory_normal.code_stop)
    while PC.PC < memory_normal.code_stop and configme.breakflag==0:
        decoder_normal.decode(PC.PC)
        instructions_executed += 1
        QApplication.processEvents()
        

    memory_normal.print_mem_into_apache()
    memory_normal.print_code_into_apache()
    fO = open('console.txt','w+')
    fO.write(f'Assume CPI = 5\n')
    fO.write(f'Total clock cycles for program = {5*instructions_executed}\n')
    fO.close()

def step_button(C=0):
    global check_on_step
    if check_on_step == 0:
        exec(open(r"parent_normal.py").read())
        check_on_step = 1
    global instructions_executed
    if PC.PC < memory_normal.code_stop:
        decoder_normal.decode(PC.PC)
        instructions_executed += 1

    if C == 0:
        memory_normal.print_mem_into_apache()
        memory_normal.print_code_into_apache()
    fO = open('console.txt', 'w+')
    fO.write(f'Assume CPI = 5\n')
    fO.write(f'Total clock cycles for program = {5 * instructions_executed}\n')
    fO.close()


def previous_button():
    global instructions_executed
    if PC.PC > 0:
        reach_here = instructions_executed
        initializereg()
        while instructions_executed < (reach_here-1):
            step_button(C=1)
            

    memory_normal.print_mem_into_apache()
    memory_normal.print_code_into_apache()
    fO = open('console.txt', 'w+')
    fO.write(f'Assume CPI = 5\n')
    fO.write(f'Total clock cycles for program = {5 * instructions_executed}\n')
    fO.close()

# memory_normal.print_all_memory()

# register_file.print_selected_registers()
# register_file.print_all_registers()
