
import xml.etree.ElementTree as ET
import csv
import ntpath
import sys

if( len(sys.argv) == 2 ):
    path = sys.argv[1]
else :
    print("Wrong Arguments .....")
    exit


#XML
xml_file = ntpath.basename(path)
tree = ET.parse( path )
root = tree.getroot()


#CSV File
csv_file = xml_file+'.csv'
csv_handler = open(csv_file, 'w')
writer = csv.writer(csv_handler)
csv_header = ['Pin', 'Name', 'Type', 'Functionality']
writer.writerow(csv_header)


for child in root:

    if( child.tag.find("Pin") >= 0 ):

        pin =  child.attrib['Position']   
        type_str = child.attrib['Type']
        name_str = child.attrib['Name']
        func_str = ''
        for item in child:
            if(item.tag.find("Signal") >= 0 ) :
                func_str += item.attrib['Name']
                func_str += '/'


        writer.writerow([pin, name_str, type_str , func_str])

csv_handler.close()