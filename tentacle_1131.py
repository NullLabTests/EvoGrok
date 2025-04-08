import re

def tentacle(input_data):
    # Check if the input is a URL
    url_pattern = re.compile(r'^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$', re.IGNORECASE)
    if isinstance(input_data, str) and url_pattern.match(input_data):
        # If it's a URL, check if it's related to known topics
        if 'data' in input_data.lower():
            return "data analysis url detected"
        elif 'math' in input_data.lower():
            return "mathematics url detected"
        elif 'text' in input_data.lower():
            return "text processing url detected"
        else:
            return "generic url detected"

    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return 'data analysis html document detected'
        elif 'mathematics' in input_data.lower():
            return 'mathematics html document detected'
        elif 'text processing' in input_data.lower():
            return 'text processing html document detected'
        else:
            return 'generic html document detected'

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # For numbers, return the result as a string, lowercase
            return str(result).lower()
        elif isinstance(result, str):
            # For strings, check if they match known topics
            if 'data' in result.lower():
                return "data analysis string detected"
            elif 'math' in result.lower():
                return "mathematics string detected"
            elif 'text' in result.lower():
                return "text processing string detected"
            else:
                # If not a known topic, process as in parent2
                processed_result = ','.join(sorted(result.lower().split()))
                return processed_result if ',' in processed_result else processed_result.replace(',', '')
        else:
            # For other types, convert to string, split into words, sort them, and join with commas
            processed_result = ','.join(sorted(str(result).lower().split()))
            # If the result is a single word, return it as is; otherwise, return the sorted, comma-separated list
            return processed_result if ',' in processed_result else processed_result.replace(',', '')
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        processed_input = ','.join(sorted(str(input_data).lower().split()))
        # If the result is a single word, return it as is; otherwise, return the sorted, comma-separated list
        return processed_input if ',' in processed_input else processed_input.replace(',', '')