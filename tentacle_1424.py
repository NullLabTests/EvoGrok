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
        
        # Attempt to evaluate the HTML content as a mathematical expression
        math_result = None
        try:
            math_result = eval(''.join(filter(str.isdigit, html_content)))
        except:
            pass
        
        # Return a dictionary with HTML-specific information
        return {
            'type': 'html',
            'document_type': document_type,
            'elements': sorted(detected_elements),
            'words': words,
            'math_result': math_result if isinstance(math_result, (int, float)) else None,
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
        
        # Attempt to find HTML-like structure in the text
        html_like = any(tag in input_data.lower() for tag in ['<html>', '<body>', '<head>'])
        
        # Return the sorted words as a list with additional information
        return {
            'type': 'text' if not html_like else 'html-like',
            'words': words,
            'original_input': input_data.strip(),
            'error': str(e) if str(e) else None,
            'html_like': html_like
        }