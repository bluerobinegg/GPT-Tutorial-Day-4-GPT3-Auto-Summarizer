# Making a Summarizer

To make a summarizer we need to think about what kind of output we want and how to craft a prompt that will give us that.
We might also want to give short but clear context encouraging the model to take inspiration from great writers to hopefully improve the end quality.
Lastly, it is often a good idea to sandwich your content in instructions to focus the model.

Here is one way we could make a prompt for three different styles: 

```python
sum_styles = ["convert the above content into bullet points",
              "write an executive summary of the above content",
              "shrink the word count of the above content without losing any information"
             ]
full_prompt = f"Imagine a great writer summarizing the following content while keeping all key information: {input_string} ||END CONTENT|| Inspired by great writers,  {sum_styles[style]} in {max_length*.75} words:"
```

To implement this we will want to add a dropdown to our Gradio interface and increase our max length to 1,000 tokens. Keep in mind, that each time you ran a summary with 4,000 characters (~1,000 tokens) of input and the same output **it will cost about 4 cents a run.** 

 ```python
 def to_gradio():
  demo = gr.Interface(
    fn=generate_text_gpt,
    inputs=[
      gr.Textbox(lines=2, placeholder="Enter content to summarize..."),
      gr.Slider(0, 1000),
      gr.Dropdown(["bullets", "executive", "trim"], type="index")
    ],
    outputs="text")
  demo.launch(debug=True, share=True)
  ``` 

Let's try summarizing the new OpenAI blog post [How should AI
systems behave, and who should decide](https://openai.com/blog/how-should-ai-systems-behave/)

![image](image_3.png)

How are the results?
How much did they https://openai.com/api/pricing/?
In what ways could they be improved?

One critical way this app would need to be improved is to enable summaries of longer content, how could we summarize content longer than 4,000 tokens?

**Before going to the next page, try building an automated solution to summarize any length text.**

One useful tool is [Textwrap](https://docs.python.org/3/library/textwrap.html) a Python library that can easily convert text into chunks in one line

```python
import textwrap
list_of_chunks = textwrap.wrap(text, num_chars_in_each_chunk)
```





