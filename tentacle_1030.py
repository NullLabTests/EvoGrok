def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lower_input = input_data.lower()
        
        # Determine the type of HTML document based on the title and content
        if 'data analysis' in lower_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lower_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lower_input:
            return "wikipedia text processing html document detected"
        else:
            # Check for specific classes or attributes
            if 'class="mw-page-title-main"' in lower_input:
                # Further classify based on content
                if 'statistics' in lower_input:
                    return "wikipedia statistics html document detected"
                elif 'science' in lower_input:
                    return "wikipedia science html document detected"
                else:
                    return "wikipedia generic html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # For numbers, return the sorted digits/characters and their sum
            sorted_digits = ''.join(sorted(str(result).lower()))
            return f"{sorted_digits}, sum: {sum(int(digit) for digit in str(abs(result)) if digit.isdigit())}"
        elif isinstance(result, str):
            # For strings, split, sort, remove duplicates, and join
            sorted_items = sorted(set(item.strip().lower() for item in result.split(',')))
            return ','.join(sorted_items)
        elif isinstance(result, (list, tuple, set)):
            # For collections, sort elements, remove duplicates, and join
            sorted_items = sorted(set(str(item).lower() for item in result))
            return ','.join(sorted_items)
        else:
            # For other types, return a lowercase string representation
            return str(result).lower()
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Check if the input contains any HTML-like tags
            if '<' in input_data and '>' in input_data:
                return "potential html fragment detected"
            
            # Split the input, sort it, remove duplicates, and join it back together
            sorted_items = sorted(set(item.strip().lower() for item in input_data.split(',')))
            return ','.join(sorted_items)
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort its elements, remove duplicates, and join them
            sorted_items = sorted(set(str(item).lower() for item in input_data))
            return ','.join(sorted_items)
        else:
            # For other types, return a lowercase string representation
            return str(input_data).lower()