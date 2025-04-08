def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return 'wikipedia data analysis html document detected'
        elif 'mathematics' in input_data.lower():
            return 'wikipedia mathematics html document detected'
        elif 'text processing' in input_data.lower():
            return 'wikipedia text processing html document detected'
        else:
            return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it into words, sort them, and join with commas
        processed_result = ','.join(sorted(str(result).lower().split()))
        # If the result is a single word or number, return it as is; otherwise, return the sorted, comma-separated list
        return processed_result if ',' in processed_result else processed_result.replace(',', '')
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        processed_input = ','.join(sorted(str(input_data).lower().split()))
        # If the result is a single word, return it capitalized; otherwise, return the sorted, comma-separated list
        return processed_input.capitalize() if ',' not in processed_input else processed_input