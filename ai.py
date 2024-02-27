import openai

# Substitua 'sua_chave_api_aqui' pela sua chave de API da OpenAI
openai.api_key = 'sua_chave_api_aqui'

def get_chatgpt_response(prompt_text):
    try:
        response = openai.Completion.create(
          engine="text-davinci-004",  # Especifica o modelo DaVinci
          prompt=prompt_text,
          temperature=1.0,  # Configura a temperatura para o valor máximo (aumenta a criatividade)
          max_tokens=4096,  # Configura o número máximo de tokens permitido pela API para uma única resposta
          top_p=1.0,  # Usa nucleus sampling com um valor que permite a maior diversidade
          frequency_penalty=0,
          presence_penalty=0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Ocorreu um erro ao gerar a resposta: {str(e)}"

# Solicita ao usuário que insira o texto
user_input = input("Metapower: ")

# Gera e imprime a resposta do modelo
response_text = get_chatgpt_response(user_input)
print(response_text)