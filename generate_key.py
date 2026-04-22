import random
import string

new_key = "Hydra_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

with open("key.txt", "w") as f:
    f.write(new_key)

print(f"New key generated: {new_key}")
