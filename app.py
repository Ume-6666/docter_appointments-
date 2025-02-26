from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message').strip().lower()
    
    # Detailed advice logic
    if user_message in ['hello', 'hi', 'hey']:
        response = ("Hello! Please choose your health condition.\n"
                    "1.fever.\n"
                    "2.cold.\n"
                    "3.stomach ache.\n"
                    "4.headache.\n"
                    "5.cough.\n")
    elif 'fever' in user_message:
        response = (
            "For fever:\n\n"
            "1. **What to Do:**\n"
            "- Drink plenty of fluids to stay hydrated.\n"
            "- Rest as much as possible.\n"
            "- Take over-the-counter medications like acetaminophen or ibuprofen to reduce fever and discomfort.\n"
            "- Wear light clothing and keep the room cool.\n"
            "\n2. **What Not to Do:**\n"
            "- Do not ignore severe symptoms such as persistent high fever or difficulty breathing.\n"
            "- Avoid taking aspirin, especially in children and teenagers, as it can cause serious complications.\n"
            "- Do not overdress or use heavy blankets which can raise body temperature further.\n"
        )
    elif 'cold' in user_message:
        response = (
            "For a cold:\n\n"
            "1. **What to Do:**\n"
            "- Stay hydrated by drinking water, herbal teas, and broths.\n"
            "- Rest and avoid strenuous activities.\n"
            "- Use saline nasal sprays to relieve nasal congestion.\n"
            "- Gargle with salt water to soothe a sore throat.\n"
            "- Over-the-counter medications like decongestants and cough syrups can help alleviate symptoms.\n"
            "\n2. **What Not to Do:**\n"
            "- Avoid smoking or exposure to secondhand smoke which can worsen symptoms.\n"
            "- Do not take antibiotics unless prescribed by a doctor, as they are ineffective against viral infections like the common cold.\n"
            "- Avoid spreading germs by practicing good hygiene like frequent hand washing and using tissues or elbows to cover sneezes and coughs.\n"
        )
    elif 'headache' in user_message:
        response = (
            "For headaches:\n\n"
            "1. **What to Do:**\n"
            "- Rest in a quiet, dark room.\n"
            "- Stay hydrated by drinking plenty of water.\n"
            "- Apply a cold or warm compress to your forehead or neck.\n"
            "- Over-the-counter pain relievers like acetaminophen or ibuprofen can help.\n"
            "- Practice relaxation techniques and manage stress.\n"
            "\n2. **What Not to Do:**\n"
            "- Avoid excessive screen time or bright lights.\n"
            "- Do not ignore severe or persistent headaches which could indicate a more serious condition.\n"
            "- Avoid overusing pain medications as it can lead to rebound headaches.\n"
        )
    elif 'stomach ache' in user_message:
        response = (
            "For stomach pain:\n\n"
            "1. **What to Do:**\n"
            "- Drink clear fluids like water, herbal tea, or broth.\n"
            "- Eat bland foods such as crackers, bananas, or rice.\n"
            "- Rest and avoid heavy or greasy foods.\n"
            "- Use a heating pad on your abdomen to relieve pain.\n"
            "\n2. **What Not to Do:**\n"
            "- Avoid consuming alcohol, caffeine, or spicy foods which can irritate the stomach.\n"
            "- Do not take over-the-counter medications like pain relievers without consulting a healthcare provider.\n"
            "- Avoid strenuous activities until the pain subsides.\n"
        )
    elif 'cough' in user_message:
        response = (
            "For a cough:\n\n"
            "1. **What to Do:**\n"
            "- Stay hydrated by drinking plenty of fluids.\n"
            "- Use cough drops or lozenges to soothe the throat.\n"
            "- Consider using a humidifier to keep the air moist.\n"
            "- Rest and avoid irritants like smoke or strong odors.\n"
            "\n2. **What Not to Do:**\n"
            "- Avoid taking cough suppressants if you have a productive cough (one with mucus).\n"
            "- Do not ignore a persistent cough that lasts more than a few weeks or is accompanied by other symptoms like fever or shortness of breath.\n"
        )
    elif 'thank you' in user_message:
        response = 'You’re welcome! If you have any more questions, feel free to ask.'
    elif 'goodbye' in user_message:
        response = 'Goodbye! Take care.'
    else:
        response = 'I’m not sure how to respond to that. Can you please provide more details or ask something else?'
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
