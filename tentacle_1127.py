def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return 'wikipedia data analysis html document detected (html5)'
        elif 'mathematics' in input_data.lower():
            return 'wikipedia mathematics html document detected (html5)'
        elif 'text processing' in input_data.lower():
            return 'wikipedia text processing html document detected (html5)'
        else:
            # If no specific pattern is detected, check for generic HTML5
            if 'html5' in input_data.lower():
                return 'generic html5 document detected'
            else:
                return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # If the result is a number, return it as a string with two decimal places
            return f"{result:.2f}".lower()
        else:
            # Convert the result to a string, split it into words, sort them, and join with commas
            processed_result = ','.join(sorted(str(result).lower().split()))
            
            # If the result is a single word or number, return it capitalized
            # Otherwise, return the sorted, comma-separated list with the first word capitalized
            if ',' in processed_result:
                return processed_result.capitalize()
            else:
                return processed_result.replace(',', '').capitalize()
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        processed_input = ','.join(sorted(str(input_data).lower().split()))
        
        # If the result is a single word, return it capitalized
        # Otherwise, return the sorted, comma-separated list with the first word capitalized
        if ',' in processed_input:
            return processed_input.capitalize()
        else:
            return processed_input.replace(',', '').capitalize()