import sqlite3

conn = sqlite3.connect('DAC.db')
c = conn.cursor()
c.execute("CREATE TABLE DAC (Tarifa, Anio, Mes, Region, Cargo fijo, Verano, Invierno, Minimo)")

conn.commit()
conn.close()