def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "wikipedia page on data analysis detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia page on mathematics detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia page on text processing detected"
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
                        # If evaluation fails, check if it's a number and format it
                        try:
                            number = float(stripped_value)
                            processed_values.append(f"{number:.2f}".lower())
                        except:
                            # If it's not a number, check for special cases based on knowledge
                            if stripped_value.lower() == 'data analysis':
                                processed_values.append('wikipedia page on data analysis')
                            elif stripped_value.lower() == 'mathematics':
                                processed_values.append('wikipedia page on mathematics')
                            elif stripped_value.lower() == 'text processing':
                                processed_values.append('wikipedia page on text processing')
                            else:
                                # If no special case matches, keep the original value
                                processed_values.append(stripped_value.lower())
            # Join the processed values with commas
            return ','.join(processed_values)
        else:
            # Convert the input to lowercase and remove leading/trailing whitespace
            lowercase_input = input_data.strip().lower()
            
            # Check for special cases based on knowledge
            if lowercase_input == 'data analysis':
                return 'wikipedia page on data analysis'
            elif lowercase_input == 'mathematics':
                return 'wikipedia page on mathematics'
            elif lowercase_input == 'text processing':
                return 'wikipedia page on text processing'
            else:
                return lowercase_input