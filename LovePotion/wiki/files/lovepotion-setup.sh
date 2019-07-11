#!/bin/bash
## Version 1.0.2

## Something something write perms
if [[ ! -w /etc/profile.d ]]; then
  echo "Please run this as root"
  exit 1
fi

## Check if .lovepotion folder exists in $HOME
if [[ ! -d $HOME/.lovepotion ]]; then
  echo -n "Creating Löve Potion folder in ${HOME}.. "
  mkdir $HOME/.lovepotion
  echo "Done!"
fi

## Create environment variables in /etc/profile.d
## Also gg apex for forgetting > was write, not append :)
ENV_FILE="/etc/profile.d/lovepotion-env.sh"
if [[ ! -f $ENV_FILE ]]; then
  echo -n "Creating Löve Potion environment variables.. "
  touch $ENV_FILE 
  echo "#!/usr/bin/bash" > $ENV_FILE
  echo "export LOVEPOTION_3DS=$HOME/.lovepotion/3ds.elf" >> $ENV_FILE 
  echo "export LOVEPOTION_SWITCH=$HOME/.lovepotion/switch.elf" >> $ENV_FILE
  echo "Done!"
fi

echo ""

echo "Setup complete."
echo "If you need to build Love Potion games right away"
echo "run 'source /etc/profile.d/lovepotion-env.sh' in your terminal."
echo "Remember to download the latest elf files from GitHub"
echo "and place them inside ~/.lovepotion as '3ds.elf' and 'switch.elf'"
