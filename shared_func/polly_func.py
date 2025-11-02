import boto3
import subprocess
import tempfile
import os

def speak_text(text):
    """Use AWS Polly to speak the given text"""
    try:
        polly = boto3.client('polly')
        
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId='Joanna'
        )
        
        # Save to temp file and play with system player
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
            temp_file.write(response['AudioStream'].read())
            temp_path = temp_file.name
        
        # Play using system audio player
        subprocess.run(['mpv', '--no-video', temp_path], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL)
        
        # Clean up
        os.unlink(temp_path)
        
    except Exception as e:
        print(f"Speech error: {e}")
