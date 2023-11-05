import xml
import xml.etree.ElementTree as ET
import xml.dom.minidom
import psycopg2

#Database Connection

conn = psycopg2.connect(database="postgres", user="postgres", password="", host="127.0.0.1", port="5432")
cur = conn.cursor()
print("Database Connected....")

# data.xml contains the data of the patients and their consent.
# As we don't need all the data, we will access the data that are important

mytree = ET.parse('data.xml')
myroot = mytree.getroot()




doc = xml.dom.minidom.parse("data.xml")


expertise = doc.getElementsByTagName("id")
lastupdated = doc.getElementsByTagName("lastUpdated")
patient = doc.getElementsByTagName("patient")

# Created Empty list for storing values

patient = []
m_value = []
m_status = []
vol = []
ide = []
last = []
start_date = []
end_date = []

   ### Patient ID extraction and preprocessing

for type_tag in myroot.findall('{http://hl7.org/fhir}entry'):
    for i in type_tag.findall('{http://hl7.org/fhir}resource/{http://hl7.org/fhir}Consent/{http://hl7.org/fhir}patient/{http://hl7.org/fhir}reference'):
        #print(i.attrib)
        for l, m in i.items():
            print(m)
            patient.append(m)
            #print(type(m))
            #print("{} {}\n".format(l, val))
print(patient)
patient2 = [str(i).removeprefix('Patient/') for i in patient]
print(patient2)

### Module Name/Value extraction and preprocessing

for type_tag in myroot.findall('{http://hl7.org/fhir}entry'):
    for i in type_tag.findall('{http://hl7.org/fhir}resource/{http://hl7.org/fhir}Consent/{http://hl7.org/fhir}policyRule/{http://hl7.org/fhir}coding/{http://hl7.org/fhir}code'):
        for a,b in i.items():

            m_value.append(b)

print(m_value)

### Module Status extraction and preprocessing

for type_tag in myroot.findall('{http://hl7.org/fhir}entry'):
    for i in type_tag.findall('{http://hl7.org/fhir}resource/{http://hl7.org/fhir}Consent/{http://hl7.org/fhir}provision/{http://hl7.org/fhir}type'):
        for a, b in i.items():
            m_status.append(b)
print(m_status)

### Start and End date extraction and preprocessing

for type_tag in myroot.findall('{http://hl7.org/fhir}entry'):
    for i in type_tag.findall('{http://hl7.org/fhir}resource/{http://hl7.org/fhir}Consent/{http://hl7.org/fhir}provision/{http://hl7.org/fhir}period/{http://hl7.org/fhir}start'):
        for a, b in i.items():
            start_date.append(b)
print(start_date)

for type_tag in myroot.findall('{http://hl7.org/fhir}entry'):
    for i in type_tag.findall('{http://hl7.org/fhir}resource/{http://hl7.org/fhir}Consent/{http://hl7.org/fhir}provision/{http://hl7.org/fhir}period/{http://hl7.org/fhir}end'):
        for a, b in i.items():
            end_date.append(b)
print(end_date)


    ### Inserting the values in table

for a, b, c, d, e in zip(patient2, m_value, m_status, start_date, end_date):
    #print(x, y, z)
    cur.execute('INSERT INTO etl (PatientID, ModuleName, ModuleStatus, ValidFrom, ValidTill) VALUES (%s, %s, %s, %s, %s)', (a, b, c, d, e))
    print('Inserted Succesfully')


conn.commit()
conn.close()

