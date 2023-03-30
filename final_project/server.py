from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = translator.english_to_french(textToTranslate)
    return translatedText

@app.route("/french_to_english")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = translator.french_to_english(textToTranslate)
    # Write your code here
    return translatedText

@app.route("/")
def render_template('index.html'):
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
