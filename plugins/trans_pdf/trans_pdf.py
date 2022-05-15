# develop a plugins, need add transer's path to env, if not you can not import it
import pdfplumber

# class pdf
class pdf:
    # init
    def __init__(self, path):
        self.path = path
        self.pdfPages = pdfplumber.open(self.path)

    # write new file
    def pdfWriter(self, res):  
        f=open('test1.txt','a+',encoding="utf-8") #test1是已经存在于当前目录下的文档
        f.write(res)
        f.close
        return

    # paf pages
    def getPdfpages(self):
        return self.pdfPages.pages