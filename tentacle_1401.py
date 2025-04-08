import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return 'data analysis wikipedia page detected'
        elif 'mathematics' in input_data.lower():
            return 'mathematics wikipedia page detected'
        elif 'text processing' in input_data.lower():
            return 'text processing wikipedia page detected'
        else:
            # For other HTML documents, extract and return the title if present
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip().lower()
                # Process the title: remove non-alphanumeric characters, split, sort, and join
                processed_title = ','.join(sorted(re.sub(r'[^a-zA-Z0-9\s]', '', title).split()))
                return f"other wikipedia page detected: {processed_title}"
            else:
                return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # For numbers, return the result as a string, lowercased, with additional information
            return f"numeric result: {str(result).lower()} (type: {type(result).__name__})"
        elif isinstance(result, (list, tuple, set)):
            # For collections, sort and join elements, including their types
            sorted_items = sorted(f"{str(item).lower()} ({type(item).__name__})" for item in result)
            joined_items = ','.join(sorted_items)
            return f"collection result: {joined_items}"
        elif isinstance(result, dict):
            # For dictionaries, sort keys and values, then join them, including their types
            sorted_items = sorted(f"{k}:{v} (key: {type(k).__name__}, value: {type(v).__name__})" for k, v in result.items())
            joined_items = ','.join(sorted_items)
            return f"dictionary result: {joined_items}"
        else:
            # For other types, convert to string, split into words, sort them, and join with commas
            processed_result = ','.join(sorted(str(result).lower().split()))
            # If the result is a single word, return it as is; otherwise, return the sorted, comma-separated list
            final_result = processed_result if ',' in processed_result else processed_result.replace(',', '')
            return f"other type result: {final_result} (type: {type(result).__name__})"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, remove non-alphanumeric characters, split into words, sort them, and join with commas
        processed_input = ','.join(sorted(re.sub(r'[^a-zA-Z0-9\s]', '', str(input_data).lower()).split()))
        # If the result is a single word, return it as is; otherwise, return the sorted, comma-separated list
        final_input = processed_input if ',' in processed_input else processed_input.replace(',', '')
        return f"text input processed: {final_input}"