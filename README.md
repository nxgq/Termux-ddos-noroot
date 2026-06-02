# DDoS Tool v2.1

## Description

This is a simple Distributed Denial of Service (DDoS) tool written in Python. It sends a large number of HTTP GET requests to a specified target to overwhelm the server and potentially cause it to crash or become unresponsive.

## Features

- Sends a configurable number of threads to the target.
- Supports both IP addresses and domain names as targets.
- Monitors the target's status and displays uptime, downtime, latency, and health.
- Can send requests with random user agents to mimic different browsers.

## Requirements

- Python 3.x

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies (if any).
3. please update the config by nano ddos.tool.py 
4. Run the script with Python:


best Settings
thread: 1000 max ( if your using termux) and over 10k If your pc good.

# The DDoS Tool does not require any external libraries and uses only built-in Python modules.
# Therefore, the requirements.txt file is empty.

# Built-in modules used in the script:
# - os
# - subprocess
# - time
# - socket
# - threading
# - signal
# - re

# No additional packages need to be installed.

```bash
git clone https://github.com/nxgq/Termux-ddos-noroot.git
cd Termux-ddos-noroot
nano ddos_tool.py
python ddos_tool.py
```
dev:alone 
