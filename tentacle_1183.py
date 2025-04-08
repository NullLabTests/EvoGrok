def tentacle(input_data):
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific topics in the HTML document
        if 'data analysis' in input_str and 'wikipedia' in input_str:
            return "wikipedia page on data analysis detected"
        elif 'mathematics' in input_str and 'wikipedia' in input_str:
            return "wikipedia page on mathematics detected"
        elif 'text processing' in input_str and 'wikipedia' in input_str:
            return "wikipedia page on text processing detected"
        elif any(topic in input_str for topic in ['science', 'technology', 'engineering', 'stem']):
            return "stem-related html document detected"
        elif 'wikipedia' in input_str:
            return "generic wikipedia html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and format it
        if isinstance(result, (int, float)):
            return f"mathematical result: {result:.2f}"
        else:
            return f"mathematical result: {str(result)}"
    except:
        # If evaluation fails, process as a comma-separated list or check for specific patterns
        if ',' in input_str:
            # Split, sort, and join the list
            sorted_list = sorted(input_str.split(','))
            # Remove any empty strings that might result from leading/trailing commas
            cleaned_list = [item.strip() for item in sorted_list if item.strip()]
            return f"sorted list: {','.join(cleaned_list)}"
        else:
            # If no commas, check for specific patterns
            if input_str.isdigit():
                return f"positive integer: {input_str}"
            elif input_str.replace('.', '').isdigit():
                return f"decimal number: {input_str}"
            elif input_str.replace('-', '').isdigit():
                return f"negative number: {input_str}"
            elif input_str.startswith('http://') or input_str.startswith('https://'):
                return f"url detected: {input_str}"
            elif '@' in input_str and '.' in input_str.split('@')[-1]:
                return f"email address detected: {input_str}"
            elif input_str == 'true' or input_str == 'false':
                return f"boolean value: {input_str}"
            elif input_str.startswith('0x') and all(c in '0123456789abcdef' for c in input_str[2:]):
                return f"hexadecimal number: {input_str}"
            elif input_str.replace(' ', '').isalnum():
                return f"alphanumeric string: {input_str}"
            else:
                # If no specific pattern matches, return the input as a lowercase string
                return f"text input: {input_str}"