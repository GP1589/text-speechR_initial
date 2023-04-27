import openai

openai.api_key = "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" 
# Asegurate de reemplazar YOUR_API_KEY con tu propia clave de API

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="¿Que es ChatGPT",
  max_tokens=2048,
)


print(response.choices[0].text)
# for choice in response.choices:
#     print(choice.text)