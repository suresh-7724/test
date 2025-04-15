#!/bin/bash
echo "Updating package list..."
sudo apt-get update

echo "Upgrading packages..."
sudo apt-get upgrade -y

echo "Cleaning up cache..."
sudo apt-get clean

echo "Removing unnecessary packages..."
sudo apt-get autoremove -y

echo "System packages updated and cleaned up."
