import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return 'wikipedia data analysis html document detected (html5)'
        elif 'mathematics' in input_data.lower():
            return 'wikipedia mathematics html document detected (html5)'
        elif 'text processing' in input_data.lower():
            return 'wikipedia text processing html document detected (html5)'
        else:
            # Check for other HTML5 document types
            if 'html' in input_data.lower():
                return 'generic html5 document detected'
            elif 'xhtml' in input_data.lower():
                return 'generic xhtml document detected'
            else:
                return 'unknown html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # For numbers, return the result with a descriptive prefix
            return f"numeric result: {result}"
        elif isinstance(result, str):
            # For strings, split into words, sort them, and join with commas
            processed_result = ','.join(sorted(result.lower().split()))
            # Capitalize the first word and return
            return processed_result.capitalize()
        elif isinstance(result, list):
            # For lists, sort the elements and join them with commas
            processed_result = ','.join(map(str, sorted(result)))
            return f"sorted list: {processed_result}"
        else:
            # For other types, return a string representation
            return f"result type: {type(result).__name__}, value: {str(result)}"
    except:
        # If evaluation fails, process the input as text
        # Remove punctuation, convert to lowercase, split into words, and remove stop words
        stop_words = set(['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'from', 'by'])
        words = re.findall(r'\b\w+\b', str(input_data).lower())
        filtered_words = [word for word in words if word not in stop_words]
        
        # If there are no words left after filtering, return the original input
        if not filtered_words:
            return str(input_data).lower()
        
        # Sort the filtered words and join with commas
        processed_input = ','.join(sorted(filtered_words))
        
        # If the result is a single word, return it capitalized
        # Otherwise, return the sorted, comma-separated list with the first word capitalized
        if ',' in processed_input:
            return processed_input.capitalize()
        else:
            return processed_input.replace(',', '').capitalize()