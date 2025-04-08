def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected"
        elif 'text processing' in input_data.lower():
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
        if isinstance(input_data, str):
            # Convert the input to lowercase and remove leading/trailing whitespace
            processed_input = input_data.strip().lower()
            
            if ',' in processed_input:
                # Sort and join comma-separated values
                sorted_values = sorted(processed_input.split(','))
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
                            # If evaluation fails, keep the original value
                            processed_values.append(stripped_value)
                # Join the processed values with commas
                return ','.join(processed_values)
            else:
                # Check for specific patterns in the input
                if 'data analysis' in processed_input:
                    return "data analysis text detected"
                elif 'mathematics' in processed_input:
                    return "mathematics text detected"
                elif 'text processing' in processed_input:
                    return "text processing text detected"
                else:
                    return processed_input
        else:
            # If input is not a string, convert it to a string and lowercase it
            return str(input_data).lower()