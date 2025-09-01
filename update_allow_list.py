# update_allow_list.py
# Script that updates allow_list.txt by removing IPs from remove_list.txt

# Nom du fichier principal
import_file = "allow_list.txt"

# Lire le fichier de départ
with open(import_file, "r") as file:
    ip_addresses = file.read().split()

# Liste des IPs à retirer
with open("remove_list.txt", "r") as file:
    remove_list = file.read().split()

# Supprimer les IPs qui doivent être retirées
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Réécrire la nouvelle liste dans allow_list.txt
with open(import_file, "w") as file:
    file.write("\n".join(ip_addresses))

print("✅ allow_list.txt has been updated!")
