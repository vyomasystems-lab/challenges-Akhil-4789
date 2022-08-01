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
def Barrel_test1(dut):                      
    yield Timer(2)
    c=4
    d=16
    dut.dinp.value = d
    dut.cinp.value = c
    yield Timer(2)
    if dut.out != d:
         raise TestFailure("barrel Shifter failed with test %s and selection %s",(dut.dinp , dut.cinp ))
    else:
         dut.log.info("barrel Shifter Passed with test %s ",(dut.dinp))
        
