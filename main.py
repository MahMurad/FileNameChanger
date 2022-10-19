import os

os.chdir(' \\directory\\')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    if 'OPT' in f_name:
        f_name = f_name.replace(" OPT","")
    print(f)
    f_name=f_name+".pdf"
    os.rename(f, f_name)
