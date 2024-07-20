import os
import xml.etree.ElementTree as ET

# Function to find all .wav files in the specified folder
def find_wav_files(folder):
    print(f"Searching for .wav files in folder: {folder}")
    wav_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.wav')]
    print(f"Found {len(wav_files)} .wav files.")
    for file in wav_files:
        print(f"Found file: {file}")
    return wav_files

# Function to add files to the MLT XML
def create_shotcut_project(folder, output_file):
    files = find_wav_files(folder)
    
    if not files:
        print("No .wav files found in the specified folder.")
        return
    
    # Parse the template XML
    tree = ET.parse('template.mlt')
    root = tree.getroot()
    
    # Find the playlist and tractor
    playlist = root.find("./playlist[@id='main_bin']")
    tractor = root.find("./tractor[@id='tractor0']")

    # Find the index to insert producers before the first playlist
    insert_index = list(root).index(tractor)
    
    # Add each file to the playlist and create corresponding entries in the tractor
    for idx, file in enumerate(files):
        print(f"Processing file {idx+1}/{len(files)}: {file}")
        producer_id = f"producer{idx}"
        
        # Create producer element
        producer = ET.SubElement(root, "producer", id=producer_id)
        ET.SubElement(producer, "property", name="resource").text = file
        ET.SubElement(producer, "property", name="mlt_service").text = "avformat-novalidate"
        ET.SubElement(producer, "property", name="video_delay").text = "0"
        
        # Insert the producer before the first playlist
        root.insert(insert_index, producer)
        insert_index += 1  # Adjust insert index to account for the newly inserted producer
        
        # Add the producer to the playlist
        ET.SubElement(playlist, "entry", producer=producer_id)
        
        # Add the producer track to the tractor
        ET.SubElement(tractor, "track", producer=producer_id)
    
    # Write the modified XML to the output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"Shotcut project created successfully: {output_file}")

# Specify the folder containing the .wav files and the output file
folder = "./"
output_file = "PrassoBusinessUsecase-generated.mlt"

# Create the Shotcut project
create_shotcut_project(folder, output_file)
