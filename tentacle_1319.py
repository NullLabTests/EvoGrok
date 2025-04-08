import re
from collections import Counter

def tentacle(input_data):
    # Convert input to string for consistency
    input_str = str(input_data).strip().lower()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        if 'data analysis' in input_str:
            return process_html("data analysis html document detected", input_str)
        elif 'mathematics' in input_str:
            return process_html("mathematics html document detected", input_str)
        elif 'text processing' in input_str:
            return process_html("text processing html document detected", input_str)
        else:
            return process_html("unknown html document detected", input_str)
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_str)
        result_str = str(result).lower()
        return process_non_html(result_str, evaluated=True)
    except:
        # If evaluation fails, process the input as text
        return process_non_html(input_str, evaluated=False)

def process_html(doc_type, html_content):
    # Extract content between the first > and <
    content = re.search(r'>([^<]+)<', html_content)
    content = content.group(1) if content else ''
    
    words = content.split()
    word_count = len(words)
    sorted_content = ','.join(sorted(words))
    word_freq = Counter(words)
    complexity = sum(freq * (freq / len(words)) for word, freq in word_freq.items())
    
    numbers = re.findall(r'\d+', content)
    number_count = len(numbers)
    
    return f"{doc_type}, word count: {word_count}, complexity: {complexity:.2f}, sorted content: '{sorted_content}', number count: {number_count}"

def process_non_html(input_str, evaluated):
    words = input_str.split()
    word_count = len(words)
    sorted_content = ','.join(sorted(words))
    word_freq = Counter(words)
    complexity = sum(freq * (freq / len(words)) for word, freq in word_freq.items())
    
    numbers = re.findall(r'\d+', input_str)
    number_count = len(numbers)
    
    return f"{sorted_content}, length: {len(input_str)}, word count: {word_count}, complexity: {complexity:.2f}, number count: {number_count}, evaluated: {evaluated}"