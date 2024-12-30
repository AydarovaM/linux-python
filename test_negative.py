from checkers import checkout_negative

folder_in = "folder_in"
folder_out = "/home/user/out"
folder_ext = "/home/user/folder1"

def test_nstep1():
    # test neg 1
    assert checkout_negative("cd {} && 7z e arx3.7z -o{} -y".format(folder_out, folder_ext), "ERROR:"), "test1 FAIL"

def test_nstep2():
    # test neg 2
    assert checkout_negative("cd {} && 7z t arx3.7z".format(folder_out), "ERROR:"), "test2 FAIL"