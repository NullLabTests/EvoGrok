import json

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input and 'wikipedia' in lowercase_input:
            return 'wikipedia data analysis html document detected'
        elif 'mathematics' in lowercase_input and 'wikipedia' in lowercase_input:
            return 'wikipedia mathematics html document detected'
        elif 'text processing' in lowercase_input and 'wikipedia' in lowercase_input:
            return 'wikipedia text processing html document detected'
        else:
            return 'generic html document detected'
    
    # Check if the input looks like JSON
    elif isinstance(input_data, str) and input_data.strip().startswith(('{', '[')):
        try:
            parsed_json = json.loads(input_data)
            if isinstance(parsed_json, dict):
                return f"json object detected: {', '.join(sorted(parsed_json.keys()))}"
            elif isinstance(parsed_json, list):
                return f"json array detected: length {len(parsed_json)}"
        except json.JSONDecodeError:
            pass  # If JSON parsing fails, continue to the next check

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # If the result is a number, return it as is
        if isinstance(result, (int, float)):
            return str(result).lower()
        else:
            # Convert the result to a string, split it into words, sort them, and join with commas
            sorted_words = ','.join(sorted(str(result).lower().split()))
            return sorted_words
    except Exception as e:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        sorted_words = ','.join(sorted(str(input_data).lower().split()))
        
        # Check if the sorted words contain specific keywords
        if 'data' in sorted_words and 'analysis' in sorted_words:
            return f'{sorted_words} - related to data analysis'
        elif 'mathematics' in sorted_words:
            return f'{sorted_words} - related to mathematics'
        elif 'text' in sorted_words and 'processing' in sorted_words:
            return f'{sorted_words} - related to text processing'
        else:
            # If no specific keywords are found, return the sorted words with error information
            return f'{sorted_words} - error in processing: {str(e)}'