def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # If no specific type is detected, check for other keywords
            keywords = ['wikipedia', 'html', 'document']
            detected_keywords = [kw for kw in keywords if kw in lowercase_input]
            if detected_keywords:
                return f"html document with {', '.join(detected_keywords)} detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in str(input_data):
            # Sort and join comma-separated values
            sorted_values = sorted(str(input_data).split(','))
            # Remove any empty strings and strip whitespace
            cleaned_values = [value.strip() for value in sorted_values if value.strip()]
            # Check if all values are numbers
            if all(value.replace('.', '').isdigit() for value in cleaned_values):
                # If all values are numbers, return their sum
                return str(sum(float(value) for value in cleaned_values)).lower()
            else:
                # If not all values are numbers, return the sorted and cleaned list
                return ','.join(cleaned_values)
        else:
            # Check if the input is a valid number (integer or float)
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # If not a number, check for common text patterns
                lowercase_input = str(input_data).lower()
                if 'http' in lowercase_input or 'www' in lowercase_input:
                    return "url detected"
                elif '@' in lowercase_input and '.' in lowercase_input:
                    return "email address detected"
                else:
                    # If no special patterns are detected, return the input as a lowercase string
                    return lowercase_input