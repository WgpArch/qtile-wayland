
from typing import List
import os
import re
import socket
import subprocess
from enum import Enum
from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
alt = "mod1"
home = os.path.expanduser("~")
accent_color="#00ffff"
terminal = "st"

# Colors for Waybar integration
colors = {
    "primary": accent_color,
    "secondary": "#ffffff",
    "background": "#000000",
}

keys = [
    ### BASIC KEYBINDINGS
    ## Qtile control
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "b", lazy.hide_show_bar(), desc="Hide/Show Qtile bar"),
    ## Apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.spawn("firefox"), desc="Web Browser"),
    Key([mod], "e", lazy.spawn("nautilus -w"), desc="File Manager"),
    Key([mod], "space",
            lazy.widget["keyboardlayout"].next_keyboard(),
            desc="Change keyboard layout."
            ),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "a",
            lazy.spawn(home + "/.config/qtile/rofi/launcher.sh"),
            desc="rofi application launcher"
            ),
    Key([alt, "control"], "Escape",
            lazy.spawn("xkill"),
            desc="X Kill"
            ),
    Key([mod], "x",
            lazy.spawn("i3lock -f -e -c 000000"),
            desc="Lock screen"
            ),
    Key([], "Print",
            lazy.spawn(["bash", "-c",
            "/usr/bin/grim ~/Pictures/Screenshots/qtile/Screenshot_$(date +%Y-%m-%d_%H-%M-%S).png && "
            "swaync-client -s 'Screenshot saved' -b 'View' 'xdg-open ~/Pictures/Screenshots/qtile/'"
            ]),
             desc="Full screen screenshot"
             ),
    Key([], "XF86Calculator", lazy.spawn("qalculate"), desc="Qalculate! (Advanced calculator)"),
    ## Sound / Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+"), desc="increase volume by 5%"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-"), desc="decrease volume by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle"), desc="mute volume"),
    ## Screen Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -d 'intel_backlight' s +5%"),
        desc="increase screen brightness by 5%"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -d 'intel_backlight' s 5%-"),
        desc="decrease scr brightness by 5%"),
    
    ### Window control
    ## Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(), desc="Move window focus to next window"),
    Key([alt, "shift"], "Tab", lazy.layout.previous(), desc="Move window focus to previous window"),
    ## Control focused window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([alt], "F4", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "m",
        lazy.window.toggle_maximize(),
        desc='toggle window max state'
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc="toggle fullscreen"
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc="toggle floating"
        ),

    ### Layout control
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle next layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle previous layout"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(),
            desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window up"),
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(),
            desc="Grow window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all windows size"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod, alt], "f", lazy.layout.flip(),
        desc="Flip the main pane in monad layouts"),
    Key([mod, alt], "Up",
        lazy.layout.section_up(),
        desc="Move Up a section in treetab layout"
        ),
    Key([mod, alt], "Down",
        lazy.layout.section_down(),
        desc="Move Down a section in treetab layout"
        ),

    ### Groups
    Key([mod], "Page_Up",
            lazy.screen.prev_group(),
            desc="switch to previous group or workspace"
            ),
    Key([mod], "Page_Down",
            lazy.screen.next_group(),
            desc="switch to next group or workspace"
            ),
    Key([mod], "Home",
            lazy.group['1'].toscreen(),
            desc="switch to first group or workspace"
            ),
    Key([mod], "End",
            lazy.group['7'].toscreen(),
            desc="switch to last group or workspace"
            ),
    Key([mod], "Escape",
            lazy.screen.toggle_group(),
            desc="Switch to last visited group"
            )
]

# === GROUPS (11 Workspaces) ===
groups = [
    Group("1"), Group("2"), Group("3"), Group("4"), Group("5"),
    Group("6"), Group("7"), Group("8"), Group("9"),
    Group("10"), Group("11"),
]

# Map keys safely: 1-9 use numbers, 10 uses 0, 11 uses minus
key_map = {
    "1": "1", "2": "2", "3": "3", "4": "4", "5": "5",
    "6": "6", "7": "7", "8": "8", "9": "9",
    "10": "0", "11": "minus"
}

for g in groups:
    key = key_map[g.name]
    keys.extend([
        Key([mod], key, lazy.group[g.name].toscreen(),
            desc=f"Switch to group {g.name}"),
        Key([mod, "shift"], key, lazy.window.togroup(g.name, switch_group=True),
            desc=f"Move to group {g.name}"),
    ])

# Add ScratchPad
groups.append(
    ScratchPad("scratchpad", [
        DropDown("bpytop", terminal + " -e bpytop", height=0.75, opacity=1, on_focus_lost_hide=True)
    ])
)

layouts = [
    layout.floating.Floating(border_focus=accent_color, border_normal="#ffffff", border_width=2),
    layout.MonadTall(border_focus=accent_color, border_normal="#00ffff", margin=4, border_width=2),
    layout.MonadWide(border_focus=accent_color, border_normal="#00ffff", margin=4, border_width=2),
    layout.MonadThreeCol(border_focus=accent_color, border_normal="#ffffff", margin=4, border_width=2),
    layout.Bsp(border_focus=accent_color, border_normal="#004444", border_width=2),
    layout.RatioTile(border_focus=accent_color, border_normal="#004444", border_width=2),
    layout.Tile(border_focus=accent_color, border_normal="#004444", border_width=2),
    layout.VerticalTile(border_focus=accent_color, border_normal="#004444", border_width=2),
    layout.Columns(border_focus=accent_color, border_normal="#004444", border_focus_stack=accent_color, border_normal_stack="#004444", border_width=2),
    layout.Stack(border_focus=accent_color, border_normal="#004444", border_width=2, num_stacks=2, autosplit=False),
    layout.Matrix(border_focus=accent_color, border_normal="#004444", border_width=2),
    layout.TreeTab(active_bg=accent_color, active_fg="#000000", panel_width=200, font="Awesome", fontsize=20, sections=["SECTION 1", "SECTION 2", "SECTION 3", "SECTION 4"], section_fontsize=22, previous_on_rm=True)
]

####### MOUSE CALLBACKS #######
def open_rofi():
    qtile.cmd_spawn(home + "/.config/qtile/rofi/launcher.sh")

def kill_active_window():
    qtile.cmd_simulate_keypress([mod], "q")

def switch_next_window():
    qtile.cmd_simulate_keypress([alt], "Tab")

def switch_previous_window():
    qtile.cmd_simulate_keypress([alt, "shift"], "Tab")

widget_defaults = dict(
    font="Awesome",
    fontsize=22,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        ## Top Bar - DISABLED (using Waybar instead)
        # top=bar.Bar(
        #     [
        #         widget.Image(
        #             filename = "~/.config/qtile/icons/python.png",
        #             mouse_callbacks = {"Button1": open_rofi}
        #         ),
        #         widget.GroupBox(disable_drag=True, spacing = 5, highlight_method="block",
        #             this_current_screen_border=accent_color, block_highlight_text_color="#000000",
        #             active=accent_color, inactive="#00ffff", urgent_alert_method="block", urgent_text="#ff0000"),
        #         widget.TextBox(text=" "),
        #         widget.Prompt(foreground=accent_color, font="Source Code Pro Semibold"),
        #         widget.Spacer(),
        #         widget.TextBox(text=" "),
        #         widget.KeyboardLayout(configured_keyboards=["us","ar"]),
        #         widget.TextBox(text=" "),
        #         widget.Volume(volume_app="pavucontrol", step=3, foreground=accent_color, fmt="🎧{}"),
        #         widget.TextBox(text="🕒"),
        #         widget.Clock(format="%a %d %b - %I:%M:%S %p", foreground=accent_color),
        #         widget.CurrentLayout(foreground=accent_color),
        #     ],
        #     33,
        #     background='#000000',
        # ),
        ## Bottom Bar (optional)
        #bottom=bar.Bar([widget.WindowTabs()], 24),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules: list = []
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(border_focus=accent_color, border_normal="#ffffff", border_width=2, float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='ssh-askpass'),
    Match(title='branchdialog'),
    Match(title='pinentry'),
    Match(title='OGL'),
    Match(title='Qalculate!'),
    Match(wm_class='vncviewer'),
    Match(wm_class='xterm'),
    Match(wm_class='feh')
])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

@hook.subscribe.startup_once
def autostart():
    subprocess.run([home + "/.config/qtile/scripts/autostart.sh"])
    subprocess.run([home + "/.config/qtile/scripts/screen-saver.sh"])

# === Waybar Integration: Workspace Tracker ===
@hook.subscribe.focus_change
@hook.subscribe.client_killed
@hook.subscribe.client_managed
def update_groups_waybar(*_args):
    try:
        # Get current group name (works on all Qtile versions)
        try:
            current = qtile.current_screen.group.name
        except:
            current = qtile.current_screen.group.label
        
        # Build workspace status
        text = ""
        for g in qtile.groups:
            name = g.name
            if name == "scratchpad":
                continue
            # Check if group has windows (universal method)
            has_windows = len(g.windows) > 0
            if name == current:
                text += f'<span fgcolor=\'{colors["background"]}\' bgcolor=\'{colors["primary"]}\' line_height=\'2\'> {name} </span>'
            elif has_windows:
                text += f'<span fgcolor=\'{colors["primary"]}\'> {name} </span>'
            else:
                text += f'<span fgcolor=\'{colors["secondary"]}\'> {name} </span>'
        
        # Write to file
        with open("/tmp/qtile-groups.txt", "w", encoding="utf-8") as f:
            f.write(text)
        
        # Signal Waybar
        import subprocess
        subprocess.call(["pkill", "-RTMIN+8", "waybar"])
    except Exception:
        pass

wmname = "QTILE"
