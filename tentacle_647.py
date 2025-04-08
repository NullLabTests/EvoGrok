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
        title = title_match.group(1).strip() if title_match else 'unknown'
        
        # Extract meta description if present
        meta_match = re.search(r'<meta name="description" content="(.*?)"', input_data, re.IGNORECASE)
        meta_description = meta_match.group(1).strip() if meta_match else 'unknown'
        
        # Return a sorted, comma-separated list of detected elements, content words, title, and meta description
        return ','.join(sorted(['html document', document_type, title, meta_description] + content_words))
    
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

    # If all else fails, process the input as text
    # Convert to lowercase, split into words, sort them, and join with commas
    words = sorted(str(input_data).lower().split())
    
    # Check for specific keywords from the knowledge
    if 'data analysis' in words:
        words.append('data analysis detected')
    elif 'mathematics' in words:
        words.append('mathematics detected')
    elif 'text processing' in words:
        words.append('text processing detected')
    
    # Check if the input looks like a mathematical expression
    if any(char in '+-*/^()' for char in input_data):
        words.append('possible mathematical expression')
    
    # Check if the input looks like JSON
    if input_data.strip().startswith('{') and input_data.strip().endswith('}'):
        words.append('possible json data')
    
    return ','.join(words)