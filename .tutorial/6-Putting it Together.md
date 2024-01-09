# Putting it Together

One approach we could use to summarize any length text is to break it into small enough chunks, summarize each chunk, and join them back together.

Below is my implementation 
```python
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
```

A couple other minor changes to make.

First we can modify our Gradio interface to rely on the new function:
 ```python
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
  ``` 

Second, quickly adding in a save_file function to save our output that we are paying all that money for! Don't forget to import time and write a statement to actually save the file. 

```python
def save_file(content, filepath):
  with open(filepath, 'w', encoding='utf-8') as outfile:
    outfile.write(content)
```

```python
import time
# save a file for reference as well as return full summary
  save_file('\n\n'.join(result), 'outputs/output_%s.txt' % time())
```

Let's go try it out!

What kind of content would help YOU if it were summarized?
News stories? Podcasts? Youtube videos?

If you do not want to use many credits, pick a short text to convert. 