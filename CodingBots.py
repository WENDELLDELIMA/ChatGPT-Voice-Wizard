
import openai
import Speech
import TextToSpeech
from termcolor import colored
openai.api_key = "SUA API KEY"


def send_message(msg, msg_list):
    msg_list.append(
        {"role": "user", "content": msg}
    )

    max_tokens = 25
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages= msg_list,
        max_tokens=max_tokens)

    return response["choices"][0]["message"]
msg_list = []
while True:
    user_text = Speech.speech_to_text()

    if user_text == "sair":
        TextToSpeech.text_to_speech("Obrigado!, Volte sempre!")
        print(colored(f"Obrigado!, Volte sempre!", 'blue', attrs=['bold']))
        break
    else:
        response = send_message(user_text, msg_list)
        msg_list.append(response)
        print(colored(f"Assistente: {response.content}", 'blue', attrs=['bold']))
        TextToSpeech.text_to_speech({response.content})
