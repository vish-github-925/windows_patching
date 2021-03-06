import pandas as pd
import sys

day_sheet = sys.argv[1]
sheet = pd.read_excel("/ansible_dir/playbooks/dummy_data.xlsx", day_sheet)
sheet.dropna()
critical_servers_ini = "[critical_servers]\n"
non_critical_servers_ini = "[non_critical_servers]\n"
reboot_servers_ini = "[reboot_servers]\n"
power_off_servers_ini = "[power_off_servers]\n"
workgroup_servers_ini = "[workgroup_servers]\n"
azure_servers_ini = "[azure_servers]\n"
vmware_servers_ini = "[vmware_servers]\n"

for i in sheet.index:
    ip_address = sheet['IP Details'][i]
    if sheet['Snapshot (Yes/No)'][i] == "Yes":
        critical_servers_ini = critical_servers_ini + str(ip_address) + "\n"
        if sheet['DataCenter'][i] == "Azure":
            azure_servers_ini = azure_servers_ini + str(ip_address) + "\n"
        else:
            vmware_servers_ini = vmware_servers_ini + str(ip_address) + "\n"
    else:
       non_critical_servers_ini = non_critical_servers_ini + str(ip_address) + "\n"
    if sheet['power off/reboot'][i] == "power off":
        power_off_servers_ini = power_off_servers_ini + str(ip_address) + "\n"
    else:
        reboot_servers_ini = reboot_servers_ini + str(ip_address) + "\n"
    if sheet['workgroup/domain'][i] == "workgroup":
        workgroup_servers_ini = workgroup_servers_ini + str(ip_address) + "\n"



<<<<<<< HEAD
total_ini_file = critical_servers_ini + "\n" + non_critical_servers_ini + "\n" + reboot_servers_ini + "\n" + power_off_servers_ini + "\n" + workgroup_servers_ini + "\n"
with open(f"/ansible_dir/playbooks/{day_sheet}_inventory.ini", "w", encoding="utf-8") as file:
=======

total_ini_file = critical_servers_ini + "\n" + non_critical_servers_ini + "\n" + reboot_servers_ini + "\n" + power_off_servers_ini + "\n" + workgroup_servers_ini + "\n" + azure_servers_ini + "\n" + vmware_servers_ini 
with open(f"C:\\Users\\user\\Desktop\\oneNeuron\\python_lecture\\python_excel_test\\github_windows_patching_scripts\\{day_sheet}_inventory.ini", "w", encoding="utf-8") as file:
>>>>>>> 646c5f726f2f900d570aebbcc26944554c5bf4a5
    file.write(total_ini_file+"\n")
    # file.write(critical_servers_ini+"\n")
    # file.write(non_critical_servers_ini+"\n")
    # file.write(reboot_servers_ini+"\n")
    # file.write(power_off_servers_ini+"\n")
    # file.write(workgroup_servers_ini+"\n")

