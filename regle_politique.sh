#!/bin/bash

cible_input = "$1"
cible_output = "$2"
cible_forward = "$3"

sudo iptables -A INPUT -j "$cible_input"
sudo iptables -A OUTPUT -j "$cible_output"
sudo iptables -A FORWARD -j "$cible_forward"