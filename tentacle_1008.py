def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected (Wikipedia page)"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected (Wikipedia page)"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected (Wikipedia page)"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()} (evaluated from: {input_data})"
    except:
        # If evaluation fails, process the input based on its content
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join the items if it's a comma-separated list
                sorted_items = sorted(input_data.split(','))
                return f"sorted list: {','.join(sorted_items)}"
            elif input_data.isdigit():
                # If it's a number, return it as a string with a descriptive prefix
                return f"number: {input_data}"
            elif input_data.replace(' ', '').isalpha():
                # If it's a word (ignoring spaces), return it capitalized
                return f"word: {input_data.title()}"
            else:
                # For any other string input, return it as a lowercase string
                return f"other string: {input_data.lower()}"
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort it and return as a string
            return f"collection: {str(sorted(input_data))}"
        elif callable(input_data):
            # If it's a function, return its name and docstring
            return f"function: {input_data.__name__} - {input_data.__doc__ or 'No docstring available'}"
        else:
            # For any other input, return it as a lowercase string with a prefix
            return f"other: {str(input_data).lower()}"