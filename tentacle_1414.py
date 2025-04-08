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
            return 'wikipedia data analysis html document detected'
        elif 'mathematics' in input_data.lower():
            return 'wikipedia mathematics html document detected'
        elif 'text processing' in input_data.lower():
            return 'wikipedia text processing html document detected'
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
                # Determine the type of HTML document in the evaluated string
                if 'data analysis' in result.lower():
                    return 'wikipedia data analysis html document detected in evaluated string'
                elif 'mathematics' in result.lower():
                    return 'wikipedia mathematics html document detected in evaluated string'
                elif 'text processing' in result.lower():
                    return 'wikipedia text processing html document detected in evaluated string'
                else:
                    return "generic html document detected in evaluated string"
            else:
                # Process the string as text
                words = sorted(result.lower().split())
                processed_result = ','.join(words)
                return processed_result if len(words) > 1 else processed_result.replace(',', '')
        else:
            # For other types, convert to string, split into words, sort them, and join with commas
            words = sorted(str(result).lower().split())
            processed_result = ','.join(words)
            return processed_result if len(words) > 1 else processed_result.replace(',', '')
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        words = sorted(str(input_data).lower().split())
        processed_input = ','.join(words)
        return processed_input if len(words) > 1 else processed_input.replace(',', '')