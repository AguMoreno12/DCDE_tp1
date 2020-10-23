import pymysql
########################################################
# Conectar con base de datos
conexion = pymysql.connect(host="basedatos", 
                           user="root", 
                           passwd="admin", 
                           database="bdPruebaTp")
cursor = conexion.cursor()
print('Conexión establecida con la DB!!!')
print('################')
########################################################
# Realizar las 5 querys
#1-> Header de columnas
cursor.execute("SELECT * FROM beacons")
header = []
header = list(cursor.description)
print('Query #1 -> Header de la tabla: ')
print(header[0][0],header[1][0],header[2][0],header[3][0],header[4][0],header[5][0])
#2-> Ultimos 10 datos cargados
cursor.execute("SELECT * FROM beacons ORDER by DateTime DESC LIMIT 10")
rows =cursor.fetchall()
print('\n','Query #2 -> Ultimos 10 registros:', rows,'\n')
#3-> Cantidad y valores con distancia A = 0
cursor.execute('SELECT * FROM beacons WHERE DistanceA=%s', 0)
rows =cursor.fetchall()
print('Query #3 -> Total de lecturas DistanceA = 0 -->', len(rows),'\n','Detalle:', rows,'\n')
#4-> Beacon permaneciendo en la pos Px=165 
cursor.execute("SELECT * FROM beacons WHERE (PositionX=%s)",165)    
rows =cursor.fetchall()
print('Query #4 -> Persistencia en PX=165 -->', cursor.rowcount,'\n','Detalle:', rows,'\n')
#5-> Devuelvo las máximas distancias para los gateways A B C en un dict
maxim={}
cursor.execute("SELECT * FROM beacons ORDER by DistanceA DESC LIMIT 1")
rows = list(cursor.fetchall())
maxim['maxDa']= rows[0][0]
cursor.execute("SELECT * FROM beacons ORDER by DistanceB DESC LIMIT 1")
maxim['maxDb']= rows[0][0]
cursor.execute("SELECT * FROM beacons ORDER by DistanceC DESC LIMIT 1")
maxim['maxDc']= rows[0][0]

print('Query #5 -> Distancias máximas -->', maxim )

########################################################
# Finalizar 
cursor.close()
conexion.commit()
conexion.close()