from netmiko import ConnectHandler

# establishing connection by creating a connection handler object
device = {
    "device_type": "cisco_ios",
    "ip": "device_ip",
    "username": "username",
    "password": "password"
}

connection = ConnectHandler(**device)

# sending a command and getting its output
output = connection.send_command("show interfaces")
print(output)

# declaring the configuration in variable and posting the changes via send_config_set method
config_commands = ["int g0/0", "des This is a test interface"]
output = connection.send_config_set(config_commands)

# closing the connection
connection.disconnect()