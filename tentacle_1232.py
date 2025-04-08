import json

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and remove leading/trailing whitespace
        return str(result).strip().lower()
    except:
        # If evaluation fails, process the input as a string
        input_str = str(input_data)
        
        # Check if the input looks like a JSON structure
        if input_str.strip().startswith('{') and input_str.strip().endswith('}'):
            try:
                # Parse the JSON and extract keys
                json_data = json.loads(input_str)
                keys = list(json_data.keys())
                # Sort keys, convert to lowercase, and join with commas
                return ','.join(sorted([str(key).lower() for key in keys]))
            except json.JSONDecodeError:
                # If JSON parsing fails, fall through to string processing
                pass
        
        # Process comma-separated values if present
        if ',' in input_str:
            # Sort and join comma-separated values
            sorted_values = sorted(input_str.split(','))
            # Remove any empty strings, strip whitespace from each value, and convert to lowercase
            cleaned_values = [value.strip().lower() for value in sorted_values if value.strip()]
            # Join the cleaned values with commas and remove leading/trailing whitespace
            return ','.join(cleaned_values).strip()
        else:
            # Convert the input to lowercase and remove leading/trailing whitespace
            return input_str.strip().lower()