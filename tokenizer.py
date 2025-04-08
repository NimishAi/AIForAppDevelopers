import tiktoken

#To verify encoding & decoding :  encode and then decode the encoded one gives same result.
enc = tiktoken.get_encoding("o200k_base")
assert enc.decode(enc.encode("hello world")) == "hello world"

#print vocabsize
print("Vocab Size:",enc.n_vocab)

# To get the tokeniser corresponding to a specific model in the OpenAI API:
enc = tiktoken.encoding_for_model("gpt-4o")
print(enc.encode("chai aur code"))