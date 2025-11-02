#!/usr/bin/env python3
"""Test step 0 - Validate input.json"""

import json
import os
import pytest

def test_input_json_exists():
    """Test that input.json file exists"""
    assert os.path.exists('../input.json'), "input.json file not found"

def test_input_json_valid():
    """Test that input.json has valid JSON format"""
    with open('../input.json', 'r') as f:
        config = json.load(f)
    assert isinstance(config, dict), "input.json should contain a dictionary"

def test_input_json_required_fields():
    """Test that input.json has all required fields"""
    with open('../input.json', 'r') as f:
        config = json.load(f)
    
    required_fields = ['topic_name', 'source_folder', 'num_questions', 'output_dir']
    for field in required_fields:
        assert field in config, f"Missing required field: {field}"

def test_input_json_field_types():
    """Test that input.json fields have correct types"""
    with open('../input.json', 'r') as f:
        config = json.load(f)
    
    assert isinstance(config['topic_name'], str), "topic_name should be string"
    assert isinstance(config['source_folder'], str), "source_folder should be string"
    assert isinstance(config['num_questions'], int), "num_questions should be integer"
    assert isinstance(config['output_dir'], str), "output_dir should be string"

if __name__ == "__main__":
    pytest.main([__file__])
