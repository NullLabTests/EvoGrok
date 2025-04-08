import re

def tentacle(input_data):
    # Check if the input is a URL
    url_pattern = re.compile(r'^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$', re.IGNORECASE)
    if isinstance(input_data, str) and url_pattern.match(input_data):
        # Check if the URL contains specific keywords
        if 'data' in input_data.lower():
            return "data-related url detected"
        elif 'math' in input_data.lower():
            return "math-related url detected"
        elif 'text' in input_data.lower():
            return "text-related url detected"
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
            # For strings, check if it's a URL or HTML document
            if url_pattern.match(result):
                return "url detected in evaluated string"
            elif result.strip().lower().startswith('<!doctype'):
                return "html document detected in evaluated string"
            else:
                # Process the string as text
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