// Main module of 8-Bit Barrel shifter
//A barrel shifter is a digital circuit that can shift a data word by a specified 
//number of bits without the use of any sequential logic, only pure combinational logic

// Code 

//mux.v Sub-Module is written in level3_design named as mux
///------------------------------------------------------------------------ 8-Bit Barrel shifter----------------------------------------------------------------

module Barrel_shifter(d,out,q,c); 
  input [7:0]d;
  output [7:0]out,q;
  input[2:0]c;
  
  mux m1(q[0],d,c);
  mux m2(q[1],{d[0],d[7:1]},c);
  mux m3(q[2],{d[1:0],d[7:2]},c);
  mux m4(q[3],{d[2:0],d[7:3]},c);
  mux m5(q[4],{d[3:0],d[7:4]},c);
  mux m6(q[5],{d[4:0],d[7:5]},c);
  mux m7(q[6],{d[5:0],d[7:6]},c);
  mux m8(q[7],{d[6:0],d[7:7]},c);
  assign out=q;
  
endmodule
