import os,time

DISP = """# 在此编写题目

> 本文档编写于 {}/{}/{}
"""

def qzero(x):
    if len(x)==1:
        return "0"+x
    else:
        return x
    
def findnow(path_d):
    nwo=0
    for a,b,c in os.walk(path_d):
        for i in c:
            if int(i.split(".")[0])>nwo:
                nwo=int(i.split(".")[0])
    return nwo+1

BASE_DIR_DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'docs')
print("[Look at]",BASE_DIR_DOCS)

now = time.localtime()
print("[Now]",now.tm_year,"/",now.tm_mon,"/",now.tm_mday)

cr_dir = os.path.join(BASE_DIR_DOCS,str(now.tm_year),qzero(str(now.tm_mon)))
print("[Cr_dir]",cr_dir)
try:
    os.makedirs(cr_dir)
except FileExistsError:
    pass

nowss = str(findnow(cr_dir))+".md"
print("[Cr_md]",os.path.join(cr_dir,nowss))
with open(os.path.join(cr_dir,nowss),"x",encoding="utf-8") as fp:
    fp.write(DISP.format(str(now.tm_year),qzero(str(now.tm_mon)),qzero(str(now.tm_mday))))

os.system("\""+str(os.path.join(cr_dir,nowss))+"\"")