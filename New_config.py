# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
#from libqtile.utils import guess_terminal

mod = "mod4"
#terminal = guess_terminal()

# Colors
colors = list(["#000000", #black 00-0000 Black BarBackground
          "#05475c", #deb_12 00-0000 Blue dmenuBackground
          "#f07867", #pantone 16-1546 Living_Coral focus_border dmenuFocus
          "#d1899b", #pantone 493C pink normal_border
          "#fae753", #pantone 12-0643 Blazing_Yellow barClock
          "#91af59", #pantone 15-0343 Greenery barVol
          "#9eaead", #pantone 15-4706 Grey Mist barDate
          "#4d7c8e", #pantone 17-4421 Lakrspur barFocus
          "#000000", #black 00-0000 Black TabBackground
          "#ffffff" #white
          ])

gap = 10  #panel gap
borderWith = 5 #border size
fontSize = 18 

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("urxvt"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn(f"dmenu_run -i -nb '{colors[1]}' -sb '{colors[2]}' -nf '{colors[-1]}' -sf '{colors[0]}' -fn 'Ubuntu-14' -b"), desc="Spawn dmenu"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "x", lazy.spawn("xscreensaver-command -lock")),
    Key([mod], "b", lazy.hide_show_bar(), desc="Hides the bar"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            Key(
                [mod],
                "Right",
                lazy.screen.next_group(),
                desc="Switch to the group on the Right".format(i.name),
            ),
            Key(
                [mod],
                "Left",
                lazy.screen.prev_group(),
                desc="Switch to the group on the Left".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(border_focus=colors[2],
                     border_normal=colors[3],
                     border_width=borderWith,
                     margin=gap,
                     single_border_with=borderWith,
                     single_margin=gap),
    #layout.Columns(border_focus=colors[2],
    #               border_normal=colors[4],
    #               border_width=borderWith,
    #               border_on_single=True,
    #               margin=gap),
    layout.Max(border_focus=colors[2],
               border_normal=colors[3],
               border_width=0),
    #layout.Stack(num_stacks=2),
    layout.Floating(border_focus=colors[2],
                    border_normal=colors[3],
                    border_width=borderWith),
    #layout.Bsp(),
    layout.Matrix(border_focus=colors[2],
                  border_normal=colors[3],
                  border_width=borderWith,
                  margin=[gap, gap, gap, gap]),
    #layout.MonadWide(),
    #layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font="Ubuntu",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

@lazy.function
def launch_powermenu(qtile):
    qtile.cmd_spawn('pavucontrol')

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(linewidth=0,
                           padding = 5),
                widget.CurrentLayoutIcon(foreground=colors[0],
                                         background=colors[7],
                                         fontsize = fontSize,
                                         scale=0.8),
                widget.Sep(linewidth=0,
                           padding=5),
                widget.GroupBox(background=colors[0],
                                fontsize = fontSize,
                                use_mouse_wheel=True,
                                this_current_screen_border=colors[7],
                                active=colors[-1], 
                                highlight_method='border'),
                #widget.Prompt(fontsize = fontSize),
                widget.Sep(linewidth=0,
                           padding=5),
                widget.WindowTabs(background=colors[8],
                                  fmt='[{}]',
                                  padding = 5,
                                  fontsize = fontSize),
                #widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.KeyboardLayout(configured_keyboards=['se'],
                                      fontsize = fontSize),
                widget.Systray(icon_size = 25,
                               padding = 5),
                widget.Sep(linewidth=0,
                           padding = 10),
                widget.PulseVolume(fmt=' Vol.: {} ',
                                   fontsize = fontSize,
                                   background=colors[5],
                                   foreground=colors[0],
                                   mouse_callbacks={'Button3':lazy.spawn('pavucontrol')}),
                #widget.Battery(fmt='Bat.: {}',
                #               format='{char} {percent:2.0%}',
                #               background=colors[4],
                #               foreground=colors[0]),
                widget.Clock(background=colors[6],
                             foreground=colors[0],
                             fontsize = fontSize,
                             format=" w.%V | %a %b. %d ",
                             update_interval = 1.0
                             ),
                widget.Clock(background=colors[4],
                             foreground=colors[0],
                             fontsize = fontSize,
                             format=" %T "),
                #widget.QuickExit(background=colors[6],
                #                 foreground=colors[0],
                #                 default_text='[Quit]',
                #                 countdown_format='[{}]'),
                widget.Sep(linewidth=0,
                           padding = 5),
            ],
            size=28,
            border_width=[3,3,3,3],
            margin=[0,0,0,0],
            #opacity=1,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(foreground=colors[0],
                                         background=colors[7],
                                         scale=0.6),
                widget.GroupBox(background=colors[0],
                                use_mouse_wheel=True,
                                this_current_screen_border=colors[1],
                                active=colors[-1],
                                highlight_method='block'),
                widget.Prompt(),
                widget.WindowTabs(fmt='[{}]',
                                  padding = 5),       
            ],
            size=24,
            border_width=[2,2,2,2],
            margin=[4,gap,0,gap],
            opacity=1,
            )
        )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=colors[2],
    border_normal=colors[3],
    border_width=borderWith,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#auto start
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autoStart.sh')
    subprocess.run([home])
