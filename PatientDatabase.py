import sqlite3
conn = sqlite3.connect('PatientDatabase.db')
c = conn.cursor()
sqlite_query = '''CREATE TABLE patient_table(Patient_code INTEGER PRIMARY KEY ,
                 Patient_name TEXT NOT NULL,
                 Patient_address TEXT NOT NULL,
                 Patient_Phone_number INTEGER NOT NULL )'''
c.execute(sqlite_query)
print("Executed Successfully")
insert_query = '''INSERT INTO patient_table
                         (Patient_code, Patient_name, Patient_address,  Patient_Phone_number) VALUES
                         (002, 'Honey', 'Gurudwara Nagar, Pune', 7896541230),
                         (009, 'Money', 'Ajanta hill, Aurangabad', 7412589630),
                         (007, 'Kaif', 'Swargate, Pune', 3698521470),
                         (005, 'vibhu', 'Baner, Pune', 4563217980),
                         (004, 'Piyush', 'Akurdi Railway Station, Pune', 357418920)'''
c.execute(insert_query)
conn.commit()
print('Data of the Patient table are:')
c.execute(''' SELECT rowid,* FROM patient_table ''')
items = c.fetchall()
for item in items:
    print(item)
conn.close()
