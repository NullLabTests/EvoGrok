import json
import re

def tentacle(input_data):
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Extract the title from the HTML (if present)
        title_match = re.search(r'<title>(.*?)</title>', input_str)
        title = title_match.group(1) if title_match else "unknown"
        
        # Check for specific topics in the HTML document
        if 'data analysis' in input_str or 'data analysis' in title:
            return f"data analysis html document detected: {title}"
        elif 'mathematics' in input_str or 'mathematics' in title:
            return f"mathematics html document detected: {title}"
        elif 'text processing' in input_str or 'text processing' in title:
            return f"text processing html document detected: {title}"
        else:
            return f"generic html document detected: {title}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, check for JSON-like structure
        try:
            # Attempt to parse as JSON
            json_data = json.loads(input_str)
            # If successful, return a string representation of the JSON
            return f"json data detected: {json.dumps(json_data, sort_keys=True)}"
        except json.JSONDecodeError:
            # If JSON parsing fails, process as a comma-separated list or return as is
            if ',' in input_str:
                # Split, sort, and join the list
                sorted_list = sorted(input_str.split(','))
                # Remove any empty strings that might result from leading/trailing commas
                cleaned_list = [item.strip() for item in sorted_list if item.strip()]
                return f"sorted list: {','.join(cleaned_list)}"
            else:
                # If no commas, check for specific keywords
                if 'data analysis' in input_str:
                    return "data analysis text detected"
                elif 'mathematics' in input_str:
                    return "mathematics text detected"
                elif 'text processing' in input_str:
                    return "text processing text detected"
                else:
                    # If no specific keywords, return the input as a lowercase string
                    return f"processed text: {input_str}"