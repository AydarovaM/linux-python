import subprocess

folder_in = "folder_in"
folder_out = "/home/user/out"
folder_ext = "/home/user/folder1"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        print(result.stdout)
        return False
    
def test_step1():
    # test1
    res1 = checkout("cd {} && 7z a {}/arx2".format(folder_in, folder_out), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_out), "arx2.7z")
    assert res1 and res2, "test1 FAIL"

def test2_step():
    # test2
    res1 = checkout("cd {} && 7z e arx2.7z -o{} -y".format(folder_out, folder_ext), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_ext), "test1")
    res3 = checkout("ls {}".format(folder_ext), "test2")
    assert res1 and res2 and res3, "test2 FAIL"

def test3_step():
    # test3
    assert checkout("cd {} && 7z t arx2.7z".format(folder_out), "Everything is Ok"), "test3 FAIL"

def test_step4():
    # test4
    assert checkout("cd {} && 7z u {}/arx2.7z".format(folder_in, folder_out), "Everything is Ok"), "test4 FAIL"

def test_step6_list():
    # test6
    assert checkout("cd {} && 7z l arx2.7z".format(folder_out), "test1"), "test6 FAIL"
    assert checkout("cd {} && 7z l arx2.7z".format(folder_out), "subdir/hello.txt"), "test6 FAIL"

def test_step7_extract():
    # test7
    res1 = checkout("cd {} && 7z x arx2.7z -o{} -y".format(folder_out, folder_ext), "Everything is Ok")
    res2 = checkout("ls {}/subdir".format(folder_ext), "hello.txt")
    assert res1 and res2, "test7 FAIL"

def test_step8_hash():
    # test8
    result = subprocess.run("crc32 {}/arx2.7z".format(folder_out), shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    assert result.returncode == 0, "test8 FAIL"
    hash = result.stdout.upper()
    
    assert checkout("7z h {}/arx2.7z".format(folder_out), hash), "test8 FAIL"
    

def test_step5():
    # test5
    assert checkout("cd {} && 7z d arx2.7z".format(folder_out), "Everything is Ok"), "test5 FAIL"

