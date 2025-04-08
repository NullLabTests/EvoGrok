def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on its content
        lowercase_input = input_data.lower()
        
        # Check for specific Wikipedia page types
        if 'data analysis' in lowercase_input:
            return "data analysis wikipedia page detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics wikipedia page detected"
        elif 'text processing' in lowercase_input:
            return "text processing wikipedia page detected"
        else:
            # If no specific type is detected, check for other keywords
            if 'wikipedia' in lowercase_input:
                return "generic wikipedia page detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # If evaluation succeeds, return the result and its square
        square = result ** 2
        return f"result: {result:.2f}, square: {square:.2f}"
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            
            # Check if all values are numeric
            if all(value.strip().replace('.', '', 1).isdigit() for value in sorted_values):
                # If numeric, calculate and return statistics
                numeric_values = [float(value.strip()) for value in sorted_values]
                average = sum(numeric_values) / len(numeric_values)
                minimum = min(numeric_values)
                maximum = max(numeric_values)
                return f"statistics: average={average:.2f}, min={minimum:.2f}, max={maximum:.2f}"
            else:
                # If not numeric, return sorted and joined values in lowercase
                return ','.join(sorted_values).lower()
        else:
            # If no comma, check for specific patterns
            if input_data.strip().replace('.', '', 1).isdigit():
                # If it's a single number, return its square and cube
                number = float(input_data.strip())
                square = number ** 2
                cube = number ** 3
                return f"number: {number:.2f}, square: {square:.2f}, cube: {cube:.2f}"
            else:
                # Return the input as a lowercase string
                return str(input_data).lower()