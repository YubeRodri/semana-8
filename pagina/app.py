from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import uuid
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({'text': 'No se recibió ningún archivo de audio'}), 400

    audio_file = request.files['audio']
    filename = f"temp_{uuid.uuid4()}.wav"
    audio_path = os.path.join("temp", filename)

    os.makedirs("temp", exist_ok=True)
    audio_file.save(audio_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
    except sr.UnknownValueError:
        text = "No se pudo entender el audio."
    except sr.RequestError:
        text = "Error al conectarse al servicio de reconocimiento."

    os.remove(audio_path)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)

