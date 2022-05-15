# Transer --A cross platform and light translate tool

- [Transer --A cross platform and light translate tool](#transer---a-cross-platform-and-light-translate-tool)
  - [About](#about)
    - [screenshot](#screenshot)
  - [Let's Start](#lets-start)
    - [install](#install)
    - [run](#run)
    - [package](#package)
      - [Linux dependence](#linux-dependence)
    - [How to use](#how-to-use)
    - [Config](#config)
  - [Dev](#dev)
  - [known issues](#known-issues)
  - [plugins Dev](#plugins-dev)
  - [Transer's Api](#transers-api)
  - [last](#last)

## About
A cross platform and light translate tool made by python.    
### screenshot
![img](https://user-images.githubusercontent.com/77034643/168425961-92310029-6b9e-49e4-8b0e-240afe6bd3b3.png)  
<div align=center><img src="https://user-images.githubusercontent.com/77034643/168418694-12fd4fb3-d642-420f-85bb-b32a7369fcd1.png"></div>

## Let's Start
### install
1. download the release in the github

2. clone sourse to you local.
```bash
pip install -r requirements.txt
```
```bash
git clone https://github.com/SongZihui-sudo/transer
```
### run
```bash
git clone https://github.com/SongZihui-sudo/transer
sudo root  
python3 transer.py
```
or
click `transer`
### package
#### Linux dependence
*in linux have some error in transer package you can install some packages to solve it*  
```bash
xsel
xclip
python3-tk
tk-dev
``` 
```bash
python3 install.py  
(in linux may be you need sudo)
```
### How to use  
Firstly `ctrl+c or ctrl+shift+c` copy what you want to translate
* `ctrl+alt+z` translate
* `ctrl+alt+s` open main window   
* `python3 transer.py -s [pdf's path] -pt` or `./transer.py -s [pdf's path] -pt`(in linux you need add sudo)  translate pdf file to txt file.  
### Config
*you can make some configs in the config.json*  
`default_outlanguage` default output language  
`gui` is open gui mode.if you close the gui,the result will cover clipboard.In the gui mode, the result will not cover the clipboard defaultly.  
`isCovercli`  up  
`theme` theme  
`hotkey` config about hotkey  
`themeConfig` custom theme  
you can make you own theme like this:
```json
"theme name":{
  "theme":"", // theme name
  "font-color":"",// words color
  "background-color":"",// background color
  "frontground-color":"", // frontground color 
  "transparency":"" // transparency
}
```
`api` translate api  
`language` language  
`plugin` plugin is in developing
## Dev
*Some devlop directions in the future:*  
1. new theme
2. new api
3. more beautiful gui design  
4. plugin    
   
in linux
```bash
su root
python3 transer.py
```
in other system
```bash
python3 transer.py
```
*Welcome to contribute to this project!*  
I will update and maintain for a long time.
## known issues
in linux:  
```txt
_tkinter.TclError: no display name and no $DISPLAY environment variable 
and
Pyperclip could not find a copy/paste mechanism for your system.
```
`su root`before use
## plugins Dev
*I am going to devlop plugins in this tool.*
the plugins is in the plugins dir.  
directory structure:  

---
plugins |  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; plugin's name |<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;main.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requirements.txt

---
you can register your p;ugins in config.json.    
like trans-pdf pugin(which can translate pdf file to a txt)   
```json
"trans-pdf":{
            "arg":"-pt",
            "file":"./plugins/trans-pdf/trans-pdf.py"
        },
```
`arg` comands args  
`file` file postion
```py
 if sys.argv[i] == json_data['Args']['trans-pdf']['arg']:
                p = transPdf.pdf(file)
                pages = p.getPdfpages()
                print(len(pages))
                for i in pages:
                    mainWin.requestApi(i.extract_text())
                    res = mainWin.getRes()
                    p.pdfWriter(res)
                return 0
```
add if brancg to add a plugin.  
## Transer's Api
1. `mainWindow.destory(void)` reurn void ; destory main window
2. `mainWindow.getMainwin(void)` return main window obj  
3. `mainWindow.getSrc(void)` return sourse language's word or sentience
4. `mainWindow.getRes(void)` return result
5. `mainWindow.requestApi(src)` return void; make a request; if src == void,transer will translate sentience in the cli.else src,transer will translate src.  
## last
If you get a bug about it, please make a issue in github, thanks.
If you think transer is good, please give me a star, thanks.  
