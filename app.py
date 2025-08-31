from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template("index.html", languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.form.get('text', '')
    target_language = request.form.get('target_language', '')

    if not text or not target_language:
        return render_template("result.html",
                               translated_text="Error: Missing text or target language")

    try:
        translated_text = translator.translate(text, dest=target_language).text
        return render_template("result.html",
                               translated_text=translated_text,
                               original=text,
                               language=LANGUAGES.get(target_language, target_language))
    except Exception as e:
        return render_template("result.html", translated_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
