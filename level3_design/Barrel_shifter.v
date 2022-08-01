//Barrel_shifter with bug 

module Barrel_shifter(d,out,q,c); 
  input [7:0]d;
  output [7:0]out,q;
  input[2:0]c;
  
  mux m1(q[0],d,c);
  mux m2(q[1],{d[0],d[7:1]},c);
  mux m3(q[2],{d[1:0],d[7:2]},c);
  mux m4(q[3],{d[2:0],d[7:3]},c);
  mux m5(q[4],{d[4:0],d[7:4]},c);
  mux m6(q[5],{d[3:0],d[7:5]},c);
  mux m7(q[6],{d[5:0],d[7:6]},c);
  mux m8(q[7],{d[6:0],d[7:7]},c);
  assign out=q;
  
endmodule
