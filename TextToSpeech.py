import pyttsx3

# Crie um objeto TTS (Text-to-Speech)
engine = pyttsx3.init()
# Defina a voz masculina usando o nome da voz
def text_to_speech(text):
    # Texto que você deseja transformar em fala
    texto = text


    engine.setProperty('rate', 200)  # Velocidade de fala (palavras por minuto)

    # Faça o TTS do texto
    engine.say(texto)

    # Reproduza a fala
    engine.runAndWait()
