//Multiplexer commonly know as MUX  is used as sub module in 8-bit Barrel Shifter
//A barrel shifter is a digital circuit that can shift a data word by a specified number of bits 
//without the use of any sequential logic, only pure combinational logic

/////----------------------------------------------------------------mux--------------------------------------------------------------

// Code your design here
module mux(y,d,c);
  input[7:0]d;
  output y;
  reg y;
  input [2:0]c;
  always @ (c)
  begin
    if (c==3'b000)
      y = d[0];
    else if (c==3'b001)
      y = d[1];
      else if (c==3'b010)
      y = d[2];
      else if (c==3'b011)
      y = d[3];
      else if (c==3'b100)
      y = d[4];
      else if (c==3'b101)
      y = d[5];
      else if (c==3'b110)
      y = d[6];
      else if (c==3'b111)
      y = d[7];
    end
  endmodule
