import mysql.connector
conn = mysql.connector.connect(host="192.168.125.2",
                               user="FN-2199", password="1_h473_7R@i70Rs",
                               database="stormtroopers")
cursor = conn.cursor()
# Opérations à réaliser sur la base ...
conn.close()
