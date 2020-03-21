import os
print(os.getcwd())

my_walk=os.walk(r"C:\Users\Nat\Desktop\Linux")
for root, dirs, files in my_walk:
    print(root)
    print(dirs)
    print(files)