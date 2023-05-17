import os
import subprocess
import speech_recognition as sr
from googletrans import Translator

def download_video(url):
    # Use youtube-dl to download the YouTube video
    subprocess.call(['youtube-dl', '-o', 'video.mp4', url])

def extract_audio():
    # Use ffmpeg to extract audio from the downloaded video
    subprocess.call(['ffmpeg', '-i', 'video.mp4', 'audio.wav'])

def convert_audio_to_text():
    # Use SpeechRecognition to convert audio to text
    r = sr.Recognizer()
    with sr.AudioFile('audio.wav') as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text

def translate_text(text, target_language):
    # Use googletrans to translate the text to the target language
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    translated_text = translation.text
    return translated_text

def generate_comments_file(text, translations):
    # Generate a comments file with the original text and translations
    with open('comments.txt', 'w') as file:
        file.write('Original Text: {}\n'.format(text))
        for lang, translation in translations.items():
            file.write('{} Translation: {}\n'.format(lang, translation))

# YouTube video URL
video_url = 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID'

# List of target languages for translation
target_languages = ['es', 'fr', 'de']

# Step 1: Download the YouTube video
download_video(video_url)

# Step 2: Extract audio from the video
extract_audio()

# Step 3: Convert audio to text
text = convert_audio_to_text()

# Step 4: Translate text into multiple languages
translations = {}
for language in target_languages:
    translated_text = translate_text(text, language)
    translations[language] = translated_text

# Step 5: Generate the comments file
generate_comments_file(text, translations)

# Step 6: Clean up temporary files
os.remove('video.mp4')
os.remove('audio.wav')

print("Comments file generated successfully!")
