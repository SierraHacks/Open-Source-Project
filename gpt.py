from openai import OpenAI

def complete(message):
  client = OpenAI(
      api_key="api key"
  )
  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": message,
          }
      ],
      model="gpt-3.5-turbo",
  )
