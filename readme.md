# Transer --A cross platform translate tool

- [Transer --A cross platform translate tool](#transer---a-cross-platform-translate-tool)
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
  - [last](#last)

## About
A cross platform translate tool made by python.    
### screenshot
![img](https://user-images.githubusercontent.com/77034643/168419118-d59b6e42-c089-4a1c-ae39-df1d36809c43.png)  
<div align=center><img src="https://user-images.githubusercontent.com/77034643/168418694-12fd4fb3-d642-420f-85bb-b32a7369fcd1.png"></div>

## Let's Start
### install
1. download the release in the github

2. clone sourse to you local.
```bash
git clone 
```
### run
```bash
git clone 
sudo python3 transer.py
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
5. solve package error
   ```
   _tkinter.TclError: no display name and no $DISPLAY environment variable 
   and
   Pyperclip could not find a copy/paste mechanism for your system.
   ```
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
## last
If you get a bug about it, please make a issue in github, thanks.
If you think transer is good, please give me a star, thanks.  
