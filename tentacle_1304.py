def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lower_input = input_data.lower()
        
        # Classify the HTML document based on its content
        if 'data analysis' in lower_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lower_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lower_input:
            return "wikipedia text processing html document detected"
        else:
            # Check for specific classes or attributes
            if 'class="mw-page-title-main"' in lower_input:
                # Extract the page title if possible
                title_start = lower_input.find('class="mw-page-title-main"') + len('class="mw-page-title-main">')
                title_end = lower_input.find('</', title_start)
                if title_start != -1 and title_end != -1:
                    title = lower_input[title_start:title_end].strip()
                    return f"wikipedia {title} html document detected"
                else:
                    return "wikipedia generic html document detected"
            else:
                # Check for other common HTML document types
                if 'html>' in lower_input and 'body>' in lower_input:
                    return "generic html document detected"
                else:
                    return "unknown document type detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, lowercase it, and sort its characters
        sorted_result = ''.join(sorted(str(result).lower()))
        
        # Calculate additional statistics
        numeric_value = float(result) if isinstance(result, (int, float)) else None
        is_prime = is_prime_number(numeric_value) if numeric_value is not None and numeric_value > 1 else None
        
        # Return the sorted result along with its length, type, original value, and additional statistics
        return f"{sorted_result} (length: {len(sorted_result)}, type: {type(result).__name__}, original: {result}, numeric: {numeric_value}, prime: {is_prime})"
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Split the input, sort it, remove duplicates, and join it back together
            sorted_items = sorted(set(item.strip().lower() for item in input_data.split(',')))
            
            # Calculate additional statistics
            word_count = len(input_data.split())
            unique_words = len(set(input_data.lower().split()))
            
            # Return the sorted items along with their count, total length, and additional statistics
            total_length = sum(len(item) for item in sorted_items)
            return f"{','.join(sorted_items)} (count: {len(sorted_items)}, total length: {total_length}, word count: {word_count}, unique words: {unique_words})"
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort its elements, remove duplicates, and join them
            sorted_items = sorted(set(str(item).lower() for item in input_data))
            
            # Calculate additional statistics
            numeric_items = sum(1 for item in input_data if isinstance(item, (int, float)))
            string_items = sum(1 for item in input_data if isinstance(item, str))
            
            # Return the sorted items along with their count, the original type, total length, and additional statistics
            total_length = sum(len(str(item)) for item in sorted_items)
            return f"{','.join(sorted_items)} (count: {len(sorted_items)}, type: {type(input_data).__name__}, total length: {total_length}, numeric items: {numeric_items}, string items: {string_items})"
        else:
            # For other types, return a lowercase string representation along with its type, length, and original value
            str_repr = str(input_data).lower()
            return f"{str_repr} (length: {len(str_repr)}, type: {type(input_data).__name__}, original: {input_data})"

# Helper function to check if a number is prime
def is_prime_number(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True