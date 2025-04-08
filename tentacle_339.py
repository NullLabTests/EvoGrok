import json

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
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string or JSON
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values (from Parent2)
                return ','.join(sorted(input_data.split(',')))
            else:
                # Attempt to parse as JSON
                try:
                    json_data = json.loads(input_data)
                    # If successful, return a string representation of the JSON
                    return str(json_data).lower()
                except json.JSONDecodeError:
                    # If JSON parsing fails, return the input as a lowercase string (from Parent1)
                    return str(input_data).lower()
        else:
            # For non-string inputs, convert to string and lowercase
            return str(input_data).lower()