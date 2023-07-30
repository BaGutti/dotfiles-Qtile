#! /bin/bash 

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#(sleep 2; run $HOME/.config/polybar/launch.sh) &

#/usr/lib/polkit-1/polkit-agent-helper-1 &	# Graphical authentication agent
#usr/lib/xfce-polkit/xfce-polkit &
rofi-polkit-agent &
libinput-gestures-setup start &
