import os
import mM
import codecs
import filecmp

# Test 1
with open("testfiles/test1.in", "w") as test1:
    for i in range(100):
        if i % 2 == 0:
            test1.write("m")
        else:
            test1.write("M")
correct_string = "".join(["M" if i % 2 == 0 else "m" for i in range(100)])
mM.mM("testfiles/test1.in", "testfiles/test1.out")
with open("testfiles/test1.out", "r") as out:
    assert("\n".join(out.readlines()) == correct_string)

# Test 2
with open("testfiles/test2.in", "w") as test2:
    with open("testfiles/test2.correct", "w") as correct_string:
        for i in range(1000):
            for j in range(100):
                if i % 50 != 0:
                    if j % 2 == 0:
                        test2.write("m".encode("utf-8"))
                        correct_string.write("M".encode("utf-8"))
                    else:
                        test2.write("M".encode("utf-8"))
                        correct_string.write("m".encode("utf-8"))
                else:
                    test2.write(u'\x79'.encode("utf-8"))
                    correct_string.write(u'\x79'.encode("utf-8"))
            test2.write("\n".encode("utf-8"))
            correct_string.write("\n".encode("utf-8"))

# print correct_string
mM.mM("testfiles/test2.in", "testfiles/test2.out")
with codecs.open("testfiles/test2.out", encoding='utf-8', mode="r") as out:
    # print correct_string
    assert(filecmp.cmp("testfiles/test2.out", "testfiles/test2.correct"))

print("All tests passed!")