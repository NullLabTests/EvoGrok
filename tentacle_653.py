def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        document_type = 'unknown'
        detected_elements = ['html document']
        
        # Determine the type of HTML document and add relevant elements
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
            detected_elements.extend(['wikipedia page', 'html5', 'data analysis'])
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
            detected_elements.extend(['wikipedia page', 'html5', 'mathematics'])
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
            detected_elements.extend(['wikipedia page', 'html5', 'text processing'])
        
        # Add the document type to detected elements
        detected_elements.append(document_type)
        
        # Return a dictionary with HTML-specific information
        return {
            'type': 'html',
            'document_type': document_type,
            'elements': sorted(detected_elements)
        }
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result
        if isinstance(result, (int, float)):
            # If the result is a number, return it as is
            return {
                'type': 'number',
                'value': result
            }
        else:
            # Convert the result to a string, split it into words, sort them
            words = sorted(str(result).lower().split())
            
            # Return the sorted words as a list
            return {
                'type': 'math_result',
                'words': words
            }
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them
        words = sorted(str(input_data).lower().split())
        
        # Return the sorted words as a list
        return {
            'type': 'text',
            'words': words
        }