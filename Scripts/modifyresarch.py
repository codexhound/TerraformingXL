import os
import xml.etree.ElementTree as ET

def update_orbtype_factors(directory):
    for filename in os.listdir(directory):
        if filename.lower().startswith("research") and filename.lower().endswith(".xml"):
            file_path = os.path.join(directory, filename)

            tree = ET.parse(file_path)
            root = tree.getroot()

            modified = False

            # Traverse ColonizationSuitabilityModifiers -> OrbTypeFactor
            for modifier in root.iter("ColonizationSuitabilityModifiers"):
                for factor_node in modifier.findall("OrbTypeFactor"):
                    factor_elem = factor_node.find("Factor")
                    if factor_elem is not None and factor_elem.text:
                        try:
                            original_value = float(factor_elem.text)
                            new_value = original_value * 1.5
                            factor_elem.text = f"{new_value:.6f}"
                            modified = True
                        except ValueError:
                            continue

            if modified:
                tree.write(file_path, encoding="utf-8", xml_declaration=True)
                print(f"Updated: {filename}")
            else:
                print(f"No changes made: {filename}")

# USAGE: Replace with your actual directory path
update_orbtype_factors(r"D:\Games\Distant Worlds 2\mods\TerraformingXL")
