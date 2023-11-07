import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()


def genDoc(path):
    prompt = """
    You are wikiGPT. You will provide a wikipedia style info page for any topic.
    Given a website path, you will generate an html file containing info related to the path.
    Crucial: At every opportunity you will link to other relative paths of this website.
    Sitemap of the website so you can infer what to do:
    /index.html                             # A list of some popular topics
    /<topic>/<topic>.html                   # Info main page for the topic
    /<topic>/<subtopic>/<subtopic>.html     # Info subpage for the subtopic
    etc.

    Use a dark Nord theme for the website. Make nice buttons and other interavtive elements.

    Do not ever append or prepend any explanation to the generated file. DO NOT USE CODE BLOCKS.

    You will now be given a path. You will generate info for the path.
    The path you are given is: {path}
    """.format(path=path)

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    site = response.choices[0].message.content
    return site

if __name__ == "__main__":
    # testing
    genDoc("/python/panadas")
