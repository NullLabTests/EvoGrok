import re

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
            # For generic HTML documents, extract and return the title if present
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip().lower()
                # Process the title further
                processed_title = ','.join(sorted(title.split()))
                return f"generic html document detected: {processed_title}"
            else:
                return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # For numbers, return the result as a string, lowercased, with additional information
            numeric_value = str(result).lower()
            if '.' in numeric_value:
                integer_part, decimal_part = numeric_value.split('.')
                return f"numeric result: integer part: {integer_part}, decimal part: {decimal_part}"
            else:
                return f"numeric result: integer: {numeric_value}"
        elif isinstance(result, (list, tuple, set)):
            # For collections, sort and join elements
            sorted_items = sorted(str(item).lower() for item in result)
            joined_items = ','.join(sorted_items)
            # Count the number of items in the collection
            item_count = len(sorted_items)
            return f"collection result: {joined_items}, item count: {item_count}"
        elif isinstance(result, dict):
            # For dictionaries, sort keys and values, then join them
            sorted_items = sorted(f"{k}:{v}" for k, v in result.items())
            joined_items = ','.join(sorted_items)
            # Count the number of key-value pairs
            pair_count = len(sorted_items)
            return f"dictionary result: {joined_items}, pair count: {pair_count}"
        else:
            # For other types, convert to string, split into words, sort them, and join with commas
            processed_result = ','.join(sorted(str(result).lower().split()))
            # If the result is a single word, return it as is; otherwise, return the sorted, comma-separated list
            final_result = processed_result if ',' in processed_result else processed_result.replace(',', '')
            # Count the number of words
            word_count = len(final_result.split(',')) if ',' in final_result else 1
            return f"other type result: {final_result}, word count: {word_count}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        processed_input = ','.join(sorted(str(input_data).lower().split()))
        # If the result is a single word, return it as is; otherwise, return the sorted, comma-separated list
        final_input = processed_input if ',' in processed_input else processed_input.replace(',', '')
        # Count the number of words
        word_count = len(final_input.split(',')) if ',' in final_input else 1
        return f"text input processed: {final_input}, word count: {word_count}"