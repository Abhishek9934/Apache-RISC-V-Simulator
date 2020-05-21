executed_info = []
branch_child = {}
branch_taken = {}
data_transfer_instructs = 0
alu_instructs = 0
control_instructs = 0
branch_mispredicts = 0
data_hazards = 0
control_hazards = 0
stalls_data_hazs = 0
stalls_control_hzs = 0

def add_to_executed_info(v1,v2,v3,v4,v5,v6,v7):
    global executed_info
    executed_info.append((v1,v2,v3,v4,v5,v6,v7))           # appended at index = cycles


def add_to_branch_child(address,child):
    global branch_child
    branch_child[address] = child


def add_to_branch_taken(address,value):
    global branch_taken
    branch_taken[address] = value


def initialize_values():
    global executed_info,branch_child,branch_taken,data_transfer_instructs,alu_instructs,control_instructs,branch_mispredicts,data_hazards,control_hazards,stalls_control_hzs,stalls_data_hazs
    executed_info.clear()
    branch_child.clear()
    branch_taken.clear()
    data_transfer_instructs = 0
    alu_instructs = 0
    control_instructs = 0
    branch_mispredicts = 0
    data_hazards = 0
    control_hazards = 0
    stalls_data_hazs = 0
    stalls_control_hzs = 0



