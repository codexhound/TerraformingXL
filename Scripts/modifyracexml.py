import xml.etree.ElementTree as ET
import glob
import os

# === CONFIGURE THESE ===
input_directory = r'D:\Games\Distant Worlds 2\data'   # <-- Set your input path here
output_directory = r'D:\Games\Distant Worlds 2\mods\TerraformingXL' # <-- Set your output path here

# Make sure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Get all matching files in input directory
xml_files = glob.glob(os.path.join(input_directory, 'Race*.xml'))

for file_path in xml_files:
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Modify all <Factor> values under <RaceFactor>
        for race in root.findall('.//Race'):
            for bias in race.findall('.//RaceFactor'):
                factor = bias.find('Factor')
                if factor is not None and factor.text:
                    try:
                        original = float(factor.text)
                        factor.text = f"{original * 1.5:.3f}"
                    except ValueError:
                        continue

        # Write to output directory with same filename
        filename = os.path.basename(file_path)
        output_path = os.path.join(output_directory, filename)
        tree.write(output_path, encoding='utf-8', xml_declaration=True)
        print(f"Processed: {filename}")

    except ET.ParseError as e:
        print(f"Failed to parse {file_path}: {e}")
