import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        return process_html_document(input_data)
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        return process_mathematical_result(result, input_data)
    except Exception as e:
        # If evaluation fails, process the input as text
        return process_text_input(input_data, str(e))

def process_html_document(html_data):
    document_type = 'unknown'
    detected_elements = ['html document']
    
    # Determine the type of HTML document and add relevant elements
    if 'data analysis' in html_data.lower():
        document_type = 'data analysis'
        detected_elements.extend(['wikipedia page', 'html5', 'data analysis', 'statistics', 'data visualization'])
    elif 'mathematics' in html_data.lower():
        document_type = 'mathematics'
        detected_elements.extend(['wikipedia page', 'html5', 'mathematics', 'algebra', 'geometry', 'calculus'])
    elif 'text processing' in html_data.lower():
        document_type = 'text processing'
        detected_elements.extend(['wikipedia page', 'html5', 'text processing', 'natural language processing', 'tokenization'])
    
    # Add the document type to detected elements
    detected_elements.append(document_type)
    
    # Extract additional information from the HTML
    html_info = {
        'doctype': html_data.split()[0].lower(),
        'html_attributes': extract_html_attributes(html_data),
        'title': extract_title(html_data)
    }
    
    # Return a dictionary with HTML-specific information
    return {
        'type': 'html',
        'document_type': document_type,
        'elements': sorted(detected_elements),
        'html_info': html_info,
        'original_input': html_data.strip()
    }

def process_mathematical_result(result, original_input):
    if isinstance(result, (int, float)):
        # If the result is a number, return it with additional information
        return {
            'type': 'number',
            'value': result,
            'string_value': str(result).lower(),
            'is_integer': isinstance(result, int),
            'is_positive': result > 0,
            'original_input': original_input.strip(),
            'evaluation_successful': True
        }
    else:
        # Convert the result to a string, split it into words, sort them
        words = sorted(str(result).lower().split())
        
        # Return the sorted words as a list with additional information
        return {
            'type': 'math_result',
            'words': words,
            'original_result': str(result),
            'word_count': len(words),
            'original_input': original_input.strip(),
            'evaluation_successful': True
        }

def process_text_input(text_input, error_message):
    # Convert to lowercase, split into words, sort them
    words = sorted(str(text_input).lower().split())
    
    # Return the sorted words as a list with additional information
    return {
        'type': 'text',
        'words': words,
        'original_input': text_input.strip(),
        'word_count': len(words),
        'error': error_message if error_message else None,
        'evaluation_successful': False
    }

def extract_html_attributes(html_string):
    # This is a simplified function to extract HTML attributes
    # In a real-world scenario, you might want to use a proper HTML parser
    start = html_string.lower().find('<html')
    if start == -1:
        return {}
    
    end = html_string.find('>', start)
    if end == -1:
        return {}
    
    attributes_string = html_string[start+5:end].strip()
    attributes = {}
    for attr in attributes_string.split():
        if '=' in attr:
            key, value = attr.split('=', 1)
            attributes[key.strip()] = value.strip().strip('"').strip("'")
        else:
            attributes[attr.strip()] = True
    
    return attributes

def extract_title(html_string):
    # Extract the title from the HTML string
    title_match = re.search(r'<title>(.*?)</title>', html_string, re.IGNORECASE)
    return title_match.group(1).strip() if title_match else None