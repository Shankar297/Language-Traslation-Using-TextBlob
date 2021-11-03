from flask import Flask, render_template, request, url_for 
from textblob import TextBlob

app = Flask('__name__')

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/change',methods = ['POST'])
def change():
    if request.method == 'POST':
        received_text = request.form['rawtext']
        text = TextBlob(received_text)
        lang = request.form['lang']
        if lang == 'hi':
            converted = text.translate(to='hi')
        elif lang == 'mr':
            converted = text.translate(to='mr')
        elif lang == 'te':
            converted = text.translate(to='te')
        elif lang == 'pa':
            converted = text.translate(to='pa')
        elif lang == 'gu':
            converted = text.translate(to='gu')
        else:
            converted = text.translate(to='ta')

    return render_template('home.html',received_text = received_text, converted = converted)
    

if __name__ =='__main__':
    app.run(debug=True)
