#!/usr/bin/env python3
"""
Step 1: Extract content from any file type using Q chat
"""

import json
import subprocess
import os
import re
import sys

def test():
    """Test this step"""
    try:
        # Test imports and basic operations
        json.loads('{"test": "value"}')
        subprocess.run(['echo', 'test'], capture_output=True)
        os.path.exists('.')
        re.compile(r'test')
        print("✅ Step 1 test passed")
        return True
    except Exception as e:
        print(f"❌ Step 1 test failed: {e}")
        return False

def clean_ansi_codes(text):
    """Remove ANSI escape codes from text"""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def clean_output(text):
    """Clean unwanted output from Q chat response"""
    # Remove ANSI codes
    text = clean_ansi_codes(text)
    
    # Find "Completed in" line and remove everything up to it
    lines = text.split('\n')
    start_index = 0
    
    for i, line in enumerate(lines):
        if 'Completed in' in line:
            start_index = i + 1
            break
    
    # Take only lines after "Completed in"
    result = '\n'.join(lines[start_index:])
    return result.strip()

def main():
    if not test():
        sys.exit(1)
        
    # Load config
    with open('input.json', 'r') as f:
        config = json.load(f)
    
    folder_path = config['source_folder']
    
    # Get all files in folder
    files = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            files.append(file_path)
    
    if not files:
        print("No files found in folder")
        return
    
    # Use Q to extract content from all files
    prompt = f"""Extract and summarize the key content from these files for educational purposes:

Files to process: {', '.join(files)}

Please read each file and provide a comprehensive summary of the main concepts, topics, and important information that would be useful for creating educational questions.

Format the output as structured text with clear sections for each file."""
    
    result = subprocess.run(['q', 'chat', '--no-interactive', '--trust-all-tools', prompt], 
                          capture_output=True, text=True, timeout=120)
    
    if result.returncode != 0:
        print(f"Q chat failed: {result.stderr}")
        return
    
    # Save extracted content with topic-linked filename
    os.makedirs(config['output_dir'], exist_ok=True)
    filename = f"{config['topic_name']}_extracted_content.txt"
    output_path = f"{config['output_dir']}/{filename}"
    
    # Clean ANSI escape codes and status messages from output
    clean_content = clean_output(result.stdout)
    
    with open(output_path, 'w') as f:
        f.write(clean_content)
    
    # Update config with output path
    config['extracted_content_path'] = output_path
    with open('input.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("Content extracted successfully")

if __name__ == "__main__":
    main()
