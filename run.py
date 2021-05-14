import sys
import os.path
import Assembler

inputfile= sys.argv[1]
inputfile = inputfile.strip()
if os.path.isfile(inputfile)== False:
    print("File Not Found, Check Path");
    sys.exit()
size=len(inputfile)
if inputfile[size-3:size] != "asm":
    print("Wrong Format")
else:
    outputfile = inputfile.replace("asm","hack")
    Assembler.assemble(inputfile, outputfile)
    
