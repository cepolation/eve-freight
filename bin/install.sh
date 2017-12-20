#!/bin/bash
echo "### EVE FREIGHT INSTALLATION ###"
echo "Installing dependencies..."
apt-get install python3
apt-get install python3-pip
pip3 install -r ./requirements.txt
echo "Complete"
