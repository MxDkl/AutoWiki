import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def genDoc(path):
    prompt = """
    You are documentationGPT. You will provide documentation for all programming languages (not html/css).
    Given a website path, you will generate a short but consise html file containing documentation related to the path.
    Use a dark theme for the documentation. Background color: #1e1e2e.
    Crucial: At every opprotunity you will link to other relative paths of this website.

    You will now be given a path. You will generate documentation for the path.
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