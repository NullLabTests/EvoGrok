def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return 'wikipedia data analysis html5 document detected'
        elif 'mathematics' in input_data.lower():
            return 'wikipedia mathematics html5 document detected'
        elif 'text processing' in input_data.lower():
            return 'wikipedia text processing html5 document detected'
        else:
            # Check for other specific HTML5 features
            if 'html5' in input_data.lower():
                return 'generic html5 document detected'
            else:
                return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it into words, sort them, and join with commas
        processed_result = ','.join(sorted(str(result).lower().split()))
        # If the result is a single word or number, return it as is; otherwise, return the sorted, comma-separated list
        if ',' in processed_result:
            return f"mathematical result: {processed_result}"
        else:
            return f"mathematical result: {processed_result.replace(',', '')}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        words = str(input_data).lower().split()
        unique_words = list(set(words))  # Remove duplicates
        processed_input = ','.join(sorted(unique_words))
        
        # Check if the processed input matches any known Wikipedia page titles
        if processed_input == 'data,analysis':
            return 'wikipedia data analysis text detected'
        elif processed_input == 'mathematics':
            return 'wikipedia mathematics text detected'
        elif processed_input == 'text,processing':
            return 'wikipedia text processing text detected'
        
        # New feature: Check for common programming language keywords
        programming_keywords = ['python', 'java', 'javascript', 'c++', 'ruby']
        detected_languages = [lang for lang in programming_keywords if lang in processed_input]
        
        if detected_languages:
            return f"programming language detected: {', '.join(detected_languages)}"
        
        # If the result is a single word, return it capitalized; otherwise, return the sorted, comma-separated list
        if ',' not in processed_input:
            return processed_input.capitalize()
        else:
            return f"processed text: {processed_input}"