import sys
import os

try:
    with open(sys.argv[1], "r") as mM_file:
        # Uses .tmp so that if they are the same file, it won't conflict
        with open(sys.argv[2] + ".tmp", "w") as out_file:
            for line in mM_file:
                # print line
                for char in line:
                    # print char
                    if char == "m":
                        out_file.write("M")
                    elif char == "M":
                        out_file.write("m")
                    else:
                        out_file.write(char)
    # Rename file back to what it was asked to be
    os.rename(sys.argv[2] + ".tmp", sys.argv[2])


except:
    print "USAGE: mM.py [input_file] [output_file]"
    print "You entered: " + " ".join(sys.argv)