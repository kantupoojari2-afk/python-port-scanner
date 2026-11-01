# Python Port Scanner

A simple multithreaded TCP port scanner written in Python, built to learn about sockets and networking.

## Features
- Scans a custom range of ports
- Multithreaded for speed
- Shows the common service name for each open port
- Input validation

## Usage
```bash
python scanner.py
```
Enter a target host and a port range when prompted. Press Enter to use the defaults (127.0.0.1, ports 1-1024).

## Example output
```
PORT      STATE     SERVICE
135       open      epmap
445       open      microsoft-ds
```

## Disclaimer
For educational use only. Scan only systems you own or have explicit permission to test.

## What I learned
- How TCP sockets work in Python
- Using threads to speed up network tasks
- Basics of ports and services
