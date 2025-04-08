def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return 'Wikipedia Data Analysis HTML5 Document Detected'
        elif 'mathematics' in input_data.lower():
            return 'Wikipedia Mathematics HTML5 Document Detected'
        elif 'text processing' in input_data.lower():
            return 'Wikipedia Text Processing HTML5 Document Detected'
        else:
            # For generic HTML documents, extract and process the title
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip()
                return f'Generic HTML5 Document Detected: "{title}"'
            else:
                return 'Generic HTML5 Document Detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result: convert to string, split into words, sort them, and join with commas
        processed_result = ','.join(sorted(str(result).lower().split()))
        
        # If the result is a single word or number, return it capitalized
        # Otherwise, return the sorted, comma-separated list with the first word capitalized
        if ',' in processed_result:
            return f'Math Result: {processed_result.capitalize()}'
        else:
            return f'Math Result: {processed_result.replace(",", "").capitalize()}'
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        processed_input = ','.join(sorted(str(input_data).lower().split()))
        
        # Count the number of unique words
        unique_words = len(set(processed_input.split(',')))
        
        # If the result is a single word, return it capitalized
        # Otherwise, return the sorted, comma-separated list with the first word capitalized
        # and include the count of unique words
        if ',' in processed_input:
            return f'Text Processed: {processed_input.capitalize()} (Unique Words: {unique_words})'
        else:
            return f'Text Processed: {processed_input.replace(",", "").capitalize()} (Unique Words: {unique_words})'