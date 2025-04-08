import json

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis wikipedia html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics wikipedia html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing wikipedia html document detected"
        elif 'wikipedia' in lowercase_input:
            return "generic wikipedia html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string or other type
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any empty strings that might result from leading/trailing commas
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                return ','.join(cleaned_values)
            else:
                # Check if the input is a string of words
                if input_data.strip():
                    # Split the input into words, sort them, and join them back
                    words = input_data.lower().split()
                    return ' '.join(sorted(words))
                else:
                    # Return an empty string for empty input
                    return ''
        elif isinstance(input_data, (dict, list)):
            # Handle JSON-like input
            try:
                return json.dumps(input_data, sort_keys=True).lower()
            except TypeError:
                # If JSON serialization fails, convert to string and lowercase
                return str(input_data).lower()
        else:
            # For other non-string inputs, convert to lowercase string
            return str(input_data).lower()