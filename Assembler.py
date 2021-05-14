################################################## For A instructions #####################################################
def A_inst_conv_num(line):
    size=len(line)
    newline=[0]*16
    
    ############################### Only numeric addresses resolved here ##################################################
    num=int(line[1:size])
    binary=bin(num)
    binary=str(binary)
    size_conv=len(binary)
    for i in range(0,18-size_conv):
        newline[i]=0
    i=i+1;
    for j in range(2,size_conv):
        newline[j+i-2]=int(binary[j])
    
    return newline

################################################## For C instructions #######################################################               
def C_inst_conv(line):
    d1=d2=d3=0
    j1=j2=j3=a=0
    c1=c2=c3=c4=c5=c6=0
    if "=" in line:
        d1, d2, d3 =dest_inst(line)
    elif ";" in line:
        j1, j2, j3 =jump_inst(line)
    else :
        print("ERROR!! Format not found in HACK") 
        print("C instruction have to be either i> dest=comp  or ii>comp;jump")
        return -1;

######################################## C1-C6 #############################################
    if "D|M" in line:
        a=1
        c1=0
        c2=1
        c3=0
        c4=1
        c5=0
        c6=1
    elif "D|A" in line:
        a=0
        c1=0
        c2=1
        c3=0
        c4=1
        c5=0
        c6=1
    elif "D&M" in line:
        a=1
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
        c6=0
    elif "D&A" in line:
        a=0
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
        c6=0
    elif "M-D" in line:
        a=1
        c1=0
        c2=0
        c3=0
        c4=1
        c5=1
        c6=1
    elif "A-D" in line:
        a=0
        c1=0
        c2=0
        c3=0
        c4=1
        c5=1
        c6=1
    elif "D-M" in line:
        a=1
        c1=0
        c2=1
        c3=0
        c4=0
        c5=1
        c6=1
    elif "D-A" in line:
        a=0
        c1=0
        c2=1
        c3=0
        c4=0
        c5=1
        c6=1 
    elif "D+M" in line:
        a=1
        c1=0
        c2=0
        c3=0
        c4=0
        c5=1
        c6=0
    elif "D+A" in line:
        a=0
        c1=0
        c2=0
        c3=0
        c4=0
        c5=1
        c6=0
    elif "M-1" in line:
        a=1
        c1=1
        c2=1
        c3=0
        c4=0
        c5=1
        c6=0
    elif "A-1" in line:
        a=0
        c1=1
        c2=1
        c3=0
        c4=0
        c5=1
        c6=0
    elif "D-1" in line:
        a=0
        c1=0
        c2=0
        c3=1
        c4=1
        c5=1
        c6=0
    elif "M+1" in line:
        a=1
        c1=1
        c2=1
        c3=0
        c4=1
        c5=1
        c6=1
    elif "A+1" in line:
        a=0
        c1=1
        c2=1
        c3=0
        c4=1
        c5=1
        c6=1
    elif "D+1" in line:
        a=0
        c1=0
        c2=1
        c3=1
        c4=1
        c5=1
        c6=1
    elif "-M" in line:
        a=1
        c1=1
        c2=1
        c3=0
        c4=0
        c5=1
        c6=1
    elif "-A" in line:
        a=0
        c1=1
        c2=1
        c3=0
        c4=0
        c5=1
        c6=1
    elif "-D" in line:
        a=0
        c1=0
        c2=0
        c3=1
        c4=1
        c5=1
        c6=1 
    elif "!M" in line:
        a=1
        c1=1
        c2=1
        c3=0
        c4=0
        c5=0
        c6=1
    elif "!A" in line:
        a=0
        c1=1
        c2=1
        c3=0
        c4=0
        c5=0
        c6=1
    elif "!D" in line:
        a=0
        c1=0
        c2=0
        c3=1
        c4=1
        c5=0
        c6=1
    elif "=M" in line or "M;" in line:
        a=1
        c1=1
        c2=1
        c3=0
        c4=0
        c5=0
        c6=0
    elif "=A" in line or "A;" in line:
        a=0
        c1=1
        c2=1
        c3=0
        c4=0
        c5=0
        c6=0
    elif "=D" in line or "D;" in line:
        a=0
        c1=0
        c2=0
        c3=1
        c4=1
        c5=0
        c6=0
    elif "=-1" in line  or "-1;" in line:
        a=0
        c1=1
        c2=1
        c3=1
        c4=0
        c5=1
        c6=0
    elif "=1" in line or "1;" in line:
        a=0
        c1=1
        c2=1
        c3=1
        c4=1
        c5=1
        c6=1
    elif "=0" in line or "= 0" in line or "0;" in line:
        a=0
        c1=1
        c2=0
        c3=1
        c4=0
        c5=1
        c6=0
    else:
        return -1;
    
    newline=[0]*16
    newline[0]=1
    newline[1]=1
    newline[2]=1
    newline[3]=a
    newline[4]=c1
    newline[5]=c2
    newline[6]=c3
    newline[7]=c4
    newline[8]=c5
    newline[9]=c6
    newline[10]=d1
    newline[11]=d2
    newline[12]=d3
    newline[13]=j1
    newline[14]=j2
    newline[15]=j3
    
    return newline

####################################### d1-d3 #############################################################
def dest_inst(line):
    if "AMD" in line:
        d1=1
        d2=1
        d3=1
    elif "AD" in line:
        d1=1
        d2=1
        d3=0
    elif "AM" in line:
        d1=1
        d2=0
        d3=1
    elif "MD" in line:
        d1=0
        d2=1
        d3=1
    elif "A=" in line or "A =" in line:
        d1=1
        d2=0
        d3=0
    elif "D=" in line or "D =" in line:
        d1=0
        d2=1
        d3=0
    elif "M=" in line or "M =" in line:
        d1=0
        d2=0
        d3=1
    else :
        d1=0
        d2=0
        d3=0
    return d1,d2,d3
	
######################################### Resolve Labels ######################################################

def firstpass(line, symbol_table,inst_num):
    if line[0] == " ":
            line=line.strip()
            line, sep, tail = line.partition('//')
            line=line.strip()
    size=len(line)
    if (line[:2] != "//") and (line[:2] != "/*") and (line[:2] !="/*") and (line != '\n'):
            if line[0] == "(" :
                label = line[1:size-2]
                val = symbol_table.get(label, -1)
                if val == -1:
                    symbol_table[label]=inst_num

    return symbol_table;

########################################## J1 - J3 #########################################################
def jump_inst(line):
    if "JGT" in line:
        j1=0
        j2=0
        j3=1
    elif "JEQ" in line:
        j1=0
        j2=1
        j3=0
    elif "JGE" in line:
        j1=0
        j2=1
        j3=1
    elif "JLT" in line:
        j1=1
        j2=0
        j3=0
    elif "JNE" in line:
        j1=1
        j2=0
        j3=1
    elif "JLE" in line:
        j1=1
        j2=1
        j3=0
    elif "JMP" in line:
        j1=1
        j2=1
        j3=1
    else:
        j1=0
        j2=0
        j3=0
    return j1, j2, j3


############################################################# Translate every input instruction to assembly code #############################################################
def assemble(inputfile, outputfile):
    #create the symbol table
    symbol_table = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576,
        }

    for i in range(0,16):
        lab = "R" + str(i)
        symbol_table[lab] = i


    #Read the asm file for 1st pass
    file_descriptor = open(inputfile, "r")
    inst_num =0
    varloc=16;
    for line in file_descriptor:
        if (line[:2] != "//") and (line[:2] != "/*") and (line[:2] !="/*") and (line != '\n'):
            symbol_table= firstpass(line, symbol_table,inst_num)
            if line[0]!="(" :
                inst_num=inst_num +1


    file_descriptor.close()

    #Read the asm file for 2nd pass
    file_descriptor2 = open(inputfile, "r")

    #Generate the hack file
    with open(outputfile, 'w') as hack_file:
        newline=[0]*16
        memory =0
        for line in file_descriptor2:
            if line[0] == " ":
                line=line.strip()
                line, sep, tail = line.partition('//')
                line=line.strip()
            size=len(line)    
            if (line[:2] != "//") and (line[:2] != "/*") and (line[:2] !="/*") and (line != '\n'):
                if line[0] == '@' and line[1].isalpha() :
                    variable = line[1:size]
                    if line[size-1] == '\n':
                        variable = line[1:size-1] 
                    val = symbol_table.get(variable, -1)
                    if val == -1 :
                        symbol_table[variable]=varloc;
                        varloc=varloc+1;
                #@ instruction
                if line[0] == '@' :
                    if line[1].isnumeric() :
                        newline = A_inst_conv_num(line)
                    elif line[1].isalpha() :
                        labelOrVar=str(line[1:size])
                        if line[size-1] == '\n':
                            labelOrVar=line[1:size-1]
                        memory = symbol_table[labelOrVar]
                        line = line.replace(labelOrVar, str(memory))
                        newline = A_inst_conv_num(line)
                    s = [str(i) for i in newline] 
                    str_newline = "".join(s)
                    hack_file.write(str_newline +'\n')
                elif line[:1].isalpha() or line[0].isnumeric():
                    newline=C_inst_conv(line)
                    if newline == -1:
                        print("Invalid Syntax")
                        break;
                    s = [str(i) for i in newline] 
                    str_newline = "".join(s)
                    hack_file.write(str_newline +'\n')
                elif line[0] != "(" :
                    print("Invalid Syntax")
                    break;

    file_descriptor2.close()
    hack_file.close()
    