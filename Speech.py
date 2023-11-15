import speech_recognition as sr

# Crie um objeto de reconhecimento de fala
recognizer = sr.Recognizer()

# Função para converter fala em texto
def speech_to_text():
    with sr.Microphone() as source:
        print("Fale alguma coisa...")
        try:
            audio = recognizer.listen(source, timeout=5)  # Aguarde até 5 segundos após o áudio terminar
            print("Aguarde enquanto o áudio é processado...")
            text = recognizer.recognize_google(audio, language="pt-BR")  # Altere o idioma conforme necessário
            return text
        except sr.RequestError as e:
            print(f"Ocorreu um erro durante a solicitação ao Google Web Speech API: {e}")
        except sr.UnknownValueError:
            print("Não foi possível entender o discurso.")

if __name__ == "__main__":
    text = speech_to_text()
    if text:
        print(f"Texto reconhecido: {text}")
