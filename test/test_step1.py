#!/usr/bin/env python3
"""Test step 1 - Validate extracted content"""

import json
import os
import pytest

def test_extracted_content_path_in_json():
    """Test that extracted_content_path is added to input.json"""
    with open('../input.json', 'r') as f:
        config = json.load(f)
    
    assert 'extracted_content_path' in config, "extracted_content_path not found in input.json"

def test_extracted_content_path_prefix():
    """Test that extracted content path starts with topic name"""
    with open('../input.json', 'r') as f:
        config = json.load(f)
    
    path = config['extracted_content_path']
    filename = os.path.basename(path)
    topic = config['topic_name']
    
    assert filename.startswith(topic), f"Filename should start with topic '{topic}'"

def test_extracted_content_file_exists():
    """Test that extracted content file exists"""
    with open('../input.json', 'r') as f:
        config = json.load(f)
    
    path = config['extracted_content_path']
    assert os.path.exists(f"../{path}"), f"Extracted content file not found: {path}"

def test_extracted_content_not_empty():
    """Test that extracted content file is not empty"""
    with open('../input.json', 'r') as f:
        config = json.load(f)
    
    path = config['extracted_content_path']
    assert os.path.getsize(f"../{path}") > 0, "Extracted content file is empty"

if __name__ == "__main__":
    pytest.main([__file__])
