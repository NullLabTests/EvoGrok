def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return 'data analysis html document detected'
        elif 'mathematics' in input_data.lower():
            return 'mathematics html document detected'
        elif 'text processing' in input_data.lower():
            return 'text processing html document detected'
        else:
            # If no specific type is detected, process the content
            content = input_data.lower().split('>', 1)[1].split('<', 1)[0]
            if content:
                return f"generic html document with content: {','.join(sorted(content.split()))}"
            else:
                return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # For numbers, return the result as a string, lowercased
            return str(result).lower()
        elif isinstance(result, bool):
            # For booleans, return a descriptive string
            return 'true' if result else 'false'
        else:
            # For other types, convert to string, split into words, sort them, and join with commas
            processed_result = ','.join(sorted(str(result).lower().split()))
            # If the result is a single word, return it as is; otherwise, return the sorted, comma-separated list
            return processed_result if ',' in processed_result else processed_result.replace(',', '')
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        processed_input = ','.join(sorted(str(input_data).lower().split()))
        # If the result is a single word, return it as is; otherwise, return the sorted, comma-separated list
        return processed_input if ',' in processed_input else processed_input.replace(',', '')