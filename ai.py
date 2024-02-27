import openai

# Substitua 'your_api_key_here' pela sua chave da API da OpenAI
openai.api_key = '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'

response = openai.Completion.create(
  engine="text-davinci-003", # Substitua pelo identificador correto do modelo se necessário
  prompt="Boa noite!",
  temperature=1.0, # Configuração da temperatura para o máximo
  max_tokens=100, # Ajuste conforme necessário para o comprimento da resposta desejado
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].text.strip())