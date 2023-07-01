from ncclient import manager

with manager.connect(
    host="192.168.100.65",
    port=830,
    username="cisco",
    password="cisco123!"
) as m:
    
    print("Conexión exitosa")
