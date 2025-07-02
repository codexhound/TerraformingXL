import os
import xml.etree.ElementTree as ET

def process_file(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    modified = False
    for rate in root.iter('AssimilationRate'):
        try:
            original = float(rate.text)
            rate.text = str(original / 2)
            modified = True
        except (TypeError, ValueError):
            print(f"Invalid number in {filepath}: {rate.text}")

    if modified:
        tree.write(filepath, encoding='utf-8', xml_declaration=True)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes in: {filepath}")

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.startswith("Race") and filename.endswith(".xml"):
            process_file(os.path.join(directory, filename))

# Example usage
directory_path = r"D:\Games\Distant Worlds 2\mods\TerraformingXL"
process_directory(directory_path)
