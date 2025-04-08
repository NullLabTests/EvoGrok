def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on its content
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # If no specific type is detected, check for other keywords
            if 'wikipedia' in lowercase_input:
                return "wikipedia html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Check if all values are numeric
            if all(value.strip().replace('.', '', 1).isdigit() for value in sorted_values):
                # If numeric, calculate and return the average
                numeric_values = [float(value.strip()) for value in sorted_values]
                average = sum(numeric_values) / len(numeric_values)
                return f"average: {average:.2f}"
            else:
                # If not numeric, return sorted and joined values
                return ','.join(sorted_values)
        else:
            # If no comma, check for specific patterns
            if input_data.strip().isdigit():
                # If it's a single number, return its square
                number = int(input_data.strip())
                return f"square: {number * number}"
            else:
                # Return the input as a lowercase string
                return str(input_data).lower()