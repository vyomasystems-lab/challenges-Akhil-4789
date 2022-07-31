# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.result import TestFailure
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    seq_seen = 0
    # reset
    dut.reset.value = 0
    await  FallingEdge(dut.clk)  
    dut.reset.value = 1
    await  FallingEdge(dut.clk)
     
    dut.reset.value = 0
    cocotb.log.info(dut.next_state.value)
    await  FallingEdge(dut.clk)
    for i in range(16):
        if i==0:    
            cocotb.log.info(dut.next_state.value)
            dut.inp_bit.value=0
            cocotb.log.info(dut.next_state.value) 
            await  FallingEdge(dut.clk)
            
        elif i==1:
            dut.inp_bit.value=1
            await  FallingEdge(dut.clk)
            cocotb.log.info(dut.next_state.value) 
        elif i==2:
            dut.inp_bit.value=1  
            await  FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value)  
        elif i==3:
            dut.inp_bit.value=0
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value)   
        elif i==4:
            dut.inp_bit.value =1
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value) 
        elif i==5:
            dut.inp_bit.value =0
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value)    
        elif i==6:
            dut.inp_bit.value =1
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value)
        elif i==7:
            dut.inp_bit.value =1
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value) 
        elif i==8:
            dut.inp_bit.value =0
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value) 
        elif i==9:
            dut.inp_bit.value =1
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value) 
        elif i==10:
            dut.inp_bit.value =0
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value) 
        elif i==11:
            dut.inp_bit.value =1
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value) 
        elif i==12:
            dut.inp_bit.value =1
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value) 
        elif i==13:
            dut.inp_bit.value =0
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value) 
        elif i==14:
            dut.inp_bit.value =1
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value) 
        elif i==15:
            dut.inp_bit.value =1
            await FallingEdge(dut.clk) 
            cocotb.log.info(dut.next_state.value)                                          
        #INP_bit=random.randint(0,1)
        #await FallingEdge(dut.clk)
        #dut.inp_bit.value=INP_bit
        #await FallingEdge(dut.clk)
        dut.log.info("input bit is %s and seqseen bit is %s state %d",(int(dut.inp_bit),int(dut.seq_seen),int(dut.current_state)))
    if dut.next_state.value==4:
        dut.log.info("input bit is %s and seqseen bit is %s state %d",(int(dut.inp_bit),int(dut.seq_seen),int(dut.current_state)))
    else:
        raise TestFailure("FAIL at OVERLAPPING Condition input bit is %s and seqseen bit is %s State  %d Expected_State 4",(int(dut.inp_bit),int(dut.seq_seen),int(dut.current_state)))
       
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----RANDOM-TEST-CASES--------------RANDOM-TEST-CASES--------------RANDOM-TEST-CASES----------RANDOM-TEST-CASES------------RANDOM-TEST-CASES----------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
       
   # See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    seq_seen = 0
    # reset
    dut.reset.value = 0
    await  FallingEdge(dut.clk)  
    dut.reset.value = 1
    await  FallingEdge(dut.clk)
    await  FallingEdge(dut.clk) 
    cocotb.log.info(dut.next_state.value) 
    dut.reset.value = 0
    await  FallingEdge(dut.clk)
    for i in range(50):  
        INP_bit=random.randint(0,1)
        await FallingEdge(dut.clk)
        dut.inp_bit.value=INP_bit
        await FallingEdge(dut.clk)
        dut.log.info("input bit is %s and seqseen bit is %s present_state %d",(int(dut.inp_bit),int(dut.seq_seen),int(dut.current_state)))


        
