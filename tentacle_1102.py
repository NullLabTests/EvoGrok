import re
import json
import math

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia text processing html document detected"
        elif 'lang="en"' in lowercase_input:
            return "english language html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        # Use a safe_eval function to prevent code injection
        result = safe_eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, check for JSON-like input
        try:
            # Attempt to parse as JSON
            json_data = json.loads(input_data)
            # If successful, return a string representation of the JSON
            return json.dumps(json_data, sort_keys=True, indent=2).lower()
        except json.JSONDecodeError:
            # If JSON parsing fails, process the input as text
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove extra whitespace from each value
                cleaned_values = [re.sub(r'\s+', ' ', value).strip() for value in sorted_values]
                return ','.join(cleaned_values)
            else:
                # Convert to lowercase and remove extra whitespace
                cleaned_input = re.sub(r'\s+', ' ', input_data.lower()).strip()
                
                # Check for specific patterns in the cleaned input
                if cleaned_input.startswith('http://') or cleaned_input.startswith('https://'):
                    return f"url detected: {cleaned_input}"
                elif '@' in cleaned_input and '.' in cleaned_input.split('@')[-1]:
                    return f"email address detected: {cleaned_input}"
                elif cleaned_input.isdigit():
                    return f"integer detected: {cleaned_input}"
                elif cleaned_input.replace('.', '').replace('-', '').isdigit():
                    return f"number detected: {cleaned_input}"
                elif all(c.isalpha() or c.isspace() for c in cleaned_input):
                    return f"text detected: {cleaned_input}"
                else:
                    return cleaned_input

def safe_eval(expression):
    # Define a safe environment for evaluation
    safe_dict = {
        'abs': abs,
        'max': max,
        'min': min,
        'pow': pow,
        'round': round,
        'sum': sum,
        'math': math
    }
    return eval(expression, {"__builtins__": None}, safe_dict)