import json
import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document
        document_type = 'unknown'
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
        
        # Extract and process the content of the HTML document
        content = input_data.lower().split('>', 1)[1].split('<', 1)[0].strip()
        content_words = sorted(content.split())
        
        # Extract title if present
        title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
        title = title_match.group(1).strip().lower() if title_match else 'no title found'
        
        # Return a sorted, comma-separated list of detected elements, content words, and title
        return ','.join(sorted(['html document', document_type, title] + content_words))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it into words, sort them, and join with commas
        return ','.join(sorted(str(result).lower().split()))
    except:
        pass

    try:
        # Attempt to parse the input as JSON
        json_data = json.loads(input_data)
        # Flatten the JSON structure and convert to a list of strings
        flat_data = []
        def flatten_json(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    flat_data.append(key.lower())
                    flatten_json(value)
            elif isinstance(data, list):
                for item in data:
                    flatten_json(item)
            else:
                flat_data.append(str(data).lower())
        flatten_json(json_data)
        # Return a sorted, comma-separated list of flattened JSON data
        return ','.join(sorted(flat_data))
    except:
        pass

    try:
        # Attempt to parse the input as a mathematical expression with variables
        # Define common mathematical constants and functions
        math_env = {
            'pi': 3.141592653589793,
            'e': 2.718281828459045,
            'sin': lambda x: x,  # Placeholder for actual implementation
            'cos': lambda x: x,  # Placeholder for actual implementation
            'tan': lambda x: x,  # Placeholder for actual implementation
        }
        result = eval(input_data, math_env)
        # Convert the result to a string, split it into words, sort them, and join with commas
        return ','.join(sorted(str(result).lower().split()))
    except:
        pass

    # If all else fails, process the input as text
    # Convert to lowercase, split into words, sort them, and join with commas
    return ','.join(sorted(str(input_data).lower().split()))