import pandas as pd
import sys

day_sheet = sys.argv[1]
sheet = pd.read_excel("dummy_data.xlsx", day_sheet)

critical_servers_ini = "[critical_servers]\n"
non_critical_servers_ini = "[non_critical_servers]\n"
reboot_servers_ini = "[reboot_servers]\n"
power_off_servers_ini = "[power_off_servers]\n"
workgroup_servers_ini = "[workgroup_servers]\n"

for i in sheet.index:
    ip_address = sheet['ip address'][i]
    if sheet['snapshot'][i] == "yes":
        critical_servers_ini = critical_servers_ini + str(ip_address) + "\n"
    else:
       non_critical_servers_ini = non_critical_servers_ini + str(ip_address) + "\n"
    if sheet['power off/reboot'][i] == "power off":
        power_off_servers_ini = power_off_servers_ini + str(ip_address) + "\n"
    else:
        reboot_servers_ini = reboot_servers_ini + str(ip_address) + "\n"
    if sheet['workgroup/domain'][i] == "workgroup":
        workgroup_servers_ini = workgroup_servers_ini + str(ip_address) + "\n"


initial_items_ini = '''[all:vars]
ansible_user=vishnuvardhan
ansible_password=123456
ansible_connection=openssh
ansible_shell_type=cmd
'''

total_ini_file = initial_items_ini + "\n" + critical_servers_ini + "\n" + non_critical_servers_ini + "\n" + reboot_servers_ini + "\n" + power_off_servers_ini + "\n" + workgroup_servers_ini + "\n"
with open(f"{day_sheet}_inventory.ini", "w", encoding="utf-8") as file:
    file.write(total_ini_file+"\n")
    # file.write(critical_servers_ini+"\n")
    # file.write(non_critical_servers_ini+"\n")
    # file.write(reboot_servers_ini+"\n")
    # file.write(power_off_servers_ini+"\n")
    # file.write(workgroup_servers_ini+"\n")

