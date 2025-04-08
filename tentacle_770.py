def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # Attempt to extract the title from the HTML
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                return f"html document detected: {title_match.group(1).strip().lower()}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input based on its content
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join the items if it's a comma-separated list
                sorted_items = sorted(input_data.split(','))
                return f"sorted list: {','.join(sorted_items)}"
            elif input_data.isdigit():
                # If it's a number, return it as a string with a descriptive prefix
                return f"number detected: {input_data}"
            elif input_data.replace(' ', '').isalpha():
                # If it's a word (ignoring spaces), return it capitalized and with a prefix
                return f"word detected: {input_data.title()}"
            else:
                # For any other input, return it as a lowercase string with a prefix
                return f"other input detected: {str(input_data).lower()}"
        else:
            # If the input is not a string, convert it to a string and return it
            return f"non-string input detected: {str(input_data)}"