#!/usr/bin/python
import mysql.connector
# Connect to the database
import xml.etree.cElementTree as ET
conn = mysql.connector.connect(user='root',password='159357123'
						,host='localhost'
						,port='3306'
						,database='van_operator')

cursor = conn.cursor()
cursor.execute("select id,name , tel ,location from operator")
operator = cursor.fetchall()

cursor.execute("select opro.id,op_id,source,destination,distance,price from opro,route where ro_id = route.id")
route = cursor.fetchall()

cursor.execute("select opro_id,time from opro_time,time where t_id=time.id")
route_time = cursor.fetchall()
root = ET.Element("operators")
for( id,name, tel,location) in operator:

	oper = ET.SubElement(root, "operator")

	ET.SubElement(oper, "name").text = name
	ET.SubElement(oper, "tel").text = tel
	ET.SubElement(oper, "location").text = location
	
	for(_opro_id,op_id,source,destination,distance,price) in route:
		if(op_id == id):
			r = ET.SubElement(oper, "route")
			ET.SubElement(r, "source").text = source
			ET.SubElement(r, "destination").text = destination
			ET.SubElement(r, "distance").text = str(distance)
			ET.SubElement(r, "price").text = str(price)
			t = ET.SubElement(r,"timetable")
			for(opro_id,time) in route_time:
				if(opro_id == _opro_id):
					
					ET.SubElement(t,"time").text = str(time)
tree = ET.ElementTree(root)
tree.write("filename.xml")
conn.close()

