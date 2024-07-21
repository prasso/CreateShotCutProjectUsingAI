import os
import re
import xml.etree.ElementTree as ET
from datetime import timedelta

def find_wav_files(folder):
    print(f"Searching for .wav files in folder: {folder}")

    def natural_sort_key(s):
        return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]

    wav_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.wav')]
    wav_files.sort(key=natural_sort_key)

    print(f"Found {len(wav_files)} .wav files.")
    for file in wav_files:
        print(f"Found file: {file}")
    return wav_files

def get_wav_length(file_path):
    import wave
    with wave.open(file_path, 'rb') as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate)
        return timedelta(seconds=duration)

def create_shotcut_project(folder, output_file):
    files = find_wav_files(folder)
    
    if not files:
        print("No .wav files found in the specified folder.")
        return
    
    # Parse the template XML
    tree = ET.parse('template.mlt')
    root = tree.getroot()
    
    # Find the profile element
    profile = root.find("./profile")
    if profile is None:
        print("Error: 'profile' element not found in template.")
        return
    
    for idx, file in enumerate(files):
        print(f"Processing file {idx+1}/{len(files)}: {file}")
        producer_id = f"chain{idx}"
        duration = get_wav_length(file)
        length_str = str(duration)
        out_str = (duration - timedelta(milliseconds=40))

        # Create chain element
        chain = ET.Element("chain", id=producer_id, out=str(out_str))
        ET.SubElement(chain, "property", name="length").text = length_str
        ET.SubElement(chain, "property", name="eof").text = "pause"
        ET.SubElement(chain, "property", name="resource").text = file
        ET.SubElement(chain, "property", name="mlt_service").text = "avformat-novalidate"
        ET.SubElement(chain, "property", name="meta.media.nb_streams").text = "1"
        ET.SubElement(chain, "property", name="meta.media.0.stream.type").text = "audio"
        ET.SubElement(chain, "property", name="meta.media.0.codec.sample_fmt").text = "s16"
        ET.SubElement(chain, "property", name="meta.media.0.codec.sample_rate").text = "22050"
        ET.SubElement(chain, "property", name="meta.media.0.codec.channels").text = "1"
        ET.SubElement(chain, "property", name="meta.media.0.codec.name").text = "pcm_s16le"
        ET.SubElement(chain, "property", name="meta.media.0.codec.long_name").text = "PCM signed 16-bit little-endian"
        ET.SubElement(chain, "property", name="meta.media.0.codec.bit_rate").text = "352800"
        ET.SubElement(chain, "property", name="seekable").text = "1"
        ET.SubElement(chain, "property", name="audio_index").text = "0"
        ET.SubElement(chain, "property", name="video_index").text = "-1"
        ET.SubElement(chain, "property", name="creation_time").text = "2024-07-20T13:39:19"  # Dummy timestamp
        ET.SubElement(chain, "property", name="astream").text = "0"
        ET.SubElement(chain, "property", name="shotcut:skipConvert").text = "1"
        ET.SubElement(chain, "property", name="xml").text = "was here"
        ET.SubElement(chain, "property", name="shotcut:hash").text = "dummy_hash"  # Dummy hash

        # Insert the chain after the profile
        profile_index = list(root).index(profile)
        root.insert(profile_index + 1, chain)
        
        # Add the chain to the playlist
        entry_attribs = {"producer": producer_id, "in": "00:00:00.000", "out": str(out_str)}
        playlist = root.find("./playlist[@id='main_bin']")
        if playlist is None:
            print("Error: 'main_bin' playlist not found in template.")
            return
        ET.SubElement(playlist, "entry", attrib=entry_attribs)
    
    # Write the modified XML to the output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"Shotcut project created successfully: {output_file}")

# Specify the folder containing the .wav files and the output file
folder = "./"
output_file = "PrassoBusinessUsecase-generated.mlt"

# Create the Shotcut project
create_shotcut_project(folder, output_file)
