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
            elif 'class="infobox"' in lower_input:
                return "wikipedia infobox html document detected"
            elif 'class="toc"' in lower_input:
                return "wikipedia table of contents html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # For numbers, return the sorted digits/characters, their sum, 
            # the original result, and a simple statistical analysis
            sorted_digits = ''.join(sorted(str(result).lower()))
            sum_of_digits = sum(int(digit) for digit in str(abs(result)) if digit.isdigit())
            mean_of_digits = sum_of_digits / len(str(abs(result))) if result != 0 else 0
            return f"{sorted_digits}, sum: {sum_of_digits}, mean: {mean_of_digits:.2f}, original: {result}"
        elif isinstance(result, str):
            # For strings, split, sort, remove duplicates, join, and count unique items
            sorted_items = sorted(set(item.strip().lower() for item in result.split(',')))
            unique_count = len(sorted_items)
            return f"{','.join(sorted_items)}, unique items: {unique_count}"
        elif isinstance(result, (list, tuple, set)):
            # For collections, sort elements, remove duplicates, join, and provide statistics
            sorted_items = sorted(set(str(item).lower() for item in result))
            item_count = len(sorted_items)
            average_length = sum(len(str(item)) for item in sorted_items) / item_count if item_count > 0 else 0
            return f"{','.join(sorted_items)}, total items: {item_count}, average length: {average_length:.2f}"
        else:
            # For other types, return a lowercase string representation, its length, 
            # the original result, and a simple analysis
            str_result = str(result).lower()
            length = len(str_result)
            word_count = len(str_result.split())
            return f"{str_result}, length: {length}, words: {word_count}, original: {result}"
    except Exception as e:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Check if the input contains any HTML-like tags
            if '<' in input_data and '>' in input_data:
                return "potential html fragment detected"
            
            # Check if the input looks like a mathematical expression
            if any(char in input_data for char in '+-*/()'):
                return f"unevaluated math expression: {input_data.lower()}"
            
            # Process the input as text
            lower_input = input_data.lower()
            words = lower_input.split()
            unique_words = len(set(words))
            word_count = len(words)
            char_count = len(lower_input)
            
            # Check for specific content types
            if 'data' in lower_input and 'analysis' in lower_input:
                return f"data analysis text detected, words: {word_count}, unique words: {unique_words}"
            elif any(math_term in lower_input for math_term in ['equation', 'formula', 'theorem', 'proof']):
                return f"mathematical text detected, words: {word_count}, unique words: {unique_words}"
            elif any(text_term in lower_input for text_term in ['token', 'stemming', 'lemmatization', 'nlp']):
                return f"text processing content detected, words: {word_count}, unique words: {unique_words}"
            else:
                return f"general text, words: {word_count}, unique words: {unique_words}, characters: {char_count}"
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort its elements, remove duplicates, join, and provide statistics
            sorted_items = sorted(set(str(item).lower() for item in input_data))
            item_count = len(sorted_items)
            average_length = sum(len(str(item)) for item in sorted_items) / item_count if item_count > 0 else 0
            return f"{','.join(sorted_items)}, total items: {item_count}, average length: {average_length:.2f}"
        else:
            # For other types, return a lowercase string representation, its length, 
            # and a simple analysis
            str_input = str(input_data).lower()
            length = len(str_input)
            word_count = len(str_input.split())
            return f"{str_input}, length: {length}, words: {word_count}, original: {input_data}"