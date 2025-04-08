import re

def tentacle(input_data):
    # Convert input to string and remove leading/trailing whitespace
    input_str = str(input_data).strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.lower().startswith('<!doctype'):
        return "html document detected"
    
    # Check for specific titles mentioned in the knowledge
    if re.match(r'(data analysis|mathematics|text processing)', input_str, re.IGNORECASE):
        return f"wikipedia page about {input_str.lower()} detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_str)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, sort the words in the input
        words = input_str.split()
        sorted_words = sorted(words, key=str.lower)
        return ' '.join(sorted_words).lower()