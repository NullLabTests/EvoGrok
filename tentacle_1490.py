import json
import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis page detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics page detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia text processing page detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any empty strings that might result from leading/trailing commas
            cleaned_values = [value.strip() for value in sorted_values if value.strip()]
            return ','.join(cleaned_values)
        else:
            # Check if the input is a valid number (integer or float)
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # If not a number, check if it's JSON-like
                try:
                    json_data = json.loads(input_data)
                    # If it's valid JSON, return a string representation
                    return str(json_data).lower()
                except json.JSONDecodeError:
                    # If not JSON, check for specific keywords
                    lowercase_input = input_data.lower()
                    if 'data' in lowercase_input and 'analysis' in lowercase_input:
                        return "data analysis text detected"
                    elif 'mathematics' in lowercase_input:
                        return "mathematics text detected"
                    elif 'text' in lowercase_input and 'processing' in lowercase_input:
                        return "text processing text detected"
                    else:
                        # Check for potential email addresses
                        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                        if re.search(email_pattern, input_data):
                            return "email address detected"
                        
                        # Check for potential URLs
                        url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
                        if re.search(url_pattern, input_data):
                            return "url detected"
                        
                        # If no specific patterns or keywords, return the input as a lowercase string
                        return str(input_data).lower()