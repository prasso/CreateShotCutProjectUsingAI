
# CreateShotCutProjectUsingAI

This project, generated with ChatGPT, contains logic to read a list of `.wav` files from disk and add them to a new `.mlt` (Shotcut) project file. The `.wav` files are generated using Text-to-Speech (TTS) technology.

## Purpose

The purpose of this project is to simplify the video creation process for tutorials related to the Prasso Framework.

## Prerequisites

Before using this project, ensure you have the following installed:
- [TTS](https://github.com/coqui-ai/TTS)
- Python
- Shotcut

These tools are required to generate `.wav` files, populate the `.mlt` file, and create the training video.

## Usage

1. **Generate the Script**: Use AI tools to generate the script for your video.

2. **Create the .wav Files**:
   - Write a script (`scripts.sh`) to convert the text of your video transcript into `.wav` files using TTS.
   - Run the script to generate the `.wav` files.

3. **Create the .mlt File**:
   - Run the provided Python script to create the `.mlt` file for Shotcut.

4. **Open and Edit in Shotcut**:
   - Open the generated `.mlt` file in Shotcut. The timeline will display each video frame, assuming you used the script to generate a `.wav` file for each frame.
   - Add your video scenes on a new timeline, matching each scene’s length to the length of the corresponding audio track.

By following these steps, you can streamline the process of creating instructional videos for the Prasso Framework.

