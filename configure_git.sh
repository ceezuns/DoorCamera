#!/bin/bash

echo "1) Personal"

echo "	ceezuns@gmail.com"

echo ""

echo "2) GitHub Provided"
echo "	49824660+ceezuns@users.noreply.github.com"

echo ""

echo "3) Personal (Old)"
echo "	ceezuns@gmail.com, 305E279D82819B20"

echo ""

echo "4) GitHub Provided (Old)"
echo "	49824660+ceezuns@users.noreply.github.com, 15C9630ACADE5855"

echo ""

echo "Choose A Profile: "

read profile

if [ $profile == "1" ]; then
	git config user.email "ceezuns@gmail.com"
	git config user.signingkey "C9F91AC919133806E41B56EC621053372EF1BCE6"
elif [ $profile == "2" ]; then
	git config user.email "49824660+ceezuns@users.noreply.github.com"
	git config user.signingkey "F5DDC126B9FEDDE104844652841182B2C4583BE8"
elif [ $profile == "3" ]; then
	echo "WARNING: Old Key Being Used!"
	git config user.email "ceezuns@gmail.com"
	git config user.signingkey "305E279D82819B20"
elif [ $profile == "4" ]; then
	echo "WARNING: Old Key Being Used!"
	git config user.email "49824660+ceezuns@users.noreply.github.com"
	git config user.signingkey "15C9630ACADE5855"
else
	echo "An Error Occurred, Please Relaunch The Script"
fi
