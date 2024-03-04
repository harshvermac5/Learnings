import paramiko

# establishing SSH Connection
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname="remote_host", username="username", password="password")

# executing commands
stdin, stdout, stderr = ssh_client.exec_command("ls -l")
print(stdout.read().decode())

# file transfer using FTP
sftp = ssh_client.open_sftp()
# uploading file
sftp.put(localpath="", remotepath="")
# downloading file
sftp.get(remotepath="", localpath="")
sftp.close()

# closing connection
ssh_client.close()