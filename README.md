# qtile_wm_config
Simplistic config for qtile window manager.  
Based on Lubuntu 20.04 LTS / 22.04LTS, not tested on Wayland yet.  

# -------------------------------------------------------------------  
Dependencies includes: suckless-tools (dmenu), kitty, dropbox is included to test autoStart  

recommended programs: xscreensaver, Kvantum, lxappearance, qt5ct, nitrogen
Note that auto start commands are locates at autoStart.sh, same as config.py  
OBS: chmod +x autoStart.sh before running 

added list for colors for easy wm color management.  
added get pavaudio control by right lick the widget.  
added function mod + b to hide bar.  
#components are a little messy in the config file

apply config to URxvt: xrdb .Xresources

# ---------------------------------------------------------------------  
Known Bugs: Text Clock may stop ticking after hiding the bar
