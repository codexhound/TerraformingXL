import os
import xml.etree.ElementTree as ET

# List of OrbTypeIds to update
TARGET_IDS_ALL_HAB = {"10","11","12","19","20","21","22","26","29","30","7","8","9","17","18","23","27"} ## everything
TARGET_IDS_EXTREME_HAB = {"10","11","12","19","20","21","22","23","26","29","30"} ## extreme
##TARGET_IDS = {"7","8","9","17","18","23","27"} ##green

def update_orbtype_factors(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for orb_type in root.findall("OrbType"):
        child_types = orb_type.find("ChildTypes")
        if child_types is not None:
            for orb_factor in child_types.findall("OrbTypeFactor"):
                orb_id_elem = orb_factor.find("OrbTypeId")
                factor_elem = orb_factor.find("Factor")
                if (
                    orb_id_elem is not None and 
                    factor_elem is not None and 
                    orb_id_elem.text in TARGET_IDS_ALL_HAB
                ):
                    try:
                        old_val = float(factor_elem.text)
                        print(f"Found habitable planet type: {orb_id_elem.text} with prob of {old_val}")
                        new_val = old_val * 0.10 ## everything
                        print(f"Modifying by 0.25: Now prob is {new_val}")
                        if (
                            orb_id_elem.text in TARGET_IDS_EXTREME_HAB
                        ):
                            print(f"Found extreme habitable planet type: {orb_id_elem.text}")
                            new_val = new_val * 0.7 ## extreme
                            print(f"Modifying by 0.7: Now prob is {new_val}")
                        factor_elem.text = f"{new_val:.6f}"
                    except ValueError:
                        continue

    tree.write(xml_path, encoding="utf-8", xml_declaration=True)
    print(f"Updated: {xml_path}")

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.lower() == "orbtypes.xml":
            file_path = os.path.join(directory, filename)
            update_orbtype_factors(file_path)

# Example usage:
# Replace with your actual directory
if __name__ == "__main__":
    target_directory = r"D:\Games\Distant Worlds 2\mods\TerraformingXL"
    process_directory(target_directory)
