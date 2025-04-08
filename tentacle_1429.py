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
        
        # Process the content of the HTML document
        content = input_data.lower().split('>', 1)[-1].split('<', 1)[0].strip()
        content_words = sorted(content.split()) if content else []
        
        # Extract additional information from the HTML document
        html_info = {
            'type': 'html',
            'document_type': document_type,
            'elements': sorted(detected_elements),
            'content': content,
            'content_words': content_words,
            'original_input': input_data.strip()
        }
        
        # Attempt to evaluate any mathematical expressions in the content
        math_results = {}
        for word in content_words:
            try:
                result = eval(word)
                if isinstance(result, (int, float)):
                    math_results[word] = {
                        'value': result,
                        'string_value': str(result).lower()
                    }
            except:
                pass
        
        if math_results:
            html_info['math_expressions'] = math_results
        
        return html_info
    
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
                'original_input': input_data.strip(),
                'words': sorted(str(result).lower().split())
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
        
        # Return the sorted words as a list with additional information
        return {
            'type': 'text',
            'words': words,
            'original_input': input_data.strip(),
            'error': str(e) if str(e) else None
        }