#!/usr/bin/env python3
"""Test step 2 - Validate questions generation"""

import json
import os
import pytest

def test_questions_path_in_json():
    """Test that questions_path is added to input.json"""
    with open('../input.json', 'r') as f:
        config = json.load(f)
    
    assert 'questions_path' in config, "questions_path not found in input.json"

def test_questions_path_prefix():
    """Test that questions path starts with topic name"""
    with open('../input.json', 'r') as f:
        config = json.load(f)
    
    path = config['questions_path']
    filename = os.path.basename(path)
    topic = config['topic_name']
    
    assert filename.startswith(topic), f"Filename should start with topic '{topic}'"

def test_questions_file_exists():
    """Test that questions file exists"""
    with open('../input.json', 'r') as f:
        config = json.load(f)
    
    path = config['questions_path']
    assert os.path.exists(f"../{path}"), f"Questions file not found: {path}"

def test_questions_file_not_empty():
    """Test that questions file is not empty"""
    with open('../input.json', 'r') as f:
        config = json.load(f)
    
    path = config['questions_path']
    assert os.path.getsize(f"../{path}") > 0, "Questions file is empty"

if __name__ == "__main__":
    pytest.main([__file__])
