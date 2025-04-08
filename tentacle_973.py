def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lower_input = input_data.lower()
        if 'data analysis' in lower_input:
            return "data analysis html document detected"
        elif 'mathematics' in lower_input:
            return "mathematics html document detected"
        elif 'text processing' in lower_input:
            return "text processing html document detected"
        elif 'wikipedia' in lower_input:
            return "wikipedia html document detected"
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
            # Remove any empty strings and apply additional processing
            processed_values = []
            for value in sorted_values:
                stripped_value = value.strip()
                if stripped_value:
                    # Attempt to evaluate each value as a mathematical expression
                    try:
                        eval_result = eval(stripped_value)
                        processed_values.append(str(eval_result).lower())
                    except:
                        # If evaluation fails, check if it's a number
                        try:
                            float(stripped_value)
                            processed_values.append(stripped_value.lower())
                        except:
                            # If it's not a number, reverse the string
                            processed_values.append(stripped_value[::-1].lower())
            # Join the processed values with commas
            return ','.join(processed_values)
        else:
            # Convert the input to lowercase and remove leading/trailing whitespace
            return input_data.strip().lower()