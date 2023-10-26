import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a master scheduler who helps college students make their four year plans"},
        {"role": "user", "content": "I am a freshman computer science student at Northwestern in the McCormick School of Engineering. I want to take four courses per quarter, and I have to fulfill all of my graduation requirements. Make me a four year plan using Northwestern's course catalog formatted as [year] [quarter]: [list of classes for that quarter]"}
    ]
)

print(completion.choices[0].message)
