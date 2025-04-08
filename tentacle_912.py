import json
import re

def tentacle(input_data):
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Use regex to extract the title from the HTML
        title_match = re.search(r'<title>(.*?)</title>', input_str)
        title = title_match.group(1) if title_match else "unknown"
        
        # Check for specific topics in the HTML document
        if 'data analysis' in title:
            return f"data analysis html document detected: {title}"
        elif 'mathematics' in title:
            return f"mathematics html document detected: {title}"
        elif 'text processing' in title:
            return f"text processing html document detected: {title}"
        else:
            return f"generic html document detected: {title}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, check for JSON-like input
        try:
            # Attempt to parse as JSON
            json_data = json.loads(input_str)
            # If successful, return a string representation of the JSON
            return json.dumps(json_data, sort_keys=True)
        except json.JSONDecodeError:
            # If JSON parsing fails, process as a comma-separated list or return as is
            if ',' in input_str:
                # Split, sort, and join the list
                sorted_list = sorted(input_str.split(','))
                # Remove any empty strings from the list
                cleaned_list = [item for item in sorted_list if item.strip()]
                return ','.join(cleaned_list)
            else:
                # If no commas, return the input as a lowercase string
                return input_str