def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical expression evaluated: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if isinstance(input_data, str):
            # Check if the input contains comma-separated values
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any leading/trailing whitespace from each value
                cleaned_values = [value.strip() for value in sorted_values]
                return f"sorted and cleaned values: {','.join(cleaned_values).lower()}"
            else:
                # If no commas, check for specific patterns
                if input_data.lower().startswith('http'):
                    return f"url detected: {input_data.lower()}"
                elif '@' in input_data and '.' in input_data:
                    return f"email address detected: {input_data.lower()}"
                else:
                    # Check for potential mathematical expressions
                    if any(char in '+-*/^%' for char in input_data):
                        return f"potential mathematical expression detected: {input_data.lower()}"
                    # Check for potential HTML tags
                    elif '<' in input_data and '>' in input_data:
                        return f"potential html tag detected: {input_data.lower()}"
                    # Check for Wikipedia-related patterns
                    elif 'wikipedia' in input_data.lower():
                        return f"wikipedia-related content detected: {input_data.lower()}"
                    # Check for data analysis-related patterns
                    elif any(term in input_data.lower() for term in ['data', 'analysis', 'statistics']):
                        return f"data analysis-related content detected: {input_data.lower()}"
                    # Check for mathematics-related patterns
                    elif any(term in input_data.lower() for term in ['math', 'equation', 'formula']):
                        return f"mathematics-related content detected: {input_data.lower()}"
                    # Check for text processing-related patterns
                    elif any(term in input_data.lower() for term in ['text', 'processing', 'nlp']):
                        return f"text processing-related content detected: {input_data.lower()}"
                    # Return the input as a lowercase string
                    else:
                        return f"processed input: {input_data.lower()}"
        else:
            # If the input is not a string, convert it to a string and return it lowercase
            return f"non-string input processed: {str(input_data).lower()}"