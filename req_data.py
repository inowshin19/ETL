
import xml.etree.ElementTree as ET
import xml.dom.minidom
import psycopg2

## You can automatically retrieve the data from gICS if you have access to remote desktop by DIZ
# (which is authorized to access gICS data directly).
# As I don't have access to the data right now, I am parsing ID.xml as the ID's are stored in this file

mytree = ET.parse('ID.xml')
myroot = mytree.getroot()

ID = []

        ### Getting ID's of Patients

for type_tag in myroot.findall('{http://hl7.org/fhir}parameter'):
    for i in type_tag.findall('{http://hl7.org/fhir}valueIdentifier/{http://hl7.org/fhir}value'):

        for l, m in i.items():

            ID.append(m)


# This step is automating the process of merging all the ID's collected from gICS so that it can retrieve data related to all ID's

data = "<Parameters xmlns=\"http://hl7.org/fhir\">\n"
for i in range(0, len(ID)):
    s1 = '<parameter>\n        <name value=\"personIdentifier\" />\n        <valueIdentifier>\n            <system value=\"https://ths-greifswald.de/fhir/gics/identifiers/MPI\" />\n            <value value=\"'
    s2 = ID[i]
    s3 = '\" />\n        </valueIdentifier>\n    </parameter>\n        '
    s4 = ''.join([s1,s2,s3])
    data += s4
data += "</Parameters>"

# This print statement is not necessary but you can see that the variable 'data' contains
# the statement that is required to retrieve data of all the patients

print(data)