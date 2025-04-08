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
            # If it's an HTML document but doesn't match specific patterns, check for other keywords
            if 'science' in lowercase_input:
                return "wikipedia science html document detected"
            elif 'history' in lowercase_input:
                return "wikipedia history html document detected"
            else:
                # Check for additional keywords from the knowledge
                if 'html5' in lowercase_input:
                    return "html5 document detected"
                else:
                    return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and remove whitespace
        result_str = str(result).strip().lower()
        
        # Check if the result is a number
        if isinstance(result, (int, float)):
            # Calculate and return the square root of the result
            import math
            square_root = math.sqrt(result)
            return f"{result_str} (square root: {square_root:.2f})"
        else:
            return result_str
    except:
        # If evaluation fails, process the input as a string
        if isinstance(input_data, str):
            # Check for comma-separated values
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any empty strings and strip whitespace from each value
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                # Join the cleaned values with commas and convert to lowercase
                result = ','.join(cleaned_values).lower()
                
                # Check if the result looks like a list of numbers
                if all(val.replace('.', '').replace('-', '').isdigit() for val in result.split(',')):
                    # If it's a list of numbers, calculate and return their average and standard deviation
                    numbers = [float(val) for val in result.split(',')]
                    average = sum(numbers) / len(numbers)
                    import statistics
                    std_dev = statistics.stdev(numbers)
                    return f"average of {result}: {average:.2f}, standard deviation: {std_dev:.2f}"
                else:
                    return result
            else:
                # Check for specific keywords related to the knowledge
                lowercase_input = input_data.lower()
                if 'data analysis' in lowercase_input:
                    return "data analysis related content detected"
                elif 'mathematics' in lowercase_input:
                    return "mathematics related content detected"
                elif 'text processing' in lowercase_input:
                    return "text processing related content detected"
                else:
                    # Convert the input to lowercase and remove any leading/trailing whitespace
                    return input_data.strip().lower()
        else:
            # For non-string inputs, convert to string and lowercase
            return str(input_data).lower()