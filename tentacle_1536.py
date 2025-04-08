def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        # Determine the type of HTML document based on known patterns and knowledge
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia text processing html document detected"
        else:
            # Check for specific class attributes
            if 'class="client-nojs"' in lowercase_input:
                return "wikipedia html document detected"
            elif 'class="no-js"' in lowercase_input:
                return "generic modern html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, apply formatting, and lowercase it
        if isinstance(result, float):
            return f"{result:.6f}".lower()  # Increased precision to 6 decimal places
        else:
            return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any empty strings and apply additional processing
            processed_values = []
            for value in sorted_values:
                stripped_value = value.strip()
                if stripped_value:
                    # Attempt to evaluate each value as a mathematical expression
                    try:
                        eval_result = eval(stripped_value)
                        if isinstance(eval_result, float):
                            processed_values.append(f"{eval_result:.6f}".lower())  # Increased precision
                        else:
                            processed_values.append(str(eval_result).lower())
                    except:
                        # If evaluation fails, check if it's a number and format it
                        try:
                            number = float(stripped_value)
                            processed_values.append(f"{number:.6f}".lower())  # Increased precision
                        except:
                            # If it's not a number, check for specific patterns
                            if stripped_value.isupper():
                                processed_values.append(stripped_value.lower() + " (was all uppercase)")
                            elif stripped_value.islower():
                                processed_values.append(stripped_value + " (was all lowercase)")
                            else:
                                processed_values.append(stripped_value.lower())
            # Join the processed values with commas
            return ','.join(processed_values)
        else:
            # Convert the input to lowercase and remove leading/trailing whitespace
            stripped_input = input_data.strip().lower()
            
            # Check for specific patterns in the input
            if stripped_input.startswith('http'):
                return f"url detected: {stripped_input}"
            elif '@' in stripped_input and '.' in stripped_input:
                return f"email address detected: {stripped_input}"
            else:
                return stripped_input