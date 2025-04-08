def tentacle(input_data):
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific topics in the HTML document
        if 'data analysis' in input_str:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_str:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_str:
            return "wikipedia text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process as a comma-separated list or check for keywords
        if ',' in input_str:
            # Split, sort, and join the list
            sorted_list = sorted(input_str.split(','))
            # Remove any empty strings from the list
            cleaned_list = [item for item in sorted_list if item]
            return f"sorted list: {','.join(cleaned_list)}"
        else:
            # Check for specific keywords
            if 'data' in input_str and 'analysis' in input_str:
                return "data analysis text detected"
            elif 'mathematics' in input_str:
                return "mathematics text detected"
            elif 'text' in input_str and 'processing' in input_str:
                return "text processing text detected"
            else:
                # If no specific keywords, check for numeric content
                if any(char.isdigit() for char in input_str):
                    return "numeric content detected"
                else:
                    # If no numeric content, perform additional text analysis
                    word_count = len(input_str.split())
                    if word_count > 10:
                        return f"long text detected (word count: {word_count})"
                    else:
                        return f"short text detected (word count: {word_count})"