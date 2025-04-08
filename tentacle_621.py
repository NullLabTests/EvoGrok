import json
import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "data analysis wikipedia html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics wikipedia html document detected"
        elif 'text processing' in input_data.lower():
            return "text processing wikipedia html document detected"
        else:
            # Extract the title from the HTML if possible
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                return f"wikipedia html document detected: {title_match.group(1).lower()}"
            else:
                return "generic wikipedia html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical expression evaluated: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string or JSON-like structure
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                return f"sorted comma-separated values: {','.join(sorted_values)}"
            else:
                # Attempt to parse as JSON
                try:
                    json_data = json.loads(input_data)
                    # If successful, return a string representation of the JSON structure
                    return f"json structure detected: {str(json_data).lower()}"
                except json.JSONDecodeError:
                    # If JSON parsing fails, check for potential mathematical expressions
                    if re.search(r'\d+[\+\-\*/]\d+', input_data):
                        return f"potential mathematical expression: {input_data.lower()}"
                    else:
                        # If no special processing applies, return the input as a lowercase string
                        return f"string input: {input_data.lower()}"
        else:
            # For non-string inputs, convert to string and lowercase
            return f"non-string input: {str(input_data).lower()}"