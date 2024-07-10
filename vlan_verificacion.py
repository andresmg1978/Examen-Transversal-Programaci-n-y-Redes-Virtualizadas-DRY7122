# vlan_verificacion.py
vlan_id = int(input("Ingrese el número de VLAN: "))

if 1 <= vlan_id <= 1005:
    print(f"La VLAN {vlan_id} está en el rango normal.")
elif 1006 <= vlan_id <= 4094:
    print(f"La VLAN {vlan_id} está en el rango extendido.")
else:
    print(f"La VLAN {vlan_id} no está en un rango válido.")
