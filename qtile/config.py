from typing import List  # noqa: F401
from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen#, Keychord
from libqtile.lazy import lazy
from libqtile.command import lazy
from libqtile.utils import guess_terminal

import os

# Colours for all document (IMPORTANT!!!!)
colour_one='e659a9'
colour_two='ffffff'
colour_three='66284B' #colores Rosa Original
colour_four='eaa1ca'
colour_bg='282a36'

#colour_one='00B3AF'
#colour_two='ffffff'
#colour_three='007F7D'
#colour_four='4DFFFC'
#colour_bg='282a36'

# fonsize for all document
font_size_b2=16
font_size=13
icon_size=40
group_box_size=20


# generate triangles for top bar
def geneate_triangle_one():
    return widget.TextBox(
        text='',
        padding=-6,
        fontsize=icon_size,
        foreground=colour_one,
        background=colour_two,
        margin_x=0,
        margin_y=-5,
    )


def geneate_triangle_two():
    return widget.TextBox(
        text='',
        padding=-6,
        fontsize=icon_size,
        foreground=colour_two,
        background=colour_one,
        margin_x=0,
        margin_y=-5,
    )
#-------------------------------------------------------------------------------------------------------------------------------------------------------
                            #basics
#-------------------------------------------------------------------------------------------------------------------------------------------------------
mod = "mod4"
terminal = "wezterm"
browser = "brave"
scrnsht = "spectacle"

keys = [
    # Switch between windows
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "b", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod], "Space", lazy.window.toggle_floating(),
        desc="Toggle between tiled and flotating"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    #-------------------------------------------------------------------------------------------------------------------------------------------------------
                    # keymaps for Apps
    #-------------------------------------------------------------------------------------------------------------------------------------------------------

    # keymap rofi menu
    Key([mod], "o", lazy.spawn("rofi -show drun -theme ~/.config/rofi/config.rasi"),desc="launch rofi app launcher"),

    # keymap xkill
    Key([mod], "F4", lazy.spawn("xkill"), desc="launch xkill"),

    # keymap min web browser
    Key([mod], "b", lazy.spawn(browser), desc="launch web browser"),

    # keymap Thunar
    Key([mod], "e", lazy.spawn("thunar"), desc="launch Thunar file manager"),

    # keymap scrot
    Key ([],"Print", lazy.spawn(scrnsht)),

    # keymap for fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    #-------------------------------------------------------------------------------------------------------------------------------------------------------
                    # multimedia Keys
    #-------------------------------------------------------------------------------------------------------------------------------------------------------
    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(" pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="lower volume "),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(" pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Raise volume "),
    # Mute/unmute
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mute the volume"),
    Key([], "XF86AudioStop", lazy.spawn("pactl set-source-mute @DEFAULT_SINK@ toggle"), desc="Mute the microphone"),
    # Play | Prev/next
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),



    # keymap layout for app launch (not use them!)
    Key([mod], "x", lazy.spawn("rofi -show power-menu -modi power-menu:rofi-power-menu"), desc="launch rofi power menu"),

    # keymap layout for app launch (not use them!)
    #Key([mod], "", lazy.spawn(""), desc="launch "),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]


groups = [Group(i) for i in [

    "  ","  ","  "," 󰓇 󰙯 ","  ","  ","  ","  ","  ",

    ]]

for i, group in enumerate(groups):
    numEsc = str(i+1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], numEsc, lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], numEsc, lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(group.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(
        border_focus=colour_one,
        border_normal=colour_three,
        border_width=5,
        margin=6,
        margin_on_single=15,
        border_on_single="true",
    ),
    layout.MonadWide(
        border_focus=colour_one,
        border_normal=colour_three,
        border_width=5,
        margin=6,
    ),
    layout.Max(
        border_focus=colour_one,
        border_normal=colour_three,
        border_with=5,
        margin=6,
    ),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=3),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),

    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),

]

widget_defaults = dict(
    font='Fira Code Nerd Font',
    fontsize=16,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.TextBox(
                    text='',
                    padding=10,
                    fontsize=group_box_size,
                    foreground=colour_one,
                    background=colour_two,
                ),
                widget.GroupBox(
                    active=colour_one,
                    inactive=colour_two,
                    borderwidth=1,
                    disable_drag=True,
                    fontsize=group_box_size,
                    highlight_method='line',
                    highlight_color=[colour_bg, colour_one],
                    margin_x=0,
                    margin_y=5,
                    other_screen_border=colour_four,
                    other_current_screen_border=colour_three,
                    padding_x=0,
                    padding_y=0,
                    block_highlight_text_color=colour_two,
                    this_current_screen_border=colour_one,
                    this_screen_border=colour_four,
                    urgent_alert_method='block',
                    urgent_border=colour_one,
                ),
                widget.Sep(
                    padding=10,
                    linewidth=3,
                    foreground=colour_one,
                ),
                widget.WindowName(
                    foreground=colour_two,
                    format='{name}',
        		    fontsize=16,
                    font='Roboto Slab',
                ),
                widget.TextBox(
	                text='',
	                padding=-6,
                    fontsize=icon_size,
                    foreground=colour_one,
                    margin_x=0,
                    margin_y=-5,
	            ),
                widget.TextBox(
                    text='Vol:',
                    font='Roboto Slab',
                    background=colour_one,
                    foreground=colour_two,
		            fontsize=font_size,
		        ),
                widget.PulseVolume(
                    font='Roboto Slab',
                    background=colour_one,
                    foreground=colour_two,
        		    fontsize=font_size,
                    update_interval=0.1,
                ),
                geneate_triangle_two(),
                widget.TextBox(
                    text='󰲝',
                    background=colour_two,
                    foreground=colour_one,
                    fontsize=font_size,
                ),
                widget.Net(
                    background=colour_two,
                    foreground=colour_one,
                    font='Roboto Slab',
                    fontsize=font_size,
                    format='{down} ↓↑ {up}',
                ),

                geneate_triangle_one(),
                widget.OpenWeather(
                    font='Roboto Slab',
                    app_key='4622c141c797366c3a7a1aa0de00c7b0',
                    foreground=colour_two,
                    background=colour_one,
                    fontsize=font_size,
                    location='Bogotá',
                    format='{icon} {location_city}: {main_temp} °{units_temperature} {weather_details}',
                    language='es',
                ),
                geneate_triangle_two(),
                widget.Memory(
                    font='Roboto Slab',
                    background=colour_two,
                    foreground=colour_one,
                    format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
		            fontsize=font_size,
                ),
                geneate_triangle_one(),
                widget.TextBox(
                    text='',
                    background=colour_one,
                    foreground=colour_two,
        		    fontsize=font_size,
                ),
                widget.Clock(
                    #format='%a %d de %b. %I:%M %p ',
                    format='%d/%m/%y %I:%M %P',
                    background=colour_one,
                    font='Roboto Slab',
                    fontsize=font_size,
                    foreground=colour_two
                ),
            ],
            24,
            background=colour_bg,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.TextBox(
                    text='',
                    padding=10,
                    fontsize=group_box_size,
                    foreground=colour_one,
                    background=colour_two,
                ),
                widget.GroupBox(
                    active=colour_one,
                    borderwidth=1,
                    disable_drag=True,
                    fontsize=group_box_size,
                    inactive=colour_two,
                    highlight_method='block',
                    margin_x=0,
                    margin_y=5,
                    other_screen_border=colour_four,
                    other_current_screen_border=colour_three,
                    padding_x=0,
                    padding_y=0,
                    block_highlight_text_color=colour_two,
                    this_current_screen_border=colour_one,
                    this_screen_border=colour_four,
                    urgent_alert_method='block',
                    urgent_border=colour_one,
                ),
                widget.Sep(
                    padding=10,
                    linewidth=3,
                    foreground=colour_one,
                ),
                widget.WindowName(
                    foreground=colour_two,
                    format='{name}',
        		    fontsize=16,
                    font='Roboto Slab',
                ),
                widget.TextBox(
	                text='',
	                padding=-6,
                    fontsize=icon_size,
                    foreground=colour_one,
                    margin_x=0,
                    margin_y=-5,
	            ),
                widget.Systray(
                    padding=10,
                    background=colour_one,
                    foreground=colour_two
                ),
                widget.TextBox(
                    text='Vol:',
                    font='Roboto Slab',
                    background=colour_one,
                    foreground=colour_two,
		            fontsize=font_size_b2,
		        ),
                widget.PulseVolume(
                    font='Roboto Slab',
                    background=colour_one,
                    foreground=colour_two,
        		    fontsize=font_size_b2,
                    update_interval=0.1,
                ),
                geneate_triangle_two(),
                widget.TextBox(
                    text='󰲝',
                    background=colour_two,
                    foreground=colour_one,
                    fontsize=font_size_b2,
                ),
                widget.Net(
                    background=colour_two,
                    foreground=colour_one,
                    font='Roboto Slab',
                    fontsize=font_size_b2,
                    format='{down} ↓↑ {up}',
                ),

                geneate_triangle_one(),
                widget.OpenWeather(
                    font='Roboto Slab',
                    app_key='4622c141c797366c3a7a1aa0de00c7b0',
                    foreground=colour_two,
                    background=colour_one,
                    fontsize=font_size_b2,
                    location='Bogotá',
                    format='{icon} {location_city}: {main_temp} °{units_temperature} {weather_details}',
                    language='es',
                ),
                geneate_triangle_two(),
                widget.Memory(
                    font='Roboto Slab',
                    background=colour_two,
                    foreground=colour_one,
                    format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
		            fontsize=font_size_b2,
                ),
                geneate_triangle_one(),
                widget.TextBox(
                    text='',
                    background=colour_one,
                    foreground=colour_two,
        		    fontsize=font_size_b2,
                ),
                widget.Clock(
                    #format='%a %d de %b. %I:%M %p ',
                    format='%d/%m/%y %I:%M %P',
                    background=colour_one,
                    font='Roboto Slab',
                    fontsize=font_size_b2,
                    foreground=colour_two
                ),
            ],
            24,
            background=colour_bg,
        ),
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
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    ],
    border_focus=colour_one,
    border_normal=colour_three,
    border_width=5,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"



##### STARTUP PROGRAMS #####

cmd=[
        "sh /home/exa/discos/d/linux-base/base-conf/autostart.sh",
        "picom &",
        "nm-applet &",
        "setxkbmap latam",
        "dunst &",
        "nitrogen --restore &",
    ]

for x in cmd:
    os.system(x)
