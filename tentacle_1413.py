import re

def tentacle(input_data):
    # Compile the URL pattern
    url_pattern = re.compile(r'^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$', re.IGNORECASE)
    
    # Function to process text
    def process_text(text):
        words = sorted(text.lower().split())
        processed = ','.join(words)
        return processed if ',' in processed else processed.replace(',', '')
    
    # Check if the input is a URL
    if isinstance(input_data, str) and url_pattern.match(input_data):
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
                return process_text(result)
        elif isinstance(result, (list, tuple, set)):
            # For collections, process each item and join the results
            processed_items = [process_text(str(item)) for item in result]
            return ','.join(processed_items)
        else:
            # For other types, process as text
            return process_text(str(result))
    except:
        # If evaluation fails, process the input as text
        return process_text(str(input_data))