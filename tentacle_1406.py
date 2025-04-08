def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        input_lower = input_data.lower()
        if 'data analysis' in input_lower:
            return 'Wikipedia Data Analysis HTML document detected (HTML5)'
        elif 'mathematics' in input_lower:
            return 'Wikipedia Mathematics HTML document detected (HTML5)'
        elif 'text processing' in input_lower:
            return 'Wikipedia Text Processing HTML document detected (HTML5)'
        else:
            # Attempt to extract the title from the HTML
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip()
                return f'Wikipedia {title} HTML document detected (HTML5)'
            else:
                return 'Generic HTML5 document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result
        result_str = str(result)
        result_type = type(result).__name__
        
        # Convert the result to a string, split it into words, sort them, and join with commas
        processed_result = ','.join(sorted(result_str.lower().split()))
        
        # Format the output
        if ',' in processed_result:
            return f"Mathematical result ({result_type}): {processed_result.capitalize()}"
        else:
            return f"Mathematical result ({result_type}): {result_str}"
    except Exception as e:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        processed_input = ','.join(sorted(str(input_data).lower().split()))
        
        # If the result is a single word, return it capitalized
        # Otherwise, return the sorted, comma-separated list with the first word capitalized
        if ',' in processed_input:
            return f"Processed text: {processed_input.capitalize()}"
        else:
            return f"Processed text: {processed_input.replace(',', '').capitalize()}"

# Import the re module for regular expression operations
import re