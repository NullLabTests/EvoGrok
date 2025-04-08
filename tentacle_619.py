import json
import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if re.search(r'data\s+analysis', input_data, re.IGNORECASE):
            return "data analysis html document detected"
        elif re.search(r'mathematics', input_data, re.IGNORECASE):
            return "mathematics html document detected"
        elif re.search(r'text\s+processing', input_data, re.IGNORECASE):
            return "text processing html document detected"
        else:
            # Extract the title from the HTML if possible
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                return f"html document detected: {title_match.group(1).strip().lower()}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string or JSON-like structure
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                return ','.join(sorted(input_data.split(',')))
            else:
                # Attempt to parse as JSON
                try:
                    json_data = json.loads(input_data)
                    # If successful, return a string representation of the JSON structure
                    return str(json_data).lower()
                except json.JSONDecodeError:
                    # If JSON parsing fails, check for potential HTML content
                    if '<' in input_data and '>' in input_data:
                        # Extract text content from HTML-like input
                        text_content = re.sub(r'<[^>]+>', '', input_data)
                        return text_content.strip().lower()
                    else:
                        # If no HTML-like content, return the input as a lowercase string
                        return input_data.lower()
        else:
            # For non-string inputs, convert to string and lowercase
            return str(input_data).lower()