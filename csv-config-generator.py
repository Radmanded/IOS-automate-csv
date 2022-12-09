import csv
from netmiko import ConnectHandler

# Open the csv file and read in the data
with open('switch_data.csv', 'r') as csv_file:
csv_reader = csv.reader(csv_file)

# skip the header row
next(csv_reader)

# iterate through each row in the csv
for row in csv_reader:
    # assign the values to variables
    ip_address = row[0]
    interface_description = row[1]
     = row[2]
    
    
    # create a dictionary for the netmiko device parameters
    device = {
        'device_type': 'cisco_ios_xe',
        'ip': ip_address,
        'username': username,
        'password': password
    }
    
    # connect to the switch using netmiko
    net_connect = ConnectHandler(**device)
    
    # create the command to configure the interface description
    command = f'interface {interface}\ndescription {description}'
    
    # send the command to the switch
    output = net_connect.send_command(command)
    
    # print the output for confirmation
    print(output)
    
    # disconnect from the switch
    net_connect.disconnect()
