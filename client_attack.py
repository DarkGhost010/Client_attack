import paramiko

def malware_command(ip,port,user,passwd,cmd):
    target = paramiko.SSHClient()
    target.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    target.connect(ip, port=port, username=user,password=passwd)

    _, stdout, stderr = target.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print("----The result-----")
        for line in output:
            print(line.strip())

if __name__ == "__main__":
    import getpass
    user = input("Please enter your target's username: ")
    password = input("Please enter the target's password: ")


    ip= input("Please enter your target's  IP address: ")
    port = input("Please specify the port: ")
    cmd = input("Please enter the command: ")
    malware_command(ip,port,user,password,cmd)
