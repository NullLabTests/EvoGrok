import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing html document detected"
        else:
            # If no specific type is detected, check for other keywords
            if 'wikipedia' in input_data.lower():
                return "wikipedia generic html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, remove extra whitespace, and sort any comma-separated values
        processed_result = re.sub(r'\s+', ' ', str(result).lower()).strip()
        if ',' in processed_result:
            sorted_values = sorted(processed_result.split(','))
            return ','.join(sorted_values)
        return processed_result
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove extra whitespace from each value and convert to lowercase
            cleaned_values = [re.sub(r'\s+', ' ', value.strip().lower()) for value in sorted_values]
            return ','.join(cleaned_values)
        else:
            # Convert to lowercase, remove extra whitespace, and replace multiple spaces with a single space
            return re.sub(r'\s+', ' ', input_data.lower()).strip()