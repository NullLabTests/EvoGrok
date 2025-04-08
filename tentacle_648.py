def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        document_type = 'unknown'
        detected_elements = ['html document']
        
        # Determine the type of HTML document and add relevant elements
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
            detected_elements.extend(['wikipedia page', 'html5', 'data visualization'])
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
            detected_elements.extend(['wikipedia page', 'html5', 'equations'])
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
            detected_elements.extend(['wikipedia page', 'html5', 'natural language processing'])
        
        # Add the document type to detected elements
        detected_elements.append(document_type)
        
        # Check for numbers and special characters in the input
        if any(char.isdigit() for char in input_data):
            detected_elements.append('contains numbers')
        if any(not char.isalnum() for char in input_data):
            detected_elements.append('contains special characters')
        
        # Return a sorted, comma-separated list of detected elements
        return ','.join(sorted(detected_elements))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result)
        
        # Check if the result is a number
        if result_str.replace('.', '').replace('-', '').isdigit():
            return result_str
        
        # Otherwise, process the result as text
        words = sorted(result_str.lower().split())
        
        # Add information about numbers and special characters
        if any(char.isdigit() for char in result_str):
            words.append('contains numbers')
        if any(not char.isalnum() for char in result_str):
            words.append('contains special characters')
        
        # Return the sorted, comma-separated list of words
        return ','.join(words)
    except:
        # If evaluation fails, process the input as text
        input_str = str(input_data).lower()
        
        # Split into words, sort them, and add information about numbers and special characters
        words = sorted(input_str.split())
        if any(char.isdigit() for char in input_str):
            words.append('contains numbers')
        if any(not char.isalnum() for char in input_str):
            words.append('contains special characters')
        
        # Return the sorted, comma-separated list of words
        return ','.join(words)