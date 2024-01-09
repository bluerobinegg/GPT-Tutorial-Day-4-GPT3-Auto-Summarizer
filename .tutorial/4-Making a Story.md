# Making a Story

- To generate a story based on a given theme, get creative with your prompt by adding more details or specific requirements, such as: "**Imagine a world where {_insert theme here_} is the norm. Write a story that captures the essence of this world and its inhabitants:**"

To implement this the only change we need to make is modify our input string before passing it to be completed:
```python
def generate_text_gpt(input_string, max_length):
  full_prompt = f"Imagine a world where {input_string} is the norm. Write a {max_length*.75} word story that captures the essence of this world and its inhabitants:"  
  response = openai.Completion.create(model="text-davinci-003",
                                        prompt=full_prompt,
                                        temperature=0.1,
                                        max_tokens=max_length,
                                        top_p=1,
                                        frequency_penalty=0,
                                        presence_penalty=0)
  answer = response.choices[0]['text']
  return (answer)
```

Notice how we can modify the prompt in different ways to give it context of the exact output we are looking for. 


Our next step is going to be making a prompt for summarizing content, **spend some time thinking about it and make a prompt before going to the next page**. You can compare with our suggestions and see which you prefer!