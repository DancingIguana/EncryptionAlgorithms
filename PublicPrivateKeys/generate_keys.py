import rsa
import sys
import os

assert(len(sys.argv) == 2 or len(sys.argv) == 3), "Run the command with at least specifying the user_name"

user_name = sys.argv[1]
n_bits = 1024
if len(sys.argv) == 3: n_bits = int(sys.argv[2])



if not os.path.exists(f"./keys/{user_name}"):
    os.mkdir(f"./keys/{user_name}")


public_key, private_key = rsa.newkeys(n_bits)


with open(f"./keys/{user_name}/public.pem","wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open(f"./keys/{user_name}/public.txt","wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open(f"./keys/{user_name}/private.pem","wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

with open(f"./keys/{user_name}/private.txt","wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

print(f"Generated keys successfully under directory ./keys/{user_name}/")