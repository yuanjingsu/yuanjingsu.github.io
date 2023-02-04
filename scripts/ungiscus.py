mess='''
<script src="https://giscus.app/client.js"
    data-repo="liuzihaohao/liuzihaohao.github.io"
    data-repo-id="R_kgDOI3HDkw"
    data-category="Announcements"
    data-category-id="DIC_kwDOI3HDk84CT4T2"
    data-mapping="pathname"
    data-strict="1"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="top"
    data-theme="preferred_color_scheme"
    data-lang="zh-CN"
    data-loading="lazy"
    crossorigin="anonymous"
    async>
</script>'''
import re,os
BASE_DIR_DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'docs')
print("[Look at]",BASE_DIR_DOCS)
for a,b,c in os.walk(BASE_DIR_DOCS):
    print(a)
    for i in c:
        if i[-3:]=='.md' and a!="home-page.md":
            dq=str(os.path.join(a,i))
            print("[Found out]",dq)
            cc=""
            with open(dq,'r+',encoding="utf-8") as fp:
                cc=fp.read().replace(mess,"")
            with open(dq,'w',encoding="utf-8") as fp:
                fp.write(cc)
print("OK..")