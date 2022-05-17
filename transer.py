#
#!A cross platform and light translate tool made by python
#
# Licensed under the GNU GENERAL PUBLIC LICENSE
#
# Copyright (C) 2022-present, SongZihui-sudo.
#
# @author      SongZihui-sudo
# @file        transer.py
#
from tkinter import ttk
from matplotlib.pyplot import get
import pyperclip
import tkinter
import keyboard
import json
import requests
import time
import sys
import plugins.trans_pdf.trans_pdf as transPdf

# global var
text_res = ""
text_src = ""


# main windows
class mainWindow:

    # Constructor
    def __init__(self, json_data):
        self.json_data = json_data
        self.background_color = json_data['themeConfig'][self.json_data['theme']]['background-color']
        self.frontground_color = json_data['themeConfig'][self.json_data['theme']]['frontground-color']
        self.font_color = json_data['themeConfig'][self.json_data['theme']]['font-color']
        self.transparency = json_data['themeConfig'][self.json_data['theme']]['transparency']
        # default api
        self.curApi = json_data['api'][0]
        # default api name
        self.curApiname = 'google'
        self.src = ""
        self.res = ""
        self.language = json_data['outLanguage']
        return

    # about
    def about(self):
        self.aw = tkinter.Toplevel()
        self.aw.geometry('200x320')
        self.aw.iconphoto(False, tkinter.PhotoImage(file='transer.png'))
        txt = "Transer v1.0\n"+ \
            "A linux translate tool\n" + \
            "author:\n" + \
            "SongZihui-sudo\n"+ \
            "LICENSE:\n"+\
            "GNU GENERAL PUBLIC LICENSE\n" +\
            "github:\n"+\
            "https://github.com/SongZihui-sudo/transer\n" 
        msg = tkinter.Message(self.aw, text=txt, width = 200, anchor = "w", justify = "left", bg = self.background_color, 
        fg = self.font_color)
        msg.grid(row=0, column=0)    
        return

    # creat window
    def creatWindow(self):
        # main windows
        self.main = tkinter.Tk()
        self.main.geometry('550x340')
        self.main.title("transer")
        self.main.attributes("-alpha", self.transparency)
        self.main.config(background = self.background_color)
        self.main.iconphoto(False, tkinter.PhotoImage(file='transer.png'))

        # about botton
        self.aboutBottom = tkinter.Button(self.main, text="about", command=lambda: self.about(), relief="raised", 
        fg = self.font_color, bg = self.background_color)
        self.aboutBottom.place(x=0, y=0)
        
        title = tkinter.Message(self.main, text="transer", font=('Arial', 12), width = 200, anchor = "w", 
        justify = "left", bg = self.background_color, fg = self.font_color)
        title.place(x=80, y= 0)

        # input
        input = tkinter.Entry(self.main, width=21, bg = self.background_color, fg = self.font_color)
        input.configure(insertbackground = self.font_color)
        input.place(x=1, y=60)

        # search botton
        self.searchBottom = tkinter.Button(self.main, text="search", command=lambda: self.requestApi(input.get()), 
        relief="raised", fg = self.font_color, bg = self.background_color)
        self.searchBottom.place(x=60, y=100)

        # msg show
        srcTip = tkinter.Message(self.main, text="original", font=('Arial', 12), width = 200, anchor = "w", 
        justify = "left", bg = self.background_color, fg = self.font_color)
        srcTip.place(x=50, y=140)

        # src show
        global text_src
        self.srcMsg = tkinter.Text(self.main, font=('Arial', 9), width=22, height=8, bg = self.background_color, fg = self.font_color)
        self.srcMsg.insert("insert", text_src)
        self.srcMsg.place(x=1, y=175)

        # res show
        resTip = tkinter.Message(self.main, text="result", font=('Arial', 12), width = 200, anchor = "w", 
        justify = "left", bg = self.background_color, fg = self.font_color)
        resTip.place(x=220, y=0)

        # result show
        global text_res
        self.resMsg = tkinter.Text(self.main, font=('Arial', 9), width=35, height=15, bg = self.background_color, fg = self.font_color)
        self.resMsg.insert("insert", text_res)
        self.resMsg.place(x=220, y=40)

        self.main.mainloop()
        return self.main

    # restart
    def restart(self):
        self.destory()
        self.creatWindow()
        return

    # destory
    def destory(self):
        self.main.destroy()
        return

    # waiting hotkey press key
    def hotkey(self):
        # translate
        keyboard.add_hotkey(self.json_data['hotkey']['translate'], lambda: self.requestApi(""))
        # open
        keyboard.add_hotkey(self.json_data['hotkey']['open_windows'], lambda: self.creatWindow())
        return
    
    # get main win
    def getMainwin(self):
        return self.main

    # get about win
    def aboutWin(self):
        return self.aw

    # set result
    def setResult(self, res):
        # result
        global text_res
        text_res = res
        self.res = res

    # set src
    def setSrc(self, src):
        # src
        global text_src
        text_src = src
        self.src = src

    # get src
    def getSrc(self):
        return self.src

    # get res
    def getRes(self):
        return self.res

    # set language
    def setLanguage(self, changed):
        self.language = changed

    # get cur language
    def getLanguage(self):
        return self.language

    # request apis
    def requestApi(self, src):
        if src == "":
            cur = getCut()
            self.setSrc(cur)
        else:
            print(src)
            self.setSrc(src)
        
        # google
        if self.curApiname == 'google':
            parman = self.curApi[self.curApiname][0]
            parman = parman +\
                self.json_data['language'][self.language] +\
                self.curApi[self.curApiname][1]
            r = parman + self.src +self.curApi[self.curApiname][2]    
            try:
                # request
                req = requests.get(r)
                # get result
                if int(req.status_code) != 200 :
                    print("error! connect failed!")
                else:
                    res = json.loads(req.text)
                    result = ""
                    for i in range(len(res['sentences'])-1):
                        self.setResult(res['sentences'][i]['trans'])
                        result+=self.getRes()
                    print(result)
                    self.setResult(result)
            except Exception as e:
                print(e)
        # youdao
        elif self.curApiname == 'youdao':
            return
        # baidu
        elif self.curApiname == 'baidu':
            return
        # 360
        elif self.curApiname == '360':
            return
        # error
        else:
            print("error! unknown translate api")
        
        # cover cli
        if self.json_data['isCovercli'] == True:
            pyperclip.copy(text_res)
        # gui
        if self.json_data['gui'] == True and src == "":
            # creat main window
            self.creatWindow()
        elif self.json_data['gui'] == False:
            pyperclip.copy(text_res)
        elif self.json_data['gui'] == True and src and len(sys.argv) > 1:
            return 0
        else :
            self.restart()
        return

# read json
def jsonReader(path):
    with open(path, 'r', encoding='utf8') as fp:
        json_data = json.load(fp)
    return json_data

# cut version
def getCut():
    return pyperclip.waitForPaste()

# write json
def jsonWrite(path, json_data):
    with open(path,"w") as fp:
        json.dump(json_data, fp)
    return 0

# main
def main(): 
    json_data = jsonReader('./config.json')        
    mainWin = mainWindow(json_data)
    # translate select
    if len(sys.argv) == 1:
        # wait hotkey
        while True:
            mainWin.hotkey()
            keyboard.wait()
            # wait 0.1 sec
            time.sleep(0.1)
    # pugins
    elif len(sys.argv) > 1 and json_data['enablePlugins'] == True:
        for i in range(len(sys.argv)):
            if sys.argv[i] == json_data['Args']['src']:
                file = sys.argv[i+1]
            if sys.argv[i] == json_data['Args']['output']:
                print(json_data['Args']['output']['-version'])
                return 0
            if sys.argv[i] == json_data['Args']['theme']:
                json_data['theme'] = sys.argv[i+1]
                jsonWrite('./config.json', json_data)
                return 0
            if sys.argv[i] == json_data['Args']['language']:
                json_data['outLanguage'] = sys.argv[i+1]
                jsonWrite('./config.json', json_data)
                return 0
            # plugin trans-pdf -----------------------------------------------------
            if sys.argv[i] == json_data['Args']['trans-pdf']['arg']:
                p = transPdf.pdf(file)
                pages = p.getPdfpages()
                print(len(pages))
                for i in pages:
                    mainWin.requestApi(i.extract_text())
                    res = mainWin.getRes()
                    p.pdfWriter(res)
            #--------------------------------------------------------------------------
                return 0
        return 0
    else:
        return -1
main()
