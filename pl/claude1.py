import os
import promptlayer

promptlayer.api_key = os.environ.get("PROMPTLAYER_API_KEY")

anthropic = promptlayer.anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    # api_key="my_api_key",
)

# completion = client.completions.create(
#     prompt=f'{anthropic.HUMAN_PROMPT} How many toes do dogs have? {anthropic.AI_PROMPT}',
#     stop_sequences=[anthropic.HUMAN_PROMPT],
#     model='claude-v1-100k',
#     max_tokens_to_sample=100,
#     pl_tags=['animal-toes']
# )

# completion = client.completions.create(
#     prompt=f'{anthropic.HUMAN_PROMPT} 狗有多少个脚趾? {anthropic.AI_PROMPT}',
#     stop_sequences=[anthropic.HUMAN_PROMPT],
#     model='claude-2.1',
#     max_tokens_to_sample=100,
#     pl_tags=['animal-toes']
# )

completion = client.messages.create(
    messages=[
        {
            "role": "user",
            "content": "狗有多少个脚趾呢",
        }
    ],
    model='claude-3-opus-20240229',
    max_tokens=500,
    pl_tags=['animal-toes']
)

print(completion)
