import sys
import os
import codecs


def mM(in_file_name, out_file_name):
    with codecs.open(in_file_name, encoding='utf-8', mode="r") as mM_file:
        # Uses .tmp so that if they are the same file, it won't conflict
        with open(out_file_name + ".tmp", "w") as out_file:
            for line in mM_file:
                # print line
                for char in line:
                    # print char
                    # Write M if m, m if M, char if neither
                    if char == "m":
                        out_file.write("M".encode("utf-8"))
                    elif char == "M":
                        out_file.write("m".encode("utf-8"))
                    else:
                        out_file.write(char.encode("utf-8"))
    # Rename file back to what it was asked to be
    os.rename(out_file_name + ".tmp", out_file_name)


if __name__ == '__main__':
    try:
        mM(sys.argv[1], sys.argv[2])
    except Exception, err:
        # print Exception, err
        print "USAGE: mM.py [input_file] [output_file]"
        print "If you entered everything correctly, there is some problem with"
        print "either file encoding or this code."
        # print "You entered: " + " ".join(sys.argv)