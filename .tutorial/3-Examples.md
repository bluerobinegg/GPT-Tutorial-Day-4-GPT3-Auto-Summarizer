# Examples

**Here are a few examples of how prompt engineering could supercharge the app we made in day 3:**


- To generate a story based on a given theme, get creative with your prompt by adding more details or specific requirements: "**Imagine a world where {_insert theme here_} is the norm. Write a story that captures the essence of this world and its inhabitants:**"
- To translate a text from one language to another, try a prompt that includes some context and specific requirements, such as: "**Translate this passage from {_insert language_} to {_insert language_}, while maintaining the same tone and style as the original.**"
- To generate a text with a specific tone or sentiment, use a prompt that sets clear expectations for the desired outcome, such as: "**Craft a text that conveys a {_insert tone or sentiment_} message, while using {_insert topic or theme_} as your inspiration.**"

These are just basic examples to get you thinking **but prompt engineering can be much more detailed and yield incredible results.** The key here is to make the prompt as specific and clear as possible. The more specific and clear the prompt is, the more likely the model will generate text that is relevant and accurate to the task at hand. The best way to learn this is through practice. 


**_Using the code from Day 3 below try and modify it to implement one of the above examples:_**

```python
import gradio as gr
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")



def generate_text_gpt(input_string, max_length):
  response = openai.Completion.create(model="text-davinci-003",
                                      prompt=input_string,
                                      temperature=0,
                                      max_tokens=max_length,
                                      top_p=1,
                                      frequency_penalty=0,
                                      presence_penalty=0)
  answer = response.choices[0]['text']
  return (answer)


def to_gradio():
  demo = gr.Interface(fn=generate_text_gpt,
                      inputs=["text", gr.Slider(0, 250)],
                      outputs="text")
  demo.launch(debug=True, share=True)


if __name__ == "__main__":
  to_gradio()
```