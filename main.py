# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    import xml
    import xml.etree.ElementTree as ET
    import xml.dom.minidom
    import psycopg2

    conn = psycopg2.connect(database="postgres", user="postgres", password="", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    print("Database Connected....")

    mytree = ET.parse('data.xml')
    myroot = mytree.getroot()
    print(myroot)
    print(myroot[5].tag)
    print(myroot[1].attrib)
    print(myroot[1].text)
    # for x in myroot.iter():
    #     print(x.tag, x.attrib, x.text)
    print(myroot[1].attrib)
    # for type_tag in myroot.findall('{http://hl7.org/fhir}entry'):
    #   value = type_tag.get('patient')
    #  print(value)
    doc = xml.dom.minidom.parse("data.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    expertise = doc.getElementsByTagName("id")
    lastupdated = doc.getElementsByTagName("lastUpdated")
    patient = doc.getElementsByTagName("patient")
    patient = []
    m_value = []
    m_status = []
    vol = []
    ide = []
    last = []
    start_date = []
    end_date = []
    # for e in myroot.iter('{http://hl7.org/fhir}display'):
    #   print(e)
    #  edu_rec = e.attrib
    # print(edu_rec)

    ### Patient ID extraction and preprocessing

    for type_tag in myroot.findall('{http://hl7.org/fhir}entry'):
        for i in type_tag.findall(
                '{http://hl7.org/fhir}resource/{http://hl7.org/fhir}Consent/{http://hl7.org/fhir}patient/{http://hl7.org/fhir}reference'):
            # print(i.attrib)
            for l, m in i.items():
                print(m)
                patient.append(m)
                # print(type(m))
                # print("{} {}\n".format(l, val))
    print(patient)
    patient2 = [str(i).removeprefix('Patient/') for i in patient]
    print(patient2)

    ### Module Name/Value extraction and preprocessing

    for type_tag in myroot.findall('{http://hl7.org/fhir}entry'):
        for i in type_tag.findall(
                '{http://hl7.org/fhir}resource/{http://hl7.org/fhir}Consent/{http://hl7.org/fhir}policyRule/{http://hl7.org/fhir}coding/{http://hl7.org/fhir}code'):
            for a, b in i.items():
                m_value.append(b)

    print(m_value)

    # patient.append(list((i.attrib).values()))
    # print(list())
    # print(patient)
    # p = ' '.join(patient)
    # print(p)

    ### Module Status extraction and preprocessing

    for type_tag in myroot.findall('{http://hl7.org/fhir}entry'):
        for i in type_tag.findall(
                '{http://hl7.org/fhir}resource/{http://hl7.org/fhir}Consent/{http://hl7.org/fhir}provision/{http://hl7.org/fhir}type'):
            for a, b in i.items():
                m_status.append(b)
    print(m_status)

    for type_tag in myroot.findall('{http://hl7.org/fhir}entry'):
        for i in type_tag.findall(
                '{http://hl7.org/fhir}resource/{http://hl7.org/fhir}Consent/{http://hl7.org/fhir}provision/{http://hl7.org/fhir}period/{http://hl7.org/fhir}start'):
            for a, b in i.items():
                start_date.append(b)
    print(start_date)

    for type_tag in myroot.findall('{http://hl7.org/fhir}entry'):
        for i in type_tag.findall(
                '{http://hl7.org/fhir}resource/{http://hl7.org/fhir}Consent/{http://hl7.org/fhir}provision/{http://hl7.org/fhir}period/{http://hl7.org/fhir}end'):
            for a, b in i.items():
                end_date.append(b)
    print(end_date)

    for i, j in zip(expertise, lastupdated):
        id = (i.getAttribute("value"))
        ide.append(id)
        lu = (j.getAttribute("value"))
        last.append(lu)

        # for k in range(0,):
        #   cur.execute('INSERT INTO test (id, sname, roll_num) VALUES (%s, %s, %s)', (k, lu, j))
        #  print('hfhf')
        # pa = (k.getElementsByTagName("display"))
        # pat = (k.getAttribute("value"))
    # print(ide, last)
    # list3 = patient + ide + last
    # print(list3)
    num = []
    l = len(ide)
    for k in range(127, 127, 1):
        num.append(k)
    print(num)
    # print(type(p))

    ### Inserting the values in table

    for a, b, c, d, e in zip(patient2, m_value, m_status, start_date, end_date):
        # print(x, y, z)
        cur.execute(
            'INSERT INTO etl (PatientID, ModuleName, ModuleStatus, ValidFrom, ValidTill) VALUES (%s, %s, %s, %s, %s)',
            (a, b, c, d, e))
        print('Inserted Succesfully')

    # cur.commit()
    # for i in myroot.findall("{http://hl7.org/fhir}Bundle"):
    #   print(i)
    #  p = i.find("id").text
    # print(p)
    # for x in child.iter():
    #   print(x.tag)
    #  print(x.attrib)
    # print(x.text)

    # cur.execute("CREATE TABLE test(id serial PRIMARY KEY, sname CHAR(50), roll_num integer);")
    # print("Table Created....")

    conn.commit()
    conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
