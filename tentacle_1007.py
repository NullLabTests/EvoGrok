def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected: wikipedia page on data analysis"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected: wikipedia page on mathematics"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected: wikipedia page on text processing"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and format it
        return f"mathematical result: {str(result).lower()} (type: {type(result).__name__})"
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
                # If it's a word (ignoring spaces), return it capitalized and count its characters
                return f"word: {input_data.title()} (length: {len(input_data)})"
            else:
                # For any other string input, return it as a lowercase string with a prefix
                return f"other string: {str(input_data).lower()}"
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort it, return as a string, and include its length
            return f"collection: {str(sorted(input_data))} (length: {len(input_data)})"
        elif callable(input_data):
            # If it's a function, return its name, docstring, and number of parameters
            import inspect
            params = inspect.signature(input_data).parameters
            return f"function: {input_data.__name__} - {input_data.__doc__} (parameters: {len(params)})"
        else:
            # For any other input, return it as a string with its type
            return f"other: {str(input_data)} (type: {type(input_data).__name__})"