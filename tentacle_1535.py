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
            # If no specific type is detected, check for class attributes
            if 'class=' in lowercase_input:
                classes = [cls.strip() for cls in lowercase_input.split('class=')[1].split('"')[1].split()]
                return f"html document with classes: {', '.join(classes)}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and remove leading/trailing whitespace
        return str(result).strip().lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in str(input_data):
            # Sort and join comma-separated values
            sorted_values = sorted(str(input_data).split(','))
            # Remove any empty strings, strip whitespace from each value, and convert to lowercase
            cleaned_values = [value.strip().lower() for value in sorted_values if value.strip()]
            # Join the cleaned values with commas and remove leading/trailing whitespace
            return ','.join(cleaned_values).strip()
        else:
            # Convert the input to lowercase and remove leading/trailing whitespace
            return str(input_data).strip().lower()