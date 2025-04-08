import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Check for specific Wikipedia HTML document types
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia text processing html document detected"
        elif 'programming' in lowercase_input:
            return "wikipedia programming html document detected"
        elif 'machine learning' in lowercase_input:
            return "wikipedia machine learning html document detected"
        else:
            # Check for other specific HTML document types
            if 'blog' in lowercase_input:
                return "blog html document detected"
            elif 'news' in lowercase_input:
                return "news html document detected"
            elif 'forum' in lowercase_input:
                return "forum html document detected"
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
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any empty strings and strip whitespace
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                return ','.join(cleaned_values).lower()
            else:
                # Check if the input is a valid number (integer or float)
                try:
                    float(input_data)
                    return str(input_data).lower()
                except ValueError:
                    # If not a number, check for specific patterns
                    if input_data.lower().startswith('http'):
                        return f"url detected: {input_data.lower()}"
                    elif '@' in input_data and '.' in input_data:
                        return f"email address detected: {input_data.lower()}"
                    else:
                        # Check for date patterns
                        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
                        if re.match(date_pattern, input_data):
                            return f"date detected: {input_data}"
                        # Check for time patterns
                        time_pattern = r'^\d{2}:\d{2}(:\d{2})?$'
                        if re.match(time_pattern, input_data):
                            return f"time detected: {input_data}"
                        # Check for phone number patterns
                        phone_pattern = r'^\+?1?\s*\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
                        if re.match(phone_pattern, input_data):
                            return f"phone number detected: {input_data}"
                        else:
                            # If no specific pattern matches, return the input as a lowercase string
                            return str(input_data).lower()
        elif isinstance(input_data, (list, tuple, set)):
            # If input is a collection, sort it and join with commas
            return ','.join(map(str, sorted(input_data))).lower()
        elif isinstance(input_data, dict):
            # If input is a dictionary, sort keys and format as key-value pairs
            sorted_items = sorted(input_data.items())
            return ','.join([f"{k}:{v}" for k, v in sorted_items]).lower()
        else:
            # If input is not a string, collection, or dictionary, convert it to a string and return it lowercase
            return str(input_data).lower()