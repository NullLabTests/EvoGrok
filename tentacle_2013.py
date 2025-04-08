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
                elif 'technology' in lower_input:
                    return "wikipedia technology html document detected"
                elif 'history' in lower_input:
                    return "wikipedia history html document detected"
                else:
                    return "wikipedia generic html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # For numbers, return the sorted digits/characters, their sum, average, and the original result
            str_result = str(result).lower()
            sorted_digits = ''.join(sorted(str_result))
            digits = [int(digit) for digit in str_result if digit.isdigit()]
            sum_of_digits = sum(digits)
            avg_of_digits = sum_of_digits / len(digits) if digits else 0
            return f"{sorted_digits}, sum: {sum_of_digits}, average: {avg_of_digits:.2f}, original: {result}"
        elif isinstance(result, str):
            # For strings, split, sort, remove duplicates, join, and calculate statistics
            words = [word.strip().lower() for word in result.split()]
            unique_words = sorted(set(words))
            word_count = len(words)
            unique_count = len(unique_words)
            return f"{','.join(unique_words)}, total words: {word_count}, unique words: {unique_count}"
        elif isinstance(result, (list, tuple, set)):
            # For collections, sort elements, remove duplicates, join, and calculate statistics
            sorted_items = sorted(set(str(item).lower() for item in result))
            item_count = len(result)
            unique_count = len(sorted_items)
            return f"{','.join(sorted_items)}, total items: {item_count}, unique items: {unique_count}"
        else:
            # For other types, return a lowercase string representation, its length, type, and the original result
            str_result = str(result).lower()
            return f"{str_result}, length: {len(str_result)}, type: {type(result).__name__}, original: {result}"
    except Exception as e:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Check if the input contains any HTML-like tags
            if '<' in input_data and '>' in input_data:
                return "potential html fragment detected"
            
            # Check if the input looks like a mathematical expression
            if any(char in input_data for char in '+-*/()'):
                return f"unevaluated math expression: {input_data.lower()}"
            
            # Split the input, sort it, remove duplicates, join it back together, and calculate statistics
            words = [word.strip().lower() for word in input_data.split()]
            unique_words = sorted(set(words))
            word_count = len(words)
            unique_count = len(unique_words)
            return f"{','.join(unique_words)}, total words: {word_count}, unique words: {unique_count}"
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort its elements, remove duplicates, join them, and calculate statistics
            sorted_items = sorted(set(str(item).lower() for item in input_data))
            item_count = len(input_data)
            unique_count = len(sorted_items)
            return f"{','.join(sorted_items)}, total items: {item_count}, unique items: {unique_count}"
        else:
            # For other types, return a lowercase string representation, its length, type, and the original input
            str_input = str(input_data).lower()
            return f"{str_input}, length: {len(str_input)}, type: {type(input_data).__name__}, original: {input_data}"