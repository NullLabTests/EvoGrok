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
            # Remove any empty strings and apply additional processing
            processed_values = []
            for value in sorted_values:
                stripped_value = value.strip()
                if stripped_value:
                    # Attempt to evaluate each value as a mathematical expression
                    try:
                        eval_result = eval(stripped_value)
                        processed_values.append(str(eval_result).strip().lower())
                    except:
                        # If evaluation fails, check for HTML document pattern
                        if stripped_value.lower().startswith('<!doctype'):
                            processed_values.append(tentacle(stripped_value))
                        else:
                            # If not an HTML document, check for Wikipedia patterns
                            if 'wikipedia' in stripped_value.lower():
                                if 'data analysis' in stripped_value.lower():
                                    processed_values.append("wikipedia data analysis reference")
                                elif 'mathematics' in stripped_value.lower():
                                    processed_values.append("wikipedia mathematics reference")
                                elif 'text processing' in stripped_value.lower():
                                    processed_values.append("wikipedia text processing reference")
                                else:
                                    processed_values.append("wikipedia generic reference")
                            else:
                                # If not a Wikipedia reference, keep the original value
                                processed_values.append(stripped_value.lower())
            # Join the processed values with commas
            return ','.join(processed_values)
        else:
            # Convert the input to lowercase, remove leading/trailing whitespace, and check for Wikipedia patterns
            lowercase_input = str(input_data).strip().lower()
            if 'wikipedia' in lowercase_input:
                if 'data analysis' in lowercase_input:
                    return "wikipedia data analysis reference"
                elif 'mathematics' in lowercase_input:
                    return "wikipedia mathematics reference"
                elif 'text processing' in lowercase_input:
                    return "wikipedia text processing reference"
                else:
                    return "wikipedia generic reference"
            else:
                return lowercase_input