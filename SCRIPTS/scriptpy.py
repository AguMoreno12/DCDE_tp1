########################################################
# Abrir el archivo csv
import pandas as pd
import pymysql
df=pd.read_csv('beacon.csv', skiprows=0, sep=',')
#print(df)
lis_fila= df.values.tolist()
for i in lis_fila:
    fa=float(i.pop(2))
    i.insert(2,fa)
print('CSV Leido!!')
########################################################
# Conectar con base de datos

conexion = pymysql.connect(host="basedatos", 
                           user="root", 
                           passwd="admin", 
                           database="bdPruebaTp")
cursor = conexion.cursor()
print('Conexión establecida!!!')
########################################################
# poblar la base de datos
for row in range(len(lis_fila)):
    print(row)
    cursor.execute("INSERT INTO beacons (DistanceA, DistanceB, DistanceC, PositionX, PositionY, DateTime) VALUES (%s, %s, %s,%s, %s, %s)",lis_fila[row])    
print('Filas Insertadas')
########################################################
# Finalizar 
cursor.close()
conexion.commit()
conexion.close()
print('Conexion close')