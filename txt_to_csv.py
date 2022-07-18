import pandas as pd

df1 = pd.read_csv("/ansible_dir/pre_patch_output_files/2022-06-30_16H-49M-01S_pre_patch.txt")
df1.to_csv("/ansible_dir/playbooks/csv_output.csv", index=None)
 
