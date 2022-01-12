import paramiko

def ssh_command(ip,port,user,passwd,cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user,password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print("----output-----")
        for line in output:
            print(line.strip())

if __name__ == "__main__":
    import getpass
    user = input("Please enter the username: ")
    password = input("Please enter the victim's password: ")


    ip= input("Please enter the IP address: ")
    port = input("Please specify the port: ")
    cmd = input("PLease enter the command: ")
    ssh_command(ip,port,user,password,cmd)