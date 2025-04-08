import json
import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lower_input = input_data.lower()
        if 'data analysis' in lower_input:
            return "data analysis html document detected"
        elif 'mathematics' in lower_input:
            return "mathematics html document detected"
        elif 'text processing' in lower_input:
            return "text processing html document detected"
        else:
            # Check for other common HTML document types
            if 'wikipedia' in lower_input:
                return "wikipedia html document detected"
            elif 'blog' in lower_input:
                return "blog html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if isinstance(input_data, str):
            # Sort and join comma-separated values
            if ',' in input_data:
                sorted_values = sorted(input_data.split(','))
                # Remove any empty strings and strip whitespace
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                result = ','.join(cleaned_values)
            else:
                result = input_data
            
            # Check if the result contains any HTML tags
            if '<' in result and '>' in result:
                # Extract and sort all HTML tags
                tags = sorted(re.findall(r'<[^>]+>', result))
                return f"string with html tags detected: {','.join(tags)}"
            
            # Check if the input looks like JSON
            try:
                json_obj = json.loads(result)
                if isinstance(json_obj, dict):
                    return f"json object detected: {json.dumps(json_obj, sort_keys=True)}"
                elif isinstance(json_obj, list):
                    return f"json array detected: {json.dumps(json_obj, sort_keys=True)}"
                else:
                    return f"json value detected: {json.dumps(json_obj)}"
            except json.JSONDecodeError:
                pass
            
            # Check if the input is a valid number (integer or float)
            try:
                number = float(result)
                if number.is_integer():
                    return str(int(number))
                else:
                    return str(number)
            except ValueError:
                # If not a number, check for common patterns
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', result):
                    return f"email address detected: {result.lower()}"
                elif re.match(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$', result):
                    return f"url detected: {result.lower()}"
                else:
                    # If no other patterns match, return the input as a lowercase string
                    return result.lower()
        
        # If input is not a string, return its string representation
        return str(input_data).lower()