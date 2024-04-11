# x86 Assembly Crash Course
The assembly language is the lowest level of human-readable language. It is also the highest level of language into which a binary can be reliably decompiled. 

When learning malware reverse engineering, knowing the basics of assembly language is essential. This is because when we get a malware sample to analyze, it is most likely a compiled binary. We cannot view this binary's C/C++ or other language code because that is not available to us. What we can do, however, is to decompile the code using a decompiler or a disassembler. The problem with decompiling is that a lot of information in the written code is removed while it is compiled into a binary; hence we won't see variable names, function names, etc., as we do while writing code. So the most reliable code we have for a compiled binary is its assembly code.

# Table of Contents

# Opcodes and Operands
The code for a program, as written on the disk and understood by the CPU, is in binary format. This means that the actual code is a sequence of 1s and 0s. To make it understandable, we often club a series of 8-bits (called a byte) into a single digit in hex. So the instructions that a computer is executing will be just a sequence of random numbers in hex to a human. Among these random numbers are opcodes and operands.

An opcode is a command that tells the processor what operation to perform. An operand is the data that the operation is performed on. For example, in the instruction `mov eax, 5`, `mov` is the opcode, `eax` is the operand, and `5` is the data that the operation is performed on.

## Example
The instruction for moving 0x5F to the eax register is:  
`mov eax, 0x5f`

When looking at it in a disassembler, we will see:  
`040000:    b8 5f 00 00 00    mov eax, 0x5f`

* The `040000` is the address where the instruction is located.
* `b8` is the opcode for the instruction `mov eax`.
* `5f 00 00 00` is the operand `0x5f`.


Please note that due to [endianness](https://en.wikipedia.org/wiki/Endianness), the operand `0x5f` is written as `5f 00 00 00`, which is actually `00 00 00 5f` but in **little-endian** notation. Similarly, there is an opcode for each instruction in the assembly language. 

There are [references](http://ref.x86asm.net/index.html) for converting opcodes into assembly instructions. Still, unless we are writing a disassembler, we will not need them, as a disassembler does that work pretty well. However, it is good to understand what is happening under the hood for a better picture overall.

## Types of Operands
In general, there are three types of operands in the assembly language.

1. **Immediate**: This is a constant value that is part of the instruction itself. For example, in the instruction `mov eax, 5`, `5` is an immediate operand.
2. **Register**: This is a register that is part of the CPU. For example, in the instruction `mov eax, 5`, `eax` is a register operand.
3. **Memory**: This is a memory address that is part of the instruction. For example, in the instruction `mov eax, [0x12345678]`, `[0x12345678]` is a memory operand.

# General Instructions
Instructions tell the CPU what operation to perform. Instructions often use operands from registers, memory, or immediate operands to perform operations and then store the results in either registers or memory. 

## The MOV Instruction
The `mov` instruction is used to move data from one location to another. The general syntax for the `mov` instruction is: `mov destination, source`

The mov instruction can move a fixed value to a register, a register to another register, and a value in a memory location to a register. The following examples will help explain.

The following instruction copies a fixed value to a register. In this particular instruction, 0x5f is being moved to eax: `mov eax, 0x5f`

In this particular case, the value stored in eax is being moved to ebx: `mov ebx, eax`

The following instruction copies the value stored in a memory location to a register: `mov eax, [0x5fc53e]`

As seen above, we use square brackets when referencing memory. Similarly, suppose we see a register in square brackets. In that case, that will mean that the value in that register will be treated as a memory location, and the value in that memory location will be moved to the destination. This means that the example `mov eax, [0x5fc3e]` and the below example will have the same result.  

`mov ebx, 0x5fc53e`  
`mov eax, [ebx]`

We can use the mov instruction to perform arithmetic calculations when referencing memory addresses. For example, the below instruction calculates ebp+4 (adding an offset of 4 bytes to the memory location) and moves the value in the resulting memory address into eax:
`mov eax, [ebp+4]`

## The LEA Instruction
The `lea` instruction is used to load the effective address of a memory location into a register. The general syntax for the `lea` instruction is: `lea destination, source`.

While the mov instruction moves the data at the source memory address to the destination, the lea instruction moves the address of the source into the destination. In the example below, the ebp value will be increased by four and moved to eax. However, if we had used a mov instruction here instead of lea, it would have moved the value in the memory location ebp+4.
`lea eax, [ebp+4]`

Here, we can notice that we have performed an arithmetic operation on a register and saved the result in another register using a single instruction. The `lea` instruction is often used by compilers not for referencing memory locations but so that an arithmetic operation is performed on a register and saved to another using a single instruction. This is true, especially if the arithmetic operations are more complex, like adding and multiplying in a single instruction. As we will see in the next task, using arithmetic operations for this operation will need several instructions.

## The NOP Instruction
The `nop` instruction is used to do nothing. It is often used for padding or for debugging purposes. But it is also used for consuming CPU cycles while waiting for an operation or other such purposes. The general syntax for the `nop` instruction is: `nop`

The nop instruction is used by malware authors when redirecting execution to their shellcode. The exact location where the execution will redirect is often unknown, so the malware author uses a bunch of nop instructions to ensure that the shellcode execution does not start from the middle. This padding of nop instructions is called a nop sled.

A nop in hex is represented as `0x90`/`\x90`.

## Shift Instructions
The shift instructions are used to shift the bits of a register left or right. The general syntax for the shift instruction is: `shr destination, count` or `shl destination, count`.

Here the `shr` instruction is for the shift right operation, and the `shl` is for the shift left operation. This instruction shifts the bits in the `destination` operand. The `count` operand decides the number of bits to be shifted. The bits which are shifted out of their location are filled with zeroes. So, if we have `00000010` in eax and shift it left, it will become `00000100`.

The carry flag (CF) is used to augment the destination, as it is filled by the last bit overflowing the destination. For example, if we have 00000101 in eax and shift it right by 1 bit, the result will have 00000010 in eax, and the carry flag will be set, i.e. it will have a value of 1.

Shift instructions are used instead of multiplication and division by two or powers of two (2n where n is the count in the shift instruction). This saves execution time by not having to manipulate values in registers before performing multiplication or division. For example, If eax has 00000010, and we shift right by 1 bit, we get 00000001, which is the same result as dividing eax by 2. Similarly, if eax has 00000001, and we shift left by 1 bit, the result is 00000010, the same as multiplying eax by 2.

## Rotate Instructions
The rotate instructions are used to rotate the bits of a register left or right. The general syntax for the rotate instruction is: `ror destination, count` or `rol destination, count`.

Here, the `ror` instruction rotates the destination to the right, and `rol` rotates the destination to the left. The rest of the syntax remains the same. As an example, if we have 10101010 in al, and we rotate it right by 1 bit, it will result in `01010101`. Similarly, rotating this result to the left by 1 bit will result in `10101010` again.

# Flags
In x86 assembly language, the CPU has several flags that indicate the outcome of certain operations or conditions. These flags are bits in a special register known as the flags register or EFLAGS register. Each flag represents a specific condition or result of the most recent arithmetic or logical operation. Here’s a table with the most common flags in x86 assembly and their explanations:

| Flag | Abbreviation | Explanation |
|:---:|:---:|:---|
| Carry | CF | Set when a carry-out or borrow is required from the most significant bit in an arithmetic operation. Also used for bit-wise shifting operations. |
| Parity | PF | Set if the least significant byte of the result contains an even number of 1 bits. |
| Auxiliary | AF | Set if a carry-out or borrow is required from bit 3 to bit 4 in an arithmetic operation (BCD arithmetic). |
| Zero | ZF | Set if the result of the operation is zero. |
| Sign | SF | Set if the result of the operation is negative (i.e., the most significant bit is 1). |
| Overflow | OF | Set if there's a signed arithmetic overflow (e.g., adding two positive numbers and getting a negative result or vice versa). |
| Direction | DF | Determines the direction for string processing instructions. If DF=0, the string is processed forward; if DF=1, the string is processed backward. |
| Interrupt Enable | IF | If set (1), it enables maskable hardware interrupts. If cleared (0), interrupts are disabled. |

Flags can be used in conditional jumps and are crucial for implementing conditional branching in assembly code. For example, you might only jump to a specific address if a certain flag is set or cleared.

# Arithmetic and Logical Instructions
Arithmetic Operations are performed by a CPU using arithmetic instructions.

## Arithmetic Operations

### Addition and Subtraction Instructions
The `add` instruction is used to add two values. The general syntax for the `add` instruction is: `add destination, source`.

The `sub` instruction is used to subtract two values. The general syntax for the `sub` instruction is: `sub destination, source`.

In the above examples, the value can be either a fixed value constant or a register. For the subtraction operation, Zero Flag (ZF) is set if the result of the subtraction is zero.

### Multiplication and Division Instructions
The multiplication and division operations use the eax and the edx registers. Therefore, we will have to look at the last instruction that manipulated these registers for every multiply and divide operation. 

The multiply instruction has the following format. It multiplies the value with eax and stores the result in edx:eax as a 64-bit value. Two registers are required here because the result of multiplying 2 32-bit values can often be higher than 32 bits. The lower 32 bits of the result are stored in the eax register, and the higher 32 bits are stored in the edx register.
`mul value`

The value can be another register or a constant as an immediate operand.

For the division instruction, the case is the opposite. It divides the 64-bit value in edx:eax and saves the result in eax and the remainder in edx.
`div value`

### Increment and Decrement Instructions
The `inc` instruction is used to increment the value of a register by 1. The general syntax for the `inc` instruction is: `inc destination`.

The `dec` instruction is used to decrement the value of a register by 1. The general syntax for the `dec` instruction is: `dec destination`.

## Logical Operations
Logical instructions are used to perform logical operations. Let's go through a few common logical operations performed by the CPU.

### AND Instruction
The AND instruction performs a bitwise AND operation on the operands. An AND operation returns an output of 1 when both the inputs are 1; otherwise, it returns 0. An example instruction is below:

`and al, 0x7c`

In this example, 0x7c converts to 01111100 in binary. Suppose al had a value of 0xfc, which is 11111100 in binary. In this case, the output of the above instruction will be 01111100. However, if al has a value of 0x8c, 10001100 in binary, the result of the above instruction will be 00001100 or 0xc.

### OR Instruction
The OR instruction performs a bitwise OR operation. An OR operation returns 1 if at least one of the operands is 1. It returns 0 if none of the operands is 1. An example instruction is below:

`or al, 0x7c`

In this example, if al had a value of 0xfc or 11111100 in binary, the output of the above instruction will be 11111100. Similarly, if al has a value of 0x8c or 10001100 in binary, the result will still be 11111100 in binary or 0xfc.

### NOT Instruction
The NOT instruction takes one operand. It simply inverts the operand bits, replacing 1s with 0s and vice versa. In the following example, if al had a value of 11110000, it would result in 00001111.
`not al`

### XOR Instruction
The XOR operation returns 1 if both the inputs are opposite. It returns 0 when both inputs are the same. This operation is performed by the XOR instruction in assembly language, which performs a bitwise XOR operation on the operands. It has the following syntax.
`xor al, 0x7c`

If al has a value of 0xfc, which is 11111100, the result of this instruction will be 10000000 or 0x80. Similarly, if al has a value of 0x8c, which is 10001100, the result of this instruction will be 11110000 or 0xf0. If al has a value of 0x7c, the result will be 0x00. This shows that XORing a register with itself results in 0. Therefore, the XOR instruction is often used to zero a register, which is more optimized than a MOV instruction.

# Conditionals and Branching
## Conditionals
A CPU often must determine if two values are equal to, greater than, or less than each other. To perform such operations, the CPU uses some conditional instructions. 

### The TEST Instruction
The test instruction performs a bitwise AND operation, and instead of storing the result in the destination operand as the AND instruction does, it sets the Zero Flag (ZF) if the result is 0. This instruction is often used to check if an operand has a NULL value, for example, by testing the operand against itself. This is done because it takes fewer bytes to use the test instruction than by comparing to 0. The test instruction has the following syntax:
`test destination, source`

### The CMP Instruction
Based on the result, the CMP instruction compares the two operands and sets the Zero Flag (ZF) or the Carry Flag (CF). It has the following syntax:

`cmp destination, source`

The compare instruction works similarly to a subtract instruction. The only difference is that the operands are not modified. The Zero Flag (ZF) is set if both operands are equal. If the source operand is greater than the destination operand, the Carry Flag (CF) is set. The ZF and the CF are cleared if the destination operand is greater than the source operand.

## Branching
When there is no branching, the Instruction Pointer goes from one instruction to the other in the order they are placed in memory. The control flow remains in a straight line unless there is a branching operation. Branching operations change the value of the Instruction Pointer and change the program's control flow from linear to branching out.

### The JMP Instruction
The jmp instruction is used to jump to a specific address. The general syntax for the jmp instruction is: `jmp address`

Here, the location operand will be moved to the Instruction Pointer, making it the address where the next instruction will be fetched for execution.

### Conditional Jumps
Often, the code requires to move if a specific condition is met. In higher-level languages, there are if conditions that help fulfil this requirement. However, there is no if statement in the assembly language. This requirement is fulfilled using conditional jumps. Conditional jumps decide whether to jump based on the value of the Flag Registers. Their syntax is similar to the jump instruction. The following table shows some of the common conditional jumps.

| Instruction | Explanation |
|---|---|
| jz | Jump if the ZF is set (ZF=1). |
| jnz | Jump if the ZF is not set (ZF=0). |
| je | Jump if equal. Often used after a CMP instruction. |
| jne | Jump if not equal. Often used after a CMP instruction. |
| jg | Jump if the destination is greater than the source operand. Performs signed comparison and is often used after a CMP instruction. |
| jl | Jump if the destination is lesser than the source operand. Performs signed comparison and is often used after a CMP instruction. |
| jge | Jump if greater than or equal to. Jumps if the destination operand is greater than or equal to the source operand. Similar to the above instructions. |
| jle | Jump if lesser than or equal to. Jumps if the destination operand is lesser than or equal to the source operand. Similar to the above instructions. |
| ja | Jump if above. Similar to jg, but performs an unsigned comparison. |
| jb | Jump if below. Similar to jl, but performs an unsigned comparison. |
| jae | Jump if above or equal to. Similar to the above instructions. |
| jbe | Jump if below or equal to. Similar to the above instructions. |

# Stack and Function calls
## The Stack
The stack is a Last In, First Out (LIFO) memory. This means the last variable pushed onto the stack is the first to pop out. These push and pop operations are performed by following instructions in the assembly language.

### The PUSH Instruction
The push instruction has the following syntax:
`push source`

As mentioned earlier, the push instruction will push the source operand onto the stack. The value of the operand is stored at the memory location pointed to by the stack pointer (ESP), effectively becoming the new top of the stack. The stack pointer is then adjusted (decremented) to reflect the updated top position of the stack. The following instructions also push all the general-purpose registers to the stack.

**pusha (push all words):** Pushes all the 16-bit general purpose registers to the stack, i.e. AX, BX, CX, DX, SI, DI, SP, BP  
**pushad (push all double words):** Pushes all the 32-bit general purpose registers to the stack, i.e. EAX, EBX, ECX, EDX, ESI, EDI, ESP, EBP

When we encounter these instructions, it is often a sign of someone manually injecting assembly instructions to save the state of registers, as is often the case with shellcode.

### The POP Instruction
The pop instruction has the following syntax:
`pop destination`

The pop instruction retrieves the value from the top of the stack and stores it in the destination operand. As a result, the stack pointer (ESP) is incremented to reflect the adjustment made after popping the value. The following instructions also pop all the general-purpose registers from the stack.

**popa (pop all words):** Pops the values sequentially from the top of the stack to general-purpose registers in the following order: DI, SI, BP, BX, DX, CX, AX. The SP or ESP is adjusted to reflect the new top position of the stack.

**popad (pop all double words):** Pops the values sequentially from the top of the stack to general-purpose registers in the following order: EDI, ESI, EBP, EBX, EDX, ECX, EAX. The SP or ESP is adjusted to reflect the new top position of the stack.

## The CALL Instruction
The call instruction is used in the assembly language for performing a function call operation to perform a specific task. It has the following syntax:
`call location`

Depending on the calling convention, the arguments are placed on the stack or in the registers in a function call. The function prologue prepares the stack by adjusting the EBP and ESP and pushing the return address on the stack. Similarly, when the function returns, the epilogue restores the stack for the caller function. 