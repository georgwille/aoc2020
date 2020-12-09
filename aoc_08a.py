fin = open("input_08.txt")

program = []

for line in fin:
    opcode, arg = line.strip().split(" ")
    program.append((opcode, arg))

fin.close()

class Comp():
    def __init__(self,prog):
        self.prog = prog
        self.pc = 0
        self.acc = 0
        self.accesscount = [0]*len(prog)


    def run(self):
        while True:
            opcode = self.prog[self.pc][0]
            arg = int(self.prog[self.pc][1])
            self.accesscount[self.pc] += 1

            if self.accesscount[self.pc] == 2:
                print("Loop detected. Accumulator:",self.acc)
                return

            if opcode == "nop":
                self.pc += 1

            elif opcode == "acc":
                self.acc += arg
                self.pc += 1

            elif opcode == "jmp":
                self.pc += arg

            else:
                print("Undefined opcode", opcode, "at", self.pc)


mycomp = Comp(program)
mycomp.run()

