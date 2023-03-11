# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import openai

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # Load your API key from an environment variable or secret management service
    api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(model="text-davinci-003", prompt="中国", temperature=0,
                                        max_tokens=1024)

    result = ''
    for x in response.choices:
        result += x.text
    print(result)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
