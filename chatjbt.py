from openai import OpenAI

client = OpenAI()

if __name__ == '__main__':
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}])

    result = ''
    for x in completion.choices:
        result += x.message.content
    print(result)