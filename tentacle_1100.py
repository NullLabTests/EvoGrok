import json
import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected"
        else:
            # Extract the title if possible
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip().lower()
                # Check for specific keywords in the title
                if 'data' in title:
                    return f"data-related html document detected: {title}"
                elif 'math' in title or 'equation' in title:
                    return f"math-related html document detected: {title}"
                elif 'text' in title or 'processing' in title:
                    return f"text processing html document detected: {title}"
                else:
                    return f"html document detected: {title}"
            else:
                # If no title found, extract the first h1 tag content
                h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', input_data, re.IGNORECASE | re.DOTALL)
                if h1_match:
                    h1_content = h1_match.group(1).strip().lower()
                    return f"html document detected: {h1_content}"
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
                sorted_values = sorted(input_data.split(','))
                # Remove any leading/trailing whitespace from each value
                cleaned_values = [value.strip() for value in sorted_values]
                return ','.join(cleaned_values)
            else:
                # Attempt to parse as JSON
                try:
                    json_data = json.loads(input_data)
                    # If successful, return a string representation of the JSON structure
                    return str(json_data).lower()
                except json.JSONDecodeError:
                    # If JSON parsing fails, return the input as a lowercase string
                    return str(input_data).lower()
        else:
            # For non-string inputs, convert to string and lowercase
            return str(input_data).lower()