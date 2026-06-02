from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

# ISO language codes mapped to their names
LANGUAGES = {
    'Marathi': 'mr',
    'Hindi': 'hi',
    'Sanskrit': 'sa'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    original_quote = ""
    translated_text = None
    selected_lang = None

    if request.method == 'POST':
        original_quote = request.form.get('quote', '').strip()
        selected_lang = request.form.get('language')
        
        if original_quote and selected_lang in LANGUAGES:
            lang_code = LANGUAGES[selected_lang]
            try:
                # Translating only to the selected language
                translated_text = GoogleTranslator(source='en', target=lang_code).translate(original_quote)
            except Exception as e:
                translated_text = f"Translation Error: {str(e)}"

    return render_template('index.html', 
                           quote=original_quote, 
                           translated_text=translated_text,
                           selected_lang=selected_lang)

if __name__ == '__main__':
    app.run(debug=True)