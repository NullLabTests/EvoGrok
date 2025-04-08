import re

def tentacle(input_data):
    # Convert input to string and strip whitespace
    input_str = str(input_data).strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.lower().startswith('<!doctype'):
        # Check for specific Wikipedia pages mentioned in the knowledge
        if re.search(r'<title>Data analysis - Wikipedia</title>', input_str, re.IGNORECASE):
            return "wikipedia data analysis page detected"
        elif re.search(r'<title>Mathematics - Wikipedia</title>', input_str, re.IGNORECASE):
            return "wikipedia mathematics page detected"
        elif re.search(r'<title>Text processing - Wikipedia</title>', input_str, re.IGNORECASE):
            return "wikipedia text processing page detected"
        else:
            return "html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_str)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, sort the words in the input
        words = input_str.split()
        sorted_words = sorted(words)
        return ' '.join(sorted_words).lower()