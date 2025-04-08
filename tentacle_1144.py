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
        
        # Extract additional information from the HTML
        language = None
        if 'lang="' in input_data.lower():
            start = input_data.lower().index('lang="') + 6
            end = input_data.lower().index('"', start)
            language = input_data[start:end]
        
        # Return a dictionary with HTML-specific information
        return {
            'type': 'html',
            'document_type': document_type,
            'elements': sorted(detected_elements),
            'language': language,
            'original_input': input_data.strip()
        }
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result
        if isinstance(result, (int, float)):
            # If the result is a number, return it with additional information
            return {
                'type': 'number',
                'value': result,
                'string_value': str(result).lower(),
                'is_integer': isinstance(result, int),
                'is_positive': result > 0,
                'original_input': input_data.strip()
            }
        else:
            # Convert the result to a string, split it into words, sort them
            words = sorted(str(result).lower().split())
            
            # Return the sorted words as a list with additional information
            return {
                'type': 'math_result',
                'words': words,
                'word_count': len(words),
                'unique_words': len(set(words)),
                'original_result': str(result),
                'original_input': input_data.strip()
            }
    except Exception as e:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them
        words = sorted(str(input_data).lower().split())
        
        # Check if the input might be related to HTML document types
        related_to_html = any(term in input_data.lower() for term in ['data analysis', 'mathematics', 'text processing'])
        
        # Return the sorted words as a list with additional information
        return {
            'type': 'text',
            'words': words,
            'word_count': len(words),
            'unique_words': len(set(words)),
            'related_to_html': related_to_html,
            'original_input': input_data.strip(),
            'error': str(e) if str(e) else None
        }