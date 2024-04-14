from transformers import GPT2LMHeadModel, GPT2Tokenizer


# # Initialize the tokenizer and model
def gpt_call(query) -> str:
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Encode the input text
    input_ids = tokenizer.encode(query,return_tensors='pt')

    # Generate text
    output = model.generate(input_ids, max_length=1500, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode the output
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text


# Try this code out and see output of this Model
# query = "Google LLC is an American multinational corporation and technology company focusing on online advertising, search engine technology, cloud computing, computer software, quantum computing, e-commerce, consumer electronics, and artificial intelligence (AI)"
# print(generate_paragraph(query))