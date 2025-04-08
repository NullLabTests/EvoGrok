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
            # Remove any empty strings and apply additional processing
            processed_values = []
            for value in sorted_values:
                stripped_value = value.strip()
                if stripped_value:
                    try:
                        # If the value is a number, keep it as is
                        float(stripped_value)
                        processed_values.append(stripped_value)
                    except ValueError:
                        # If not a number, convert to lowercase
                        processed_values.append(stripped_value.lower())
            # Join the processed values
            return ','.join(processed_values)
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                return str(input_data)
            except ValueError:
                # If not a number, return the input as a lowercase string
                return str(input_data).lower()