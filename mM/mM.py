import sys

try:
    with open(sys.argv[2], "r") as mM_file:
        with open(sys.argv[3], "w") as out_file:
            for line in mM_file:
                for char in line:
                    if char == "m":
                        out_file.write("M")
                    elif char == "M":
                        out_file.write("m")
                    else:
                        out_file.write(char)

except:
    print("USAGE: mm.py [input_file] [output_file]")
