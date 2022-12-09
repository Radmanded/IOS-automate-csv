# IOS-automate-csv


Configure Cisco switch interface name and description from a csv file.

1. Create a function to extract Switch IP Address, Phone Description, and Switch Port # from .csv name olivercer.csv.
2. SSH into switch using the Switch IP Address and username: admin, and password: Cisco12345
3. In the switch enter all the interfaces defined in the .csv and configure the interface description using the Phone Description in .csv
4. Verify the interface was configured correctly and ask user to continue.
5. If yes, save config with wr command
6. Run the show running config command 
7. Repeat on the next Switch IP Address in the csv.




from csv import reader
from pprint import pprint
import paramiko
import time

conf_dict = {}
with open("olivecer.csv", "r") as csv_file:
 csv_content = reader(csv_file)
 for device in csv_content:
  if not device[0]:
   continue
  if device[0] not in conf_dict.keys():
   conf_dict[device[0]] = []
  n = len(device)
  for conf in range(1,n):
   if not device[conf]:
    continue
   conf_dict[device[0]].append(device[conf])

session = paramiko.SSHClient()
session.load_system_host_keys()

for ip in conf_dict.keys():
 try:
  print(f"\n{'#' * 50}\nConnecting to the Device {ip}\n{'#' * 50} ")
  session.connect(hostname=ip,
      username='admin',
      password='Cisco12345',
      )
  DEVICE_ACCESS = session.invoke_shell()
  print(f"\nExecuting Commands are\n{'~'*22}\n{conf_dict[ip]}")
  for conf in conf_dict[ip]:
   DEVICE_ACCESS.send(conf+'\n')
   time.sleep(1)
   output = DEVICE_ACCESS.recv(65000)
   print (output.decode('ascii'),end='')
   time.sleep(.5)
  session.close()
 except :
  print('Can not connect to the device')

print (f"\n{'#' * 50}\nCOMMAND EXECUTION COMPLETED\n{'#' * 50}\n")
