# Qtile GruvBox

<img src="https://github.com/BaGutti/dotfiles/blob/qtile-gruvbox/source/2023-07-22_19-45.png">

## How to install
install dependencies, e.g on Arch
```bash
paru -S rofi-wifi-menu rofi-polkit-agent-git qtile firefox rofi playerctl brightnessctl pavucontrol \
lxappearance network-manager-applet flameshot dunst nitrogen picom neofetch
```
Dependencies for gaming (Optional)
```bash
sudo pacman -S --needed wine-staging giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls \
mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error \
lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo \
sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama \
ncurses lib32-ncurses ocl-icd lib32-ocl-icd libxslt lib32-libxslt libva lib32-libva gtk3 \
lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader lutris discord discord-screenaudio heroic-games-launcher-bin protonup-qt 
```
Dependencies for screen config (In GUI)
```bash
paru -S arandr 
```
Installing the config:
```bash
cp -r dotfiles/config/* ~/.config/
```
Make the necessary changes in `.config/qtile/config.py`

### This is not the final state of the dotfiles. I will be updating the branch with the dotfiles!
