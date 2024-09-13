import tiktoken

cl100k = tiktoken.get_encoding("cl100k_base")

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

def token_counter(string):
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return num_tokens

with open("all_txt.txt", "r") as all_txt:
    total_tokens = 0
    for line in all_txt:
        num_tokens = token_counter(line)
        total_tokens += num_tokens

print("TOTAL TOKENS:", total_tokens)