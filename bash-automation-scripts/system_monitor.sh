#!/bin/bash
echo "System Monitor - top 5 processes by memory"
ps aux --sort=-%mem | head -n 6
