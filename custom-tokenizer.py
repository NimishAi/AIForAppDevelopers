import string

class CustomTokenizer:
    def __init__(self):
        self.token_dict = self.token_dictionary()
        self.reverse_token_dict = {v: k for k, v in self.token_dict.items()}

    @staticmethod
    def token_dictionary():
        tokens = list(string.ascii_letters)  # A-Z and a-z
        token_dict = {token: i for i, token in enumerate(tokens)}
        special_tokens = [
            " ", ",", ".", "!", "?", "'", "\"", ";", ":", "-", "_", "(", ")", 
            "{", "}", "[", "]", "<", ">", "/", "\\", "&", "%", "$", "#", "@", 
            "^", "*", "+", "=", "~", "`", "|", "\n", "\t", "\r", "\b"
        ]
        start_index = 53  # Start after the letters
        for i, token in enumerate(special_tokens):
            token_dict[token] = start_index + i
        return token_dict

    def vocab(self):
        return len(self.token_dict)
    
    def encode(self, word):
        return [self.token_dict[char] for char in word if char in self.token_dict]

    def decode(self, tokens):
        return ''.join(self.reverse_token_dict[token] for token in tokens if token in self.reverse_token_dict)


# Example usage
tokenizer = CustomTokenizer()
encoded = tokenizer.encode("Hey this is done, now we can encode and decode tokens accordingly!")
decoded = tokenizer.decode(encoded)
print("Encoded:", encoded)
print("Decoded:", decoded)
print("Length of tokenizer:", tokenizer.vocab())