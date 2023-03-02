# Intro to x86-64
## Introduction
Computers execute machine code, which is encoded as bytes, to carry out tasks on a computer. Since different computers have different processors, the machine code executed on these computers is specific to the processor. In this case, we’ll be looking at the Intel x86-64 instruction set architecture which is most commonly found today.

Intel first started out by building 16-bit instruction set, followed by 32 bit, after which they finally created 64 bit. All these instruction sets have been created for backward compatibility, so code compiled for 32 bit architecture will run on 64 bit machines. 

Machine code is usually represented by a more readable form of the code called assembly code. This machine is code is usually produced by a compiler, which takes the source code of a file, and after going through some intermediate stages, produces machine code that can be executed by a computer. 

So before an executable file is produced, the source code is first compiled into assembly(.s files), after which the assembler converts it into an object program(.o files), and operations with a linker finally make it an executable. 
## Syntax
x86 (both 32- and 64-bit) has two alternative syntaxes available for it. Some assemblers can only work with one or the other, while a few can work with both. These alternatives are Intel and AT&T. I've tried to show the differences below
|  | Intel | AT&T |
|---|---|---|
| Comments | ; | // |
| Instructions | Untagged add | Tagged with operand sizes: addq |
| Registers | eax, ebx, etc. | %eax,%ebx, etc. |
| Immediates | 0x100 | $0x100 |
| Indirect | [eax] | (%eax) |
| General indirect | [base + reg + reg * scale + displacement] | displacement(reg, reg, scale) |

To use AT&T in radare2 = `e asm.syntax=att`  
To use Intel in radare2 = `e asm.syntax=intel`

To use AT&T in gdb = `set disassembly-flavor att`
To use Intel in gdb = `set disassembly-flavor intel`

## Simple example using Radare2
The first step is to execute the program intro by running  
```console
berkankutuk@kali:~$ ./intro
value for a is 1 and b is 2
value of a is 2 and b is 1
```
From the execution, it can be seen that the program is creating two variables and switching their values. Time to see what it’s actually doing under the hood!


```console
berkankutuk@kali:~$ r2 -d intro

Process with PID 1366 started...
= attach 1366 1366
bin.baddr 0x5643f7bb6000
Using 0x5643f7bb6000
asm.bits 64
 -- The more 'a' you add after 'aa' the more analysis steps are executed.
```
This will open the binary in debugging mode. Once the binary is open, one of the first things to do is ask r2 to analyze the program, and this can be done by typing in:

```console
[0x7ff449179090]>:~$ aa

[x] Analyze all flags starting with sym. and entry0 (aa)
```
Which is the most common analysis command. It analyses all symbols and entry points in the executable.

Then lets run
[0x7ff449179090]>:~$ e asm.syntax=att
```
to set the disassembly syntax to AT&T.

If you need help, you can use the `?` command.  
For more specific information about the analysis, run:  `a?`

Once the analysis is complete, you would want to know where to start analysing from - most programs have an entry point defined as main. To find a list of the functions run:

```console
[0x7ff449179090]>:~$ afl

0x5643f7bb6560    1 42           entry0
0x5643f7db6fe0    1 4124         reloc.__libc_start_main
0x5643f7bb6590    4 50   -> 40   sym.deregister_tm_clones
0x5643f7bb65d0    4 66   -> 57   sym.register_tm_clones
0x5643f7bb6620    5 58   -> 51   entry.fini0
0x5643f7bb6550    1 6            sym..plt.got
0x5643f7bb6660    1 10           entry.init0
0x5643f7bb6730    1 2            sym.__libc_csu_fini
0x5643f7bb6734    1 9            sym._fini
0x5643f7bb66c0    4 101          sym.__libc_csu_init
0x5643f7bb666a    1 78           main
0x5643f7bb6540    1 6            sym.imp.__printf_chk
0x5643f7bb6510    3 23           sym._init
0x5643f7bb6000    3 97   -> 123  map.home_tryhackme_introduction_intro.r_x
```
As seen here, there actually is a function at main. Let’s examine the assembly code at main by running the command

```console
[0x7ff449179090]>:~$ pdf @main

/ (fcn) main 78
|   int main (int argc, char **argv, char **envp);
|           ; DATA XREF from entry0 (0x5643f7bb657d)
|           0x5643f7bb666a      4883ec08       subq $8, %rsp
|           0x5643f7bb666e      b902000000     movl $2, %ecx
|           0x5643f7bb6673      ba01000000     movl $1, %edx
|           0x5643f7bb6678      488d35c90000.  leaq str.value_for_a_is__d_and_b_is__d, %rsi ; 0x5643f7bb6748 ; "value for a is %d and b is %d\n"
|           0x5643f7bb667f      bf01000000     movl $1, %edi
|           0x5643f7bb6684      b800000000     movl $0, %eax
|           0x5643f7bb6689      e8b2feffff     callq sym.imp.__printf_chk
|           0x5643f7bb668e      b901000000     movl $1, %ecx
|           0x5643f7bb6693      ba02000000     movl $2, %edx
|           0x5643f7bb6698      488d35c90000.  leaq str.value_of_a_is__d_and_b_is__d, %rsi ; 0x5643f7bb6768 ; "value of a is %d and b is %d\n"
|           0x5643f7bb669f      bf01000000     movl $1, %edi
|           0x5643f7bb66a4      b800000000     movl $0, %eax
|           0x5643f7bb66a9      e892feffff     callq sym.imp.__printf_chk
|           0x5643f7bb66ae      b800000000     movl $0, %eax
|           0x5643f7bb66b3      4883c408       addq $8, %rsp
\           0x5643f7bb66b7      c3             retq
```
Where pdf means print disassembly function. Doing so will give us the following view

**Values from the view**  
The values on the complete left column are memory addresses of the instructions, and these are usually stored in a structure called the stack. 

The middle column contains the instructions encoded in bytes(what is usually the machine code)

The last column actually contains the human readable instructions. 

## Registers
The core of assembly language involves using registers to do the following:

* Transfer data between memory and register, and vice versa
* Perform arithmetic operations on registers and data
* Transfer control to other parts of the program

Since the architecture is x86-64, the registers are 64 bit and Intel has a list of 16 registers:
| 64 bit | 32 bit |
|:---:|:---:|
| %rax | %eax |
| %rbx | %ebx |
| %rcx | %ecx |
| %rdx | %edx |
| %rsi | %esi |
| %rdi | %edi |
| %rsp | %esp |
| %rbp | %ebp |
| %r8 | %r8d |
| %r9 | %r9d |
| %r10 | %r10d |
| %r11 | %r11d |
| %r12 | %r12d |
| %r13 | %r13d |
| %r14 | %r14d |
| %r15 | %r15d |

16, 8 and 4 bits can also be referenced.

**What they represent**
* The first 6 registers are known as general purpose registers.  
* The %rsp is the stack pointer and it points to the top of the stack which contains the most recent memory address. The stack is a data structure that manages memory for programs. 
* %rbp is a frame pointer and points to the frame of the function currently being executed - every function is executed in a new frame. 

To move data using registers, the following instruction is used:
`movq source, destination` 

**This involves:**  
* Transferring constants(which are prefixed using the $ operator) e.g. `movq $3 rax` would move the constant 3 to the register
* Transferring values from a register e.g. `movq %rax %rbx` which involves moving value from rax to rbx
* Transferring values from memory which is shown by putting registers inside brackets e.g. `movq %rax (%rbx)` which means move value stored in %rax to memory location represented by %rbx.

The last letter of the mov instruction represents the size of the data:
| Intel Data Type | Suffix | Size(bytes) |
|:---:|:---:|:---:|
| Byte | b | 1 |
| Word | w | 2 |
| Double Word | l | 4 |
| Quad Word | q | 8 |
| Single Precision | s | 4 |
| Double Precision | l | 8 |

When dealing with memory manipulation using registers, there are other cases to be considered:
* (Rb, Ri) = MemoryLocation[Rb + Ri]
* D(Rb, Ri) = MemoryLocation[Rb + Ri + D]
* (Rb, Ri, S) = MemoryLocation(Rb + S * Ri]
* D(Rb, Ri, S) = MemoryLocation[Rb + S * Ri + D]

Some other important instructions are:
* `leaq source, destination`: this instruction sets destination to the address denoted by the expression in source
* `addq source, destination`: destination = destination + source
* `subq source, destination`: destination = destination - source
* `imulq source, destination`: destination = destination * source
* `salq source, destination`: destination = destination << source where << is the left bit shifting operator
* `sarq source, destination`: destination = destination >> source where >> is the right bit shifting operator
* `xorq source, destination`: destination = destination XOR source
* `andq source, destination`: destination = destination & source
* `orq source, destination`: destination = destination | source

## If statements
If statements use 3 important instructions in assembly:
* `cmpq source2, source1`: it is like computing a-b without setting destination
* `testq source2, source1`: it is like computing a&b without setting destination

Jump instructions are used to transfer control to different instructions, and there are different types of jumps:
| Instruction | Useful to... |
|---|---|
| jmp | Always jump |
| ja | Unsigned > |
| jae | Unsigned >= |
| jb | Unsigned < |
| jbe | Unsigned <= |
| jc | Unsigned overflow, or multiprecision add |
| jecxz | Compare ecx with 0      (Seriously!?) |
| je | Equality |
| jg | Signed > |
| jge | Signed >= |
| jl | Signed < |
| jle | Signed <= |
| jne | Inequality |
| jo | Signed overflow |

Unsigned integers cannot be negative while signed integers represent both positive and negative values.
