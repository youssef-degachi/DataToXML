import xml.etree.ElementTree as ET
import os
import xml.dom.minidom as minidom

def create_student():
    name = input("Enter student's name: ")
    email = input("Enter student's email: ")
    city = input("Enter student's city: ")
    role = input("Enter student's role: ")
    number = input("Enter student's number: ")

    student = ET.Element("student")
    name_element = ET.SubElement(student, "name")
    name_element.text = name
    email_element = ET.SubElement(student, "email")
    email_element.text = email

    address = ET.SubElement(student, "address")
    city_element = ET.SubElement(address, "city")
    city_element.text = city
    role_element = ET.SubElement(address, "role")
    role_element.text = role
    number_element = ET.SubElement(address, "number")
    number_element.text = number

    return student

def prettify_xml(elem):
    #ta3mel tab w return new line
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

def save_to_xml(students, filename="students.xml"):
    try:
        # tchouf kin 3indek filename wla la
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            tree = ET.parse(filename)
            root = tree.getroot()
        else:
            # asna3  ficher kin mich mawjoud
            root = ET.Element("students")
            tree = ET.ElementTree(root)
    except ET.ParseError:
        root = ET.Element("students")
        tree = ET.ElementTree(root)

    # add new student
    for student in students:
        root.append(student)
    
    # write in teh file 
    xml_string = prettify_xml(root)

    # update data
    with open(filename, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(xml_string)

def main():
    students = []
    while True:
        add_student = input("Do you want to add a new student? (yes/no): ").lower()
        if add_student == "yes" or add_student == "y":
            student = create_student()
            students.append(student)
            print("Student added successfully.")
        elif add_student == "no"  or add_student == "n":
            if students:
                save_to_xml(students)
                print(f"Saved {len(students)} students to the XML file.")
            print("Exiting the program.")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()