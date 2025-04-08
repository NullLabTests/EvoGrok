def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        document_type = 'unknown'
        detected_elements = ['html document']
        
        # Determine the type of HTML document and add relevant elements
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
            detected_elements.extend(['wikipedia page', 'html5', 'statistics', 'data visualization'])
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
            detected_elements.extend(['wikipedia page', 'html5', 'algebra', 'geometry'])
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
            detected_elements.extend(['wikipedia page', 'html5', 'nlp', 'regex'])
        
        # Add the document type to detected elements
        detected_elements.append(document_type)
        
        # Check for additional keywords and add them to detected elements
        if 'wikipedia' in input_data.lower():
            detected_elements.append('wikipedia')
        if 'html5' in input_data.lower():
            detected_elements.append('html5')
        
        # Return a sorted, comma-separated list of unique detected elements
        return f"html document detected: {','.join(sorted(set(detected_elements)))}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string and lowercase it
        result_str = str(result).lower()
        
        # Check if the result is a single number
        if result_str.replace('.', '').replace('-', '').isdigit():
            return result_str
        
        # If not a single number, process as text
        words = sorted(result_str.split())
        
        # Check for specific keywords and categorize the result
        categories = []
        if any(keyword in words for keyword in ['data', 'analysis', 'statistics', 'visualization']):
            categories.append('data analysis')
        if any(keyword in words for keyword in ['math', 'equation', 'algebra', 'geometry']):
            categories.append('mathematics')
        if any(keyword in words for keyword in ['text', 'string', 'nlp', 'regex']):
            categories.append('text processing')
        
        # Combine categories and words, ensuring uniqueness
        result_list = list(set(categories + words))
        
        # Sort the result and join with commas
        return f"mathematical expression evaluated: {','.join(sorted(result_list))}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        words = sorted(str(input_data).lower().split())
        
        # Check for specific keywords and categorize the result
        categories = []
        if any(keyword in words for keyword in ['data', 'analysis', 'statistics', 'visualization']):
            categories.append('data analysis')
        if any(keyword in words for keyword in ['math', 'equation', 'algebra', 'geometry']):
            categories.append('mathematics')
        if any(keyword in words for keyword in ['text', 'string', 'nlp', 'regex']):
            categories.append('text processing')
        
        # Remove any empty strings from the words list
        words = [word for word in words if word]
        
        # Combine categories and words, ensuring uniqueness
        result_list = list(set(categories + words))
        
        # Sort the result and join with commas
        return f"text processed: {','.join(sorted(result_list))}"