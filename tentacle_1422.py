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
        
        # Process the HTML content
        html_content = input_data.lower()
        words = sorted(html_content.split())
        
        # Extract additional information
        doctype = html_content.split('>')[0] if '>' in html_content else 'unknown'
        title = next((word for word in words if word.startswith('title=')), 'unknown')
        
        # Return a dictionary with HTML-specific information
        return {
            'type': 'html',
            'document_type': document_type,
            'elements': sorted(detected_elements),
            'words': words,
            'doctype': doctype,
            'title': title,
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
                'words': sorted(str(result).lower().split()),
                'original_input': input_data.strip()
            }
        else:
            # Convert the result to a string, split it into words, sort them
            words = sorted(str(result).lower().split())
            
            # Return the sorted words as a list with additional information
            return {
                'type': 'math_result',
                'words': words,
                'original_result': str(result),
                'original_input': input_data.strip()
            }
    except Exception as e:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them
        words = sorted(str(input_data).lower().split())
        
        # Attempt to evaluate as a simple arithmetic expression
        try:
            simple_result = eval(' '.join(words))
            if isinstance(simple_result, (int, float)):
                return {
                    'type': 'simple_arithmetic',
                    'value': simple_result,
                    'string_value': str(simple_result).lower(),
                    'words': words,
                    'original_input': input_data.strip()
                }
        except:
            pass
        
        # Check for specific patterns in the text
        if 'data analysis' in input_data.lower():
            return {
                'type': 'data_analysis_text',
                'words': words,
                'original_input': input_data.strip()
            }
        elif 'mathematics' in input_data.lower():
            return {
                'type': 'mathematics_text',
                'words': words,
                'original_input': input_data.strip()
            }
        elif 'text processing' in input_data.lower():
            return {
                'type': 'text_processing_text',
                'words': words,
                'original_input': input_data.strip()
            }
        
        # Return the sorted words as a list with additional information
        return {
            'type': 'text',
            'words': words,
            'original_input': input_data.strip(),
            'error': str(e) if str(e) else None
        }