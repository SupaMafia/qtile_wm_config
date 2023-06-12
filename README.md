## The qtile project
https://github.com/qtile/qtile <br>
Thanks for the great window manager

## qtile_wm_config
Simplistic config for qtile window manager.<br>
Based on Lubuntu 20.04 LTS / 22.04LTS

## config Features
added list for colors for easy wm color management. <br>
added get pavaudio control by right lick the widget. (broken under debian 12)  <br>
added function mod + b to hide bar.  <br>
components are a little messy in the config file.

## Dependencies
suckless-tools (dmenu), urxvt, dropbox is included to test autoStart.

## Some recommended program
xscreensaver, Kvantum, lxappearance, qt5ct, nitrogen.<br>
Note that auto start commands are locates at autoStart.sh, same as config.py  <br>
```chmod +x autoStart.sh``` before running.<br>
apply config to URxvt: ```xrdb .Xresources```

## wayland
something something :)

## Known Bugs 
Text Clock stop ticking after hiding the bar.<br>
Need to reload the config to make it tick again.

## Problems with debian 12:
Problems with debian 12 as of June 12th 2023: 
1. pip install of qtile broken: ERROR: externally managed software, 
2. dependency issue with xcffib: ModuleNotFoundError
3. pavaudio control widget broken
### solution to problem 1 and 2:
(install qtile in python3 venv in debian 12)
1. ```sudo apt install python3-venv``` dependency
2. ```sudo apt install python3-pip```  dependency
3. ```python3 -m venv qtile``` create venv
4. ```qtile/bin/pip install --no-cache-dir xcffib==1.3.0``` version
5. ```qtile/bin/pip install --no-cache-dir cairocffi==1.4.0``` version
6. ```qtile/bin/pip install --no-use-pep517 --no-build-isolation qtile```
if fail, use remove the qtile folder and try again: rm -rf qtile <br>
then create the desktop entry:
```
  [Desktop Entry]
  Name=Qtile
  Comment=Qtile Session
  Exec=qtile/bin/qtile start
  Type=Application
  Keywords=wm;tiling
```



