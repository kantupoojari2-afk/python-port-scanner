# Python Port Scanner
# A simple TCP port scanner for learning about sockets and networking.
# Use ONLY on your own machine or systems you have permission to test.

import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


def scan_port(host, port, timeout=0.5):
    """Try to connect to one port. Return the port number if open, else None."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((host, port)) == 0:   # 0 means the connection worked
                return port
    except OSError:
        pass
    return None


def get_service(port):
    """Look up the common service name for a port (e.g. 80 -> http)."""
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"


def main():
    print("=" * 50)
    print("          PYTHON PORT SCANNER")
    print("  Scan only systems you own or have permission to test")
    print("=" * 50)

    # --- Get input from the user ---
    target = input("Target host (press Enter for 127.0.0.1): ").strip() or "127.0.0.1"

    try:
        start_port = int(input("Start port (default 1): ") or 1)
        end_port = int(input("End port (default 1024): ") or 1024)
    except ValueError:
        print("Please enter valid numbers for the ports.")
        sys.exit(1)

    if not (1 <= start_port <= end_port <= 65535):
        print("Ports must be between 1 and 65535, and start must be <= end.")
        sys.exit(1)

    # --- Resolve the hostname to an IP address ---
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Could not resolve that host.")
        sys.exit(1)

    print(f"\nScanning {target} ({ip}) ports {start_port}-{end_port}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # --- Scan all ports using 100 threads at once (much faster) ---
    ports = range(start_port, end_port + 1)
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(ip, p), ports)

    open_ports = [p for p in results if p is not None]

    # --- Show results ---
    if open_ports:
        print(f"{'PORT':<10}{'STATE':<10}SERVICE")
        for p in open_ports:
            print(f"{p:<10}{'open':<10}{get_service(p)}")
    else:
        print("No open ports found in that range.")

    print(f"\nScan finished. {len(open_ports)} open port(s) found.")


if __name__ == "__main__":
    main()