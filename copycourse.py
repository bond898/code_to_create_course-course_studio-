import shutil
import xml.etree.ElementTree as ET
import os
import psycopg2

def copy_folder(source_folder, destination_folder):
    try:
        # Copy the entire contents of the source folder to the destination folder
        shutil.copytree(source_folder, destination_folder)
        print(f"Folder '{source_folder}' successfully copied to '{destination_folder}'.")
    except shutil.Error as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def create_xml_file(folder_path, file_name):
    # Create a simple XML file
    # root = ET.Element("root")
    # child = ET.SubElement(root, "data")
    # child.text = "Hello, XML!"

    # tree = ET.ElementTree(root)
    root = ET.Element("problem") 
    m1 = ET.Element("multiplechoiceresponse") 
    m1.text = "EFGH"
    m1.set('display_name','Multiple Choice')
    m1.set('markdown','&#10;You can use this template as a guide to the simple editor markdown and OLX markup to use for multiple choice problems. Edit this component to replace this template with your own assessment.&#10;&#10;&gt;&gt;Add the question text, or prompt, here. This text is required.||You can add an optional tip or note related to the prompt like this. &lt;&lt;&#10;&#10;( ) an incorrect answer&#10;(x) the correct answer&#10;( ) an incorrect answer&#10;')
    root.append (m1)
    
    # m5 = ET.SubElement(m1,"p")
    # m5.text = "paragraph"
    # m4 = ET.SubElement(m1,"label")
    # m4.text = "label"
    # m2 = ET.SubElement(m1,"description")
    # m2.text = "ABCD"
    # m3 = gfg.SubElement(m1,"choicegroup")
    # m3.text = "choice"
    # 
    #  
    
    a1 = ET.SubElement(m1,"choicegroup")
    a1.text = "choicegroup"


    m6 = ET.SubElement(a1,"choice")
    m6.text = "choice 1"
    m6.set('correct','false')
    m7 = ET.SubElement(a1,"choice")
    m7.text = "choice 2"
    m7.set('correct','true')
    m8 = ET.SubElement(a1,"choice")
    m8.text = "choice 3"
    m8.set('correct','false')
    
        
    tree = ET.ElementTree(root)

    xml_path = os.path.join(folder_path, file_name)
    tree.write(xml_path)
    print(f"XML file '{file_name}' created in '{folder_path}'.")


def update_xml_with_database_data(xml_path, connection):
    try:
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Example: Retrieve data from the database (replace this query with your own)
        cursor.execute("SELECT first_name, last_name FROM customers")
        rows = cursor.fetchall()

        # Update XML elements with data from the database
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for row in rows:
            first_name = row[0]
            last_name = row[0]

            # Example: Update XML elements based on database data
            for element in root.findall(".//p"):
                element.text = str(first_name)
                
            for element in root.findall(".//label"):
                element.text = str(last_name)

        # Write the updated XML file
        tree.write(xml_path)
        print(f"XML file '{xml_path}' updated with data from the database.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection and cursor
        cursor.close()


xml_file_path = '/home/dell/Documents/xmlfile/new created course/problem/example.xml'
database_connection_params = {
   'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': '123456',
    'port': '5432'
}



# Example usage:
source_path = '/home/dell/Documents/xmlfile/newxml/course.tgkj8ztl (copy)/course'
destination_path = '/home/dell/Documents/xmlfile/new created course'
xml_file_name = 'example.xml'
new_destination_path = '/home/dell/Documents/xmlfile/new created course/problem'

copy_folder(source_path, destination_path)

create_xml_file(new_destination_path, xml_file_name)

# Connect to the database
try:
    connection = psycopg2.connect(**database_connection_params)
    print("Connected to the database.")

    # Update XML file with data from the connected database
    update_xml_with_database_data(xml_file_path, connection)

except Exception as e:
    print(f"Error connecting to the database: {e}")

finally:
    # Close the database connection
    if connection:
        connection.close()
        print("Database connection closed.")
        

def create_subelement(xml_file, parent_element_name, subelement_name, attributes=None, text_content=None):
    # Parse the existing XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find the parent element by name
    parent_element = root.findall(".//" + parent_element_name)

    if parent_element is not None:
        # Create a subelement
        subelement = ET.SubElement(root, 'problem', attrib={'url_name': 'example'})
        
        # Save the updated XML tree to the existing file
        tree.write(xml_file)
        print(f"Subelement '{subelement_name}' added to '{parent_element_name}' in {xml_file}")
    else:
        print(f"Parent element '{parent_element_name}' not found in {xml_file}")

# Example usage
xml_file_path = "/home/dell/Documents/xmlfile/new created course/vertical/e10635230a3d487fa1b946d008b6fef6.xml"
parent_element_name = "vertical"
subelement_name = "problem"
attributes = {"url_name": "example"}


create_subelement(xml_file_path, parent_element_name, subelement_name, attributes)
