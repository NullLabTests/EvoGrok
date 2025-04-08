def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        lowercase_input = input_data.lower()
        
        if 'data analysis' in lowercase_input:
            return "data analysis wikipedia page detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics wikipedia page detected"
        elif 'text processing' in lowercase_input:
            return "text processing wikipedia page detected"
        else:
            return "generic wikipedia page detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except (SyntaxError, NameError, TypeError):
        # If evaluation fails due to syntax, name, or type issues, process the input based on its content
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join the items if it's a comma-separated list
                sorted_items = sorted(input_data.split(','))
                return f"sorted list: {','.join(item.strip().lower() for item in sorted_items)}"
            elif input_data.isdigit():
                # If it's a number, return it as a string with a descriptive prefix
                return f"number detected: {input_data}"
            elif input_data.replace(' ', '').isalpha():
                # If it's a word (ignoring spaces), return it capitalized and with a prefix
                return f"word detected: {input_data.title()}"
            else:
                # For any other string input, return it as a lowercase string with a prefix
                return f"other string input detected: {input_data.lower()}"
        elif isinstance(input_data, (int, float, bool)):
            # Handle numeric and boolean inputs
            return f"numeric or boolean input detected: {str(input_data).lower()}"
        elif isinstance(input_data, list):
            # Handle list inputs
            return f"list input detected: {','.join(str(item).lower() for item in input_data)}"
        else:
            # For any other type of input, return its type and string representation
            return f"other input type detected: {type(input_data).__name__} - {str(input_data).lower()}"