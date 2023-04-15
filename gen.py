import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def genDoc(path):
    prompt = """
    You are wikiGPT. You will provide a wikipedia style info page for any topic.
    Given a website path, you will generate a short but consise html file containing info related to the path.
    Use a dark theme for the website. Background color: #1e1e2e.
    Crucial: At every opportunity you will link to other relative paths of this website. Make the links #f38ba8.
    Sitemap of the website so you can infer what to do:
    /index.html                             # A list of some popular topics
    /<topic>/<topic>.html                   # Info main page for the topic
    /<topic>/<subtopic>/<subtopic>.html     # Info subpage for the subtopic
    /ai/openai/openai.html                  # Info page for the openai
    etc.

    You will now be given a path. You will generate info for the path.
    The path you are given is: {path}
    """.format(path=path)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    site = response["choices"][0]["message"]["content"]
    return site

if __name__ == "__main__":
    # testing
    genDoc("/python/panadas")
