# RISC-V-Assembler

Built a Simulator for RISC-V 32 bit ISA
The simulator has capabilities for Pipelining Instructions with and without Data Forwarding and Branch Prediction.

The Program Counters (PC) of Branch Instructions are stored separately.
Each time a new instruction is fetched, the PC is searched for amongst previously stored PC's.

If found, the Simulator uses a 1-bit branch predictor to predict the PC of next instruction to be fetch, however branch decision is resolved only after Execute Stage

Instruction in decode stage is compared with the 2 previous instructions to detect data dependencies.
If data dependency is found, the appropriate Interstage Buffer (IB) (IB3 for arithmetic instructions and IB4 for load instructions) is computed.
Data is then fetched at the appropriate cycle from this IB and given to the instruction in Decode stage.

Further Details and directory structure is explained in another README file in "risc_v_assembler-master"
