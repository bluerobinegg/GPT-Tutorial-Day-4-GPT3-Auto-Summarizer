import gradio as gr
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text_gpt(input_string, max_length):
  full_prompt = f"Answer the prompt: + {input_string}. Make your answer concise and write a {max_length*0.90} word response."
  response = openai.Completion.create(model="gpt-3.5-turbo-instruct",
                                      prompt=full_prompt,
                                      temperature=0,
                                      max_tokens=max_length,
                                      top_p=1,
                                      frequency_penalty=0,
                                      presence_penalty=0)
  answer = response.choices[0]['text']
  return (answer)


def to_gradio():
  demo = gr.Interface(fn=generate_text_gpt,
                      inputs=["text", gr.Slider(0, 500)],
                      outputs="text")
  demo.launch(debug=True, share=True)

if __name__ == "__main__":
  to_gradio()
