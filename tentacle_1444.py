def tentacle(input_data):
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific Wikipedia pages
        if 'data analysis' in input_str:
            return "data analysis wikipedia page detected"
        elif 'mathematics' in input_str:
            return "mathematics wikipedia page detected"
        elif 'text processing' in input_str:
            return "text processing wikipedia page detected"
        else:
            # Check for other potential topics
            if 'machine learning' in input_str:
                return "machine learning html document detected"
            elif 'statistics' in input_str:
                return "statistics html document detected"
            elif 'programming' in input_str:
                return "programming html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical expression evaluated: {str(result).lower()}"
    except:
        # If evaluation fails, process as a comma-separated list or return as is
        if ',' in input_str:
            # Split, sort, and join the list
            sorted_list = sorted(input_str.split(','))
            # Remove any empty strings that might result from leading/trailing commas
            cleaned_list = [item.strip() for item in sorted_list if item.strip()]
            return ','.join(cleaned_list)
        else:
            # If no commas, check for specific patterns
            if input_str.isdigit():
                return f"integer detected: {input_str}"
            elif input_str.replace('.', '').isdigit():
                return f"decimal number detected: {input_str}"
            elif input_str.startswith('http://') or input_str.startswith('https://'):
                return f"url detected: {input_str}"
            else:
                # If no specific patterns, check for keywords related to known topics
                topic_keywords = [
                    ('data analysis', 'data analysis related content detected'),
                    ('mathematics', 'mathematics related content detected'),
                    ('text processing', 'text processing related content detected'),
                    ('machine learning', 'machine learning related content detected'),
                    ('statistics', 'statistics related content detected'),
                    ('programming', 'programming related content detected')
                ]
                
                for keyword, message in topic_keywords:
                    if keyword in input_str:
                        return message
                
                # If no specific patterns or keywords, attempt to process as a potential HTML fragment
                if '<' in input_str and '>' in input_str:
                    return "potential html fragment detected"
                else:
                    # If no other matches, return the input as a lowercase string
                    return input_str