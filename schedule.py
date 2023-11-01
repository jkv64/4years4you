import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

context = """You are a master scheduler who helps Northwestern University students make their four year plans.
You always read the appropriate department websites to understand what graduation requirements are.
You always give both the course number and name and adhere to the given output format. If a slot could be
filled by multiple courses, note that, but give an example course name and number as well.
Output format:
{
    "First Year": [
        {
        "Fall": []
        }
    
    ]
}"""

prompt = """I am a freshman computer science student at Northwestern in the McCormick School of Engineering. 
I want to take four courses per quarter, and I have to fulfill all of my graduation requirements. 
Make me a four year plan using Northwestern's course catalog formatted as [year] [quarter]: [list of classes for that quarter]"""

completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": context},
        {"role": "user", "content": prompt}
    ]
)

print(completion.choices[0].message)
