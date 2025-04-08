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
        # If evaluation fails, process the input as a string or JSON-like data
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any empty strings that might result from leading/trailing commas
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                return ','.join(cleaned_values)
            elif input_data.strip().startswith('{') and input_data.strip().endswith('}'):
                # Attempt to parse as JSON
                try:
                    json_data = json.loads(input_data)
                    return json.dumps(json_data, sort_keys=True, indent=2).lower()
                except json.JSONDecodeError:
                    # If JSON parsing fails, fall back to string processing
                    pass
            
            # Convert the input to lowercase and remove any leading/trailing whitespace
            return input_data.strip().lower()
        else:
            # For non-string inputs, convert to string and lowercase
            return str(input_data).lower()