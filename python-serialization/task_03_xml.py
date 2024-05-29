#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to the given filename.

    Parameters:
    - dictionary (dict): The dictionary to serialize.
    - filename (str): The name of the file to save the serialized XML data.
    """
    try:
        # Create the root element
        root = ET.Element("data")

        # Iterate through the dictionary items and
        # add them as child elements to the root
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Create the XML tree and write it to the file
        tree = ET.ElementTree(root)
        tree.write(filename)

        return True

    except Exception as e:
        print(f"An error occurred during serialization: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Read XML data from a file and return a deserialized Python dictionary.

    Parameters:
    - filename (str): The name of the file to read the XML data from.

    Returns:
    - dict: The deserialized dictionary, or None if an error occurs.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from the XML elements
        dictionary = {child.tag: child.text for child in root}

        return dictionary

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None

    except Exception as e:
        print(f"An error occurred during deserialization: {e}")
        return None


if __name__ == "__main__":
    # Sample Test
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    if serialize_to_xml(sample_dict, xml_file):
        print(f"Dictionary serialized to {xml_file}")

        deserialized_data = deserialize_from_xml(xml_file)
        print("\nDeserialized Data:")
        print(deserialized_data)
    else:
        print(f"Failed to serialize the dictionary to {xml_file}")
