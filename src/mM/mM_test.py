import codecs
import filecmp

import mM

# Test 1
with open("../../data/mM/testfiles/test1.in", "w") as test1:
    for i in range(100):
        # Every other character is m, the rest are M
        if i % 2 == 0:
            test1.write("m")
        else:
            test1.write("M")
correct_string = "".join(["M" if i % 2 == 0 else "m" for i in range(100)])

# Run program on in file
mM.mM("../../data/mM/testfiles/test1.in", "../../data/mM/testfiles/test1.out")
with open("../../data/mM/testfiles/test1.out", "r") as out:
    # compare to correct file
    assert("\n".join(out.readlines()) == correct_string)

# Test 2
with open("../../data/mM/testfiles/test2.in", "w") as test2:
    with open("../../data/mM/testfiles/test2.correct", "w") as correct_string:
        # 1000 lines
        for i in range(1000):
            for j in range(100):
                # Every 50th line has unicode stuff
                if i % 50 != 0:
                    # Every other character is m, the rest are M
                    if j % 2 == 0:
                        test2.write("m".encode("utf-8"))
                        # Write opposite char to correct string file
                        correct_string.write("M".encode("utf-8"))
                    else:
                        test2.write("M".encode("utf-8"))
                        # Write opposite char to correct string file
                        correct_string.write("m".encode("utf-8"))
                else:
                    test2.write(u'\x79'.encode("utf-8"))
                    # Char should remain the same
                    correct_string.write(u'\x79'.encode("utf-8"))
            test2.write("\n".encode("utf-8"))
            correct_string.write("\n".encode("utf-8"))

# print correct_string
mM.mM("../../data/mM/testfiles/test2.in", "../../data/mM/testfiles/test2.out")
with codecs.open("../../data/mM/testfiles/test2.out", encoding='utf-8', mode="r") as out:
    # print correct_string
    # uses filecmp because it has issues with strings and unicode character comparison, but the switching works
    assert(filecmp.cmp("../../data/mM/testfiles/test2.out", "../../data/mM/testfiles/test2.correct"))

# If it reaches the end, it's good
print("All tests passed!")