import os
import promptlayer
# from openai import OpenAI

promptlayer.api_key = os.environ.get("PROMPTLAYER_API_KEY")

OpenAI = promptlayer.openai.OpenAI
openai = OpenAI()

# response = openai.completions.create(
#     model="gpt-4",
#     prompt="What is the largest desert in the world?",
# )
# print(response.choices[0].text)

# response = openai.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are an AI."},
#     {"role": "user", "content": "Compose a short poem about soccer and messi."}
#   ],
#   pl_tags=["getting-started"]
# )
# print(response.choices[0].message.content)

response = openai.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are an AI."},
    {"role": "user", "content": "What is the largest desert in the world?"}
  ],
  pl_tags=["qa"]
)
print(response.choices[0].message.content)
