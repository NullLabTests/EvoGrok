import json

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        input_lower = input_data.lower()
        if 'data analysis' in input_lower:
            return "data analysis html document detected"
        elif 'mathematics' in input_lower:
            return "mathematics html document detected"
        elif 'text processing' in input_lower:
            return "text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string or other data type
        if isinstance(input_data, str):
            input_lower = input_data.strip().lower()
            
            # Check for comma-separated values
            if ',' in input_lower:
                # Sort and join comma-separated values
                sorted_values = sorted(input_lower.split(','))
                # Remove any empty strings
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                return ','.join(cleaned_values)
            
            # Check if the input is a valid number (integer or float)
            try:
                float(input_lower)
                return input_lower
            except ValueError:
                # If not a number, check for specific patterns
                if input_lower.startswith('http'):
                    return f"url detected: {input_data}"
                elif '@' in input_lower and '.' in input_lower:
                    return f"email address detected: {input_data}"
                elif len(input_data) > 100:
                    return f"long text detected: {len(input_data)} characters"
                elif input_lower.isalpha():
                    return f"alphabetic string detected: {input_data}"
                elif input_lower.isdigit():
                    return f"numeric string detected: {input_data}"
                elif input_lower.replace(' ', '').isalnum():
                    return f"alphanumeric string detected: {input_data}"
                else:
                    # If no specific pattern is detected, check for JSON-like structure
                    try:
                        json_data = json.loads(input_data)
                        return f"json-like structure detected: {json.dumps(json_data, indent=2)}"
                    except json.JSONDecodeError:
                        # If not JSON-like, return the input as a lowercase string
                        return input_lower
        else:
            # If input is not a string, check for JSON-like structure
            try:
                json_data = json.loads(str(input_data))
                return f"json-like structure detected: {json.dumps(json_data, indent=2)}"
            except json.JSONDecodeError:
                # If not JSON-like, return its string representation
                return str(input_data).lower()