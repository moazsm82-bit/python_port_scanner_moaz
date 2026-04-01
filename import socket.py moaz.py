import socket
print("-" * 50)
print("Staring scanner...please wait.")
print("-" * 50)
hostname = socket.gethostname()
target_ip = socket.gethostbyname(hostname)
print(f"Scanning target IP:{target_ip}")
start_port = int(input("enter the start port: "))
end_port = int(input("enter the and port: "))
for port in range(start_port, end_port + 1):
    #print(f"Cheking port: {port}...")
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex(( target_ip,port))
    if result == 0:
        print(f"port {port} is OPEN!")
        s.close()
print("\nScan completed successfully!")s