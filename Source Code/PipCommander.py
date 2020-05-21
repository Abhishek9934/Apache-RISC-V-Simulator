#exec(open(r"mcgenerator.py").read())        # generate the machine code into mc file
# COMMENT it while running Apache


import register_file
import PC
import memory
import decoder
import configme
from PyQt5.QtWidgets import QApplication
import EXEC_instruct
import executed_information

instructions_executed = 0
check_on_step = 0
decoded_result = (-1,-1,-1,-1,0,-1)
IR = ""
r_index = m_index = m_type = m_read = -1
r_value = m_value = 0
opc = -1
cycles = 0      # append at index=cycles
stalls = 0      # total stalls in pipeline
stall_flag = 0      # number of stalls in special combo cases
d_stall = 0

def run_button():
    initializereg()

    exec(open(r"parent.py").read())  # This puts all the data and code into the memory.
    PC.PC = 0x0
    global instructions_executed,IR,decoded_result,r_value,r_index,m_type,m_value,m_index,m_read,opc,cycles,stalls,stall_flag,d_stall

    c3 = c2 = c1 = 0
    pcb = 0
    r_index_temp = r_value_temp = m_fwd_temp = flush = 0            # m_fwd_temp can be used in M-_ fwding path
    while (PC.PC < memory.code_stop or c3 == 0) and configme.breakflag == 0:
        if r_index_temp > 0:         EXEC_instruct.write_back(r_index_temp,r_value_temp)
        if c2==1:   c3=1            # Last instruction passes thru WrBack Stage

        r_index_temp = r_index
        r_value_temp = r_value
        if m_index != -1 and c2==0:
            if m_read == 0:     # store
                memory.memory_access(m_index,m_value,m_type,m_read)
            elif m_read == 1:   # load
                r_index_temp = r_index
                r_value_temp = memory.memory_access(m_index,m_value,m_type,m_read)
                m_fwd_temp = r_value_temp

        if c1==1:   c2 = 1          # Last instruction passes thru MemAcc stage

        if decoded_result != (-1,-1,-1,-1,0,-1) and d_stall == 0 and c1==0:     # statement not executed if d_stall!=0
            opc, r_index, r_value, m_index, m_value, m_type, m_read,stall_flag = EXEC_instruct.execute_instruction(decoded_result)
            if stall_flag==0:   instructions_executed += 1
            if PC.PC >= memory.code_stop:       c1=1        # This is the last instruction to be executed
        elif d_stall !=0:
            opc = result[0]         ########## it was decoded_result[0] here before
            r_index=-3
            r_value=m_value=0
            m_index=m_type=-1
            stalls+=1
            d_stall -= 1
            executed_information.stalls_data_hazs += 1

        if stall_flag > 0:          # stall for 1 or 2 cycles(as required) in case of special combo. After stalling, continue from E-stage itself
            while stall_flag > 0 :
                executed_information.add_to_executed_info(opc,-1,0,-1,0,-1,m_fwd_temp)
                stalls += 1
                cycles += 1
                stall_flag -= 1
                executed_information.stalls_data_hazs += 1
                if m_fwd_temp!=0:   m_fwd_temp=0
            m_index = -1
            continue


        executed_information.add_to_executed_info(opc, r_index, r_value, m_index, m_value, m_type,m_fwd_temp)
        cycles += 1
        m_fwd_temp = 0

        if 19 <= opc <= 20 and flush==1 and c2==0 and d_stall==0:
            executed_information.add_to_executed_info(opc, -47, 0, -1, 0, -1, 0)
            stalls += 1
            cycles += 1                         # stores jump-to-address of uncond branch to reduce stalls
            executed_information.stalls_control_hzs += 1

        if 27 <= opc <= 30 and flush==1 and c1==0 and d_stall==0:
            executed_information.add_to_executed_info(opc, -47, 0, -1, 0, -1, 0)
            stalls += 1
            cycles += 1                 # 1 STALL after cond jump becoz of wrong prediction
            executed_information.stalls_control_hzs += 1


        if IR != "" and c1 == 0:
            flush = 0
            result = decoder.decode(IR)
            d_stall = result[6]
            if d_stall > 0:
                continue

            decoded_result = result[:6]
            if decoded_result[0]==20 or decoded_result[0]==19:
                if pcb != PC.PC:
                    flush = 1
                    pcb = PC.PC
                    executed_information.control_hazards += 1
            if 27 <= decoded_result[0] <= 30:
                if pcb != PC.PC:        # if prediction is wrong
                    flush = 1
                    pcb = PC.PC
                    executed_information.branch_mispredicts += 1
                    executed_information.control_hazards += 1

        if pcb < memory.code_stop:
            # wer = pcb
            IR = decoder.fetch(pcb)
            if pcb in executed_information.branch_child.keys() and executed_information.branch_taken[pcb] == 1:
                pcb = executed_information.branch_child[pcb]
            else:
                pcb += 4

        QApplication.processEvents()

    memory.print_mem_into_apache()
    memory.print_code_into_apache()
    fO = open('console.txt','w+')
    fO.write(f'Assume CPI = 5\n')
    fO.write(f'Total clock cycles for program = {5*cycles}\n')
    fO.close()


def initializereg():
    for i in range(32):
        if i == 2: register_file.store_in_register(i,0x7ffffff0)
        elif i == 3: register_file.store_in_register(i,0x10000000)
        else:   register_file.store_in_register(i,0)
    memory.code_stop = 0x0
    PC.PC = 0x0
    executed_information.initialize_values()
    global instructions_executed,check_on_step,IR,decoded_result,r_value,r_index,m_type,m_value,m_index,m_read,opc,cycles,stalls,stall_flag,d_stall
    cycles = stalls = stall_flag = d_stall = 0
    instructions_executed = 0
    check_on_step = 0
    IR = ""
    decoded_result = (-1,-1,-1,-1,0,-1)
    r_index = m_index = m_type = m_read = -1
    r_value = m_value = 0
    opc = -1
    memory.memory_map.clear()
    fO = open('console.txt','w+')
    fO.write(f'Everything is reset!\n')
    fO.close()


# run_button()
# memory.print_all_memory()
# print()
# register_file.print_selected_registers()
# print(f"\nCycles = {cycles}")
# print(f"Instructions executed: {instructions_executed}")
# print(f"CPI: {(cycles/instructions_executed):.2f}")
# print(f"Store, Load instructs executed: {executed_information.data_transfer_instructs}")
# print(f"ALU instructs executed: {executed_information.alu_instructs}")
# print(f"Control instructs executed: {executed_information.control_instructs}")
# print(f"Data Hazards: {executed_information.data_hazards}")
# print(f"Control Hazards: {executed_information.control_hazards}")
# print(f"Stalls = {stalls}")
# print(f"Stalls due to control hazards: {executed_information.stalls_control_hzs}")
# print(f"Stalls due to data hazards: {executed_information.stalls_data_hazs}")
# print(f"Branch Mis-predictions: {executed_information.branch_mispredicts}")
# print(executed_information.branch_child)
# print(*executed_information.executed_info,sep="\n")
# register_file.print_all_registers()
