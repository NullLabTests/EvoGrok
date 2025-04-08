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
                # Check for other common Wikipedia elements
                if 'id="firstheading"' in lower_input:
                    return "wikipedia article html document detected"
                elif 'class="infobox"' in lower_input:
                    return "wikipedia infobox html document detected"
                else:
                    return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # For numbers, return the sorted digits/characters, their sum, product, and the original result
            sorted_digits = ''.join(sorted(str(result).lower()))
            digits = [int(digit) for digit in str(abs(result)) if digit.isdigit()]
            sum_of_digits = sum(digits)
            product_of_digits = 1 if digits else 0
            for digit in digits:
                product_of_digits *= digit
            return f"{sorted_digits}, sum: {sum_of_digits}, product: {product_of_digits}, original: {result}"
        elif isinstance(result, str):
            # For strings, split, sort, remove duplicates, count occurrences, and join
            items = [item.strip().lower() for item in result.split(',')]
            sorted_items = sorted(set(items))
            item_counts = {item: items.count(item) for item in sorted_items}
            formatted_items = [f"{item} ({count})" for item, count in item_counts.items()]
            return ','.join(formatted_items)
        elif isinstance(result, (list, tuple, set)):
            # For collections, sort elements, remove duplicates, count occurrences, and join
            items = [str(item).lower() for item in result]
            sorted_items = sorted(set(items))
            item_counts = {item: items.count(item) for item in sorted_items}
            formatted_items = [f"{item} ({count})" for item, count in item_counts.items()]
            return ','.join(formatted_items)
        else:
            # For other types, return a lowercase string representation, its length, type, and the original result
            return f"{str(result).lower()}, length: {len(str(result))}, type: {type(result).__name__}, original: {result}"
    except Exception as e:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Check if the input contains any HTML-like tags
            if '<' in input_data and '>' in input_data:
                return "potential html fragment detected"
            
            # Check if the input looks like a mathematical expression
            if any(char in input_data for char in '+-*/()'):
                return f"unevaluated math expression: {input_data.lower()}"
            
            # Split the input, sort it, remove duplicates, count occurrences, and join it back together
            items = [item.strip().lower() for item in input_data.split(',')]
            sorted_items = sorted(set(items))
            item_counts = {item: items.count(item) for item in sorted_items}
            formatted_items = [f"{item} ({count})" for item, count in item_counts.items()]
            return ','.join(formatted_items)
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort its elements, remove duplicates, count occurrences, and join them
            items = [str(item).lower() for item in input_data]
            sorted_items = sorted(set(items))
            item_counts = {item: items.count(item) for item in sorted_items}
            formatted_items = [f"{item} ({count})" for item, count in item_counts.items()]
            return ','.join(formatted_items)
        else:
            # For other types, return a lowercase string representation, its length, type, and the original input
            return f"{str(input_data).lower()}, length: {len(str(input_data))}, type: {type(input_data).__name__}, original: {input_data}"