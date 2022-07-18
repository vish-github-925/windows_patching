import sys

pre_services_arg = sys.argv[1]
post_services_arg = sys.argv[2]

with open(pre_services_arg, "r") as pre_file:
    pre_services_str = pre_file.read()
with open(post_services_arg, "r") as post_file:
    post_services_str = post_file.read()

pre_services_str = pre_services_str[1:-2].replace("'","")
pre_services_list = pre_services_str.split(", ")

post_services_str = post_services_str[1:-2].replace("'","")
post_services_list = post_services_str.split(", ") 

pre_services_list_count = len(pre_services_list)
post_services_list_count = len(post_services_list)


missed_services_in_pre = []
missed_services_in_post = []

for i in range(pre_services_list_count):
    if pre_services_list[i] in post_services_list:
        continue
    else:
      missed_services_in_post.append(pre_services_list[i])

for i in range(post_services_list_count):
    if post_services_list[i] in pre_services_list:
        continue
    else:
        missed_services_in_pre.append(post_services_list[i])
print(pre_services_list_count)
print(missed_services_in_pre)
print(missed_services_in_post)
