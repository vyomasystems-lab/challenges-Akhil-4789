# level1_design2 ( Sequence Detector ) Verification
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

My Gitpod id with the screenshot


## Screenshots

![App Screenshot](https://github.com/Akhil-4789/Bug_Verification/blob/main/image.png)

## Description
The design will take the inp bit continuosly which is synchronous with the clock 
if the sequence 1011 is detected then the output bit (seq_seen) becomes high
It also consists of the reset input which will reset the design when it is high

![App Screenshot](https://github.com/Akhil-4789/Bug_Verification/blob/main/seq_D.jpg)

## State Diagram of SEQ 1011 with Overlapping

The state diagram for the 1011 sequence with overlapping is:

![App Screenshot](https://github.com/Akhil-4789/Bug_Verification/blob/main/seq_det_1_dig.jpg)



## Verification Environment

  The CoCoTb based Python test is developed as explained.To the reference the python testbench file is also given for the better understanding
  we need to drive the inputs from the dut to test_mkbitmanip.py file and need to obsverve the bugs.
  
## bugs identification

 given random sequence and observed for the bugs 
  
  

     INP_bit=random.randint(0,1)
     await FallingEdge(dut.clk)
     dut.inp_bit.value=INP_bit
 
 When the input seq is Overlapping then the Bug is observed
 we found the bug as like:
 
 ![App Screenshot](https://github.com/Akhil-4789/Bug_Verification/blob/main/seq_det_1_fail.png)

 



## reason for the bug


    SEQ_1011:
      begin
        next_state = IDLE;     // bug3 incomplete lines which makes overlapping incomplete
      end
      

when the current state is in ``SEQ_1011`` and the inp bit is 1 then code is not written it goes to 
default state which is ``IDLE`` so the overlapping condition is failed

To rectify it:


 SEQ_1011:
      begin
        if(inp_bit == 1)
           next_state = SEQ_1;
        else
           next_state = SEQ_10;
      end

 ![App Screenshot](https://github.com/Akhil-4789/Bug_Verification/blob/main/seq_det_1_pass.png)

## conclusion 

The design was verified and the bugs were identified using cocotb
