import mysql.connector
conn = mysql.connector.connect(host="192.168.125.2",
                               user="FN-2199", password="***************",
                               database="stormtroopers")
cursor = conn.cursor()
# Opérations à réaliser sur la base ...
conn.close()
