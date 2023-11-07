import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


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

    Use a dark theme for the website. Background color: #1e1e2e.
    Use nice buttons for all the links. Make the links #f38ba8. 
    Add other div elements and colors to make the website look nice.

    You will now be given a path. You will generate info for the path.
    The path you are given is: {path}
    """.format(path=path)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    site = response["choices"][0]["message"]["content"]
    return site

if __name__ == "__main__":
    # testing
    genDoc("/python/panadas")
