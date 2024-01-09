# Final Touches

### Going further
There are so many ways these projects can go further. While today is the end of this quick course, it is just the start of your journey with large language models. 

These tools radically change the way the digital world interacts with language and there is immense opportunity. OpenAI released a state-of-the-art voice-to-text model called [Whisper](https://github.com/openai/whisper) in Sept. 2022 that anyone can use to convert voice to text easily.  

We hope to hear what you have been working on and how you are using LLM's on social media or at camp this year! 

**Today in Day 4 we:**
* Learned about prompt engineering and how to use it to solve more complex problems
* Created an auto-summarizer that can summarize any length text into any format we want
* Once more discussed the ethical considerations of using powerful language models


## Checkout AI Camp!
<img src="https://i.imgur.com/cm5IS8V.png" width="100px" height="100px" id="ai-camp">

 **If you are a teenager interested in joining a community solving problems with technology and exploring careers in tech, check out AI Camp!**

  We offer 1-week and 3-week camps to start, but exceptional students can join our [Team Tomorrow](https://teamtomorrow.com/). **_TT members work after school + weekends on paid internal and external projects_**, opening doors for their future. 

  In fact TT member Jayden Cavanagh, a college freshman, helped create today's content!


## Solution Code:

```python
import gradio as gr
import os
import openai
import textwrap
import time

openai.api_key = os.getenv("OPENAI_API_KEY")


def save_file(content, filepath):
  with open(filepath, 'w', encoding='utf-8') as outfile:
    outfile.write(content)


def chunk_summarize(alltext, max_length, style):
  # split and convert
  chunks = textwrap.wrap(alltext, 4000)
  result = list()
  count = 0

  for chunk in chunks:
    count = count + 1
    summary = generate_text_gpt(chunk, max_length, style)
    print('\n\n', count, 'of', len(chunks), summary)
    result.append(summary)

  # save a file for reference as well as return full summary
  save_file('\n\n'.join(result), 'outputs/output_%s.txt' % time())

  return '\n\n'.join(result)


def generate_text_gpt(input_string, max_length, style):
  sum_styles = [
    "convert the above content into bullet points",
    "write an executive summary of the above content",
    "shrink the word count of the above content without losing any information"
  ]
  full_prompt = f"Imagine a great writer summarizing the following content while keeping all key information: {input_string} ||END CONTENT|| Inspired by great writers,  {sum_styles[style]} in {max_length*.75} words:"
  response = openai.Completion.create(model="text-davinci-003",
                                      prompt=full_prompt,
                                      temperature=0.1,
                                      max_tokens=max_length,
                                      top_p=1,
                                      frequency_penalty=0,
                                      presence_penalty=0)
  answer = response.choices[0]['text']
  return (answer)


def to_gradio():
  demo = gr.Interface(
    fn=chunk_summarize,
    inputs=[
      gr.Textbox(lines=2, placeholder="Enter content to summarize..."),
      gr.Slider(0, 1000),
      gr.Dropdown(["bullets", "executive", "trim"], type="index")
    ],
    outputs="text")
  demo.launch(debug=True, share=True)


if __name__ == "__main__":
  to_gradio()
```