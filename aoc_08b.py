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
        self.state = "init"


    def run(self):
        self.state = "run"
        while True:
            if self.pc == len(self.prog):
                print("Normal termination.")
                self.state = "stop"
                return

            opcode = self.prog[self.pc][0]
            arg = int(self.prog[self.pc][1])
            self.accesscount[self.pc] += 1

            if self.accesscount[self.pc] == 2:
                print("Loop detected. Accumulator:",self.acc)
                self.state = "loop"
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


for pos,element in enumerate(program):
    mutant = program.copy()
    if element[0] == "nop":
        newelement = ("jmp",element[1])
    elif element[0] == "jmp":
        newelement = ("nop",element[1])
    else:
        newelement = element
    mutant[pos] = newelement
    mycomp = Comp(mutant)
    mycomp.run()
    print(pos,mycomp.state)
    if mycomp.state == "stop":
        print(pos, element)
        print(mycomp.acc)

