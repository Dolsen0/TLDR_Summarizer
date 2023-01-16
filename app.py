import openai
from api_key import apiKey

openai.api_key = apiKey

message = input("\nwhat would you like to summarize?\n")
response = openai.Completion.create(
    model= "text-davinci-002",
    prompt = f"summarize the following message, it's too long: {message}",
    temperature = .8,
    max_tokens = 80,
    top_p = 1
)

tldr = response["choices"][0]["text"]

print(tldr)