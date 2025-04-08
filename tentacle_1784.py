import re

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
        elif 'statistics' in lower_input:
            return "wikipedia statistics html document detected"
        elif 'science' in lower_input:
            return "wikipedia science html document detected"
        elif 'programming' in lower_input:
            return "wikipedia programming html document detected"
        elif 'class="mw-page-title-main"' in lower_input:
            # Further classify based on content
            if 'history' in lower_input:
                return "wikipedia history html document detected"
            elif 'literature' in lower_input:
                return "wikipedia literature html document detected"
            else:
                return "wikipedia generic html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # For numbers, return the sorted digits/characters, their sum, product, and the original result
            sorted_digits = ''.join(sorted(str(result).lower()))
            sum_of_digits = sum(int(digit) for digit in str(abs(result)) if digit.isdigit())
            product_of_digits = 1
            for digit in str(abs(result)):
                if digit.isdigit():
                    product_of_digits *= int(digit)
            return f"{sorted_digits}, sum: {sum_of_digits}, product: {product_of_digits}, original: {result}"
        elif isinstance(result, str):
            # For strings, split, sort, remove duplicates, join, and count words
            words = result.split()
            sorted_items = sorted(set(item.strip().lower() for item in result.split(',')))
            word_count = len(words)
            return f"{','.join(sorted_items)}, word count: {word_count}"
        elif isinstance(result, (list, tuple, set)):
            # For collections, sort elements, remove duplicates, join, and count items
            sorted_items = sorted(set(str(item).lower() for item in result))
            item_count = len(sorted_items)
            return f"{','.join(sorted_items)}, item count: {item_count}"
        elif callable(result):
            # For functions, return its name and docstring
            return f"function: {result.__name__}, docstring: {result.__doc__ or 'None'}"
        else:
            # For other types, return a lowercase string representation, its length, type, and the original result
            return f"{str(result).lower()}, length: {len(str(result))}, type: {type(result).__name__}, original: {result}"
    except Exception as e:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Check if the input contains any HTML-like tags
            if re.search(r'<[^>]+>', input_data):
                return "potential html fragment detected"
            
            # Check if the input looks like a mathematical expression
            if re.search(r'[+\-*/()]', input_data):
                return f"unevaluated math expression: {input_data.lower()}"
            
            # Check if the input looks like a URL
            if re.match(r'^(https?|ftp)://', input_data):
                return f"url detected: {input_data.lower()}"
            
            # Split the input, sort it, remove duplicates, join it back together, and count words
            words = input_data.split()
            sorted_items = sorted(set(item.strip().lower() for item in input_data.split(',')))
            word_count = len(words)
            return f"{','.join(sorted_items)}, word count: {word_count}"
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort its elements, remove duplicates, join them, and count items
            sorted_items = sorted(set(str(item).lower() for item in input_data))
            item_count = len(sorted_items)
            return f"{','.join(sorted_items)}, item count: {item_count}"
        elif callable(input_data):
            # For functions, return its name and docstring
            return f"function: {input_data.__name__}, docstring: {input_data.__doc__ or 'None'}"
        else:
            # For other types, return a lowercase string representation, its length, type, and the original input
            return f"{str(input_data).lower()}, length: {len(str(input_data))}, type: {type(input_data).__name__}, original: {input_data}"