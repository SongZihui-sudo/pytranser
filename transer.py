#
#!A cross platform and light translate tool made by python
#
# Licensed under the GNU GENERAL PUBLIC LICENSE
#
# Copyright (C) 2022-present, SongZihui-sudo.
#
# @author      SongZihui-suao
# @file        transer.py
#
import pyperclip
import tkinter
import keyboard
import json
import requests
import time

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
        return

    # about
    def about(self):
        self.aw = tkinter.Toplevel()
        self.aw.geometry('200x300')
        self.aw.iconphoto(False, tkinter.PhotoImage(file='transer.png'))
        txt = "Transer v1.0\n"+ \
            "A linux translate tool\n" + \
            "author:\n" + \
            "SongZihui-sudo\n"+ \
            "LICENSE:\n"+\
            "GNU GENERAL PUBLIC LICENSE\n" +\
            "github:\n"+\
            "" 
        msg = tkinter.Message(self.aw, text=txt, width = 200, anchor = "w", justify = "left", bg = self.background_color, fg = self.font_color)
        msg.grid(row=0, column=0)    
        return

    # creat window
    def creatWindow(self):
        self.main = tkinter.Tk()
        self.main.geometry('200x300')
        self.main.title("transer")
        self.main.resizable()
        self.main.attributes("-alpha", self.transparency)
        self.main.config(background = self.background_color)
        self.main.iconphoto(False, tkinter.PhotoImage(file='transer.png'))
        
        # about botton
        self.aboutBottom = tkinter.Button(self.main, text="about", command=lambda: self.about(), relief="raised")
        self.aboutBottom.grid(row=0, column=0)
        
        title = tkinter.Message(self.main, text="transer", font=('Arial', 12), width = 200, anchor = "w", 
        justify = "left", bg = self.background_color, fg = self.font_color)
        title.grid(row=1, column=0)

        # input
        input = tkinter.Entry(self.main, width=24)
        input.grid(row=2, column=0)

        # search botton
        self.searchBottom = tkinter.Button(self.main, text="search", command=lambda: self.requestApi(input.get()), relief="raised")
        self.searchBottom.grid(row=3, column=0)
        
        srcTip = tkinter.Message(self.main, text="original", font=('Arial', 12), width = 200, anchor = "w", 
        justify = "left", bg = self.background_color, fg = self.font_color)
        srcTip.grid(row=4, column=0)

        # src show
        global text_src
        self.srcMsg = tkinter.Text(self.main, font=('Arial', 12), width=16, height=1, bg = self.background_color, fg = self.font_color)
        self.srcMsg.insert("insert", text_src)
        self.srcMsg.grid(row=5, column=0)

        resTip = tkinter.Message(self.main, text="result", font=('Arial', 12), width = 200, anchor = "w", 
        justify = "left", bg = self.background_color, fg = self.font_color)
        resTip.grid(row=6, column=0)

        # result show
        global text_res
        self.resMsg = tkinter.Text(self.main, font=('Arial', 12), width=16, height=1, bg = self.background_color, fg = self.font_color)
        self.resMsg.insert("insert", text_res)
        self.resMsg.grid(row=7, column=0)

        self.main.mainloop()
        return self.main

    # restart
    def restart(self):
        self.main.destroy()
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
        return self.res

    # set src
    def setSrc(self, src):
        # src
        global text_src
        text_src = src
        self.src = src
        return self.src

    # get src
    def getSrc(self):
        return self.src

    # get res
    def getRes(self):
        return self.res

    # request apis
    def requestApi(self, src):
        if src == "":
            self.setSrc(getCut())
        else:
            self.setSrc(src)
        
        # google
        if self.curApiname == 'google':
            parman = self.curApi[self.curApiname][0]
            parman = parman +\
                self.json_data['language'][self.json_data['default_outlanguage']] +\
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
                    result = self.setResult(res['sentences'][0]['trans'])
                    print(result)
            except:
                print("connect error!")
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

# main
def main():
    json_data = jsonReader('./config.json')
    mainWin = mainWindow(json_data)
    # wait hotkey
    while True:
        mainWin.hotkey()
        keyboard.wait()
        # wait 0.1 sec
        time.sleep(0.1)

main()
