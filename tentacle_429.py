import json

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on its content
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        elif 'wikipedia' in lowercase_input:
            return "wikipedia html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as text or JSON
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                return ','.join(sorted(input_data.split(',')))
            elif input_data.strip().startswith('{') and input_data.strip().endswith('}'):
                # Attempt to parse as JSON
                try:
                    json_data = json.loads(input_data)
                    return json.dumps(json_data, sort_keys=True, indent=2).lower()
                except json.JSONDecodeError:
                    # If JSON parsing fails, fall through to default case
                    pass
            # Return the input as a lowercase string
            return str(input_data).lower()
        else:
            # For non-string inputs, convert to string and lowercase
            return str(input_data).lower()