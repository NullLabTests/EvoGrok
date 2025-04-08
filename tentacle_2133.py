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
            # For numbers, return the sorted digits/characters, their sum, 
            # the original result, and whether it's prime (for integers)
            sorted_digits = ''.join(sorted(str(result).lower()))
            sum_of_digits = sum(int(digit) for digit in str(abs(result)) if digit.isdigit())
            
            if isinstance(result, int) and result > 1:
                is_prime = all(result % i != 0 for i in range(2, int(result**0.5) + 1))
                prime_status = "prime" if is_prime else "not prime"
            else:
                prime_status = "n/a"
            
            return f"{sorted_digits}, sum: {sum_of_digits}, original: {result}, {prime_status}"
        
        elif isinstance(result, str):
            # For strings, split, sort, remove duplicates, join, and count unique words
            words = result.lower().split()
            unique_words = sorted(set(words))
            word_count = len(unique_words)
            return f"{','.join(unique_words)}, unique word count: {word_count}"
        
        elif isinstance(result, (list, tuple, set)):
            # For collections, sort elements, remove duplicates, join, and calculate average length
            items = [str(item).lower() for item in result]
            unique_items = sorted(set(items))
            avg_length = sum(len(item) for item in unique_items) / len(unique_items) if unique_items else 0
            return f"{','.join(unique_items)}, average length: {avg_length:.2f}"
        
        else:
            # For other types, return a lowercase string representation, its length, 
            # the original result, and its type
            return f"{str(result).lower()}, length: {len(str(result))}, original: {result}, type: {type(result).__name__}"
    
    except Exception as e:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Check if the input contains any HTML-like tags
            if '<' in input_data and '>' in input_data:
                return "potential html fragment detected"
            
            # Check if the input looks like a mathematical expression
            if any(char in input_data for char in '+-*/()'):
                return f"unevaluated math expression: {input_data.lower()}"
            
            # Split the input, sort it, remove duplicates, join it back together, and count items
            items = sorted(set(item.strip().lower() for item in input_data.split(',')))
            item_count = len(items)
            return f"{','.join(items)}, item count: {item_count}"
        
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort its elements, remove duplicates, join them, and calculate average length
            items = [str(item).lower() for item in input_data]
            unique_items = sorted(set(items))
            avg_length = sum(len(item) for item in unique_items) / len(unique_items) if unique_items else 0
            return f"{','.join(unique_items)}, average length: {avg_length:.2f}"
        
        else:
            # For other types, return a lowercase string representation, its length, 
            # the original input, and its type
            return f"{str(input_data).lower()}, length: {len(str(input_data))}, original: {input_data}, type: {type(input_data).__name__}"