import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Detect specific types of Wikipedia HTML documents
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input and 'lang="en"' in lowercase_input:
            return "wikipedia english text processing html document detected"
        
        # Attempt to extract the title from the HTML
        title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).lower()
            return f"wikipedia {title} html document detected"
        
        # Check for other known HTML document types
        if 'xmlns="http://www.w3.org/1999/xhtml"' in lowercase_input:
            return "xhtml document detected"
        elif '<!DOCTYPE html>' in lowercase_input:
            return "html5 document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove extra whitespace from each value
            cleaned_values = [re.sub(r'\s+', ' ', value).strip() for value in sorted_values]
            # Join the cleaned values
            result = ','.join(cleaned_values)
            
            # Check if the result looks like a list of numbers
            if all(re.match(r'^-?\d+(\.\d+)?$', value) for value in cleaned_values):
                # Calculate and return the sum, average, and count of the numbers
                numbers = [float(value) for value in cleaned_values]
                return f"sum: {sum(numbers)}, average: {sum(numbers)/len(numbers)}, count: {len(numbers)}"
            else:
                return result
        else:
            # Convert to lowercase and remove extra whitespace
            cleaned_input = re.sub(r'\s+', ' ', input_data.lower()).strip()
            
            # Check for specific patterns in the input
            if cleaned_input.startswith('wikipedia: '):
                return f"wikipedia page detected: {cleaned_input[11:]}"
            elif re.match(r'^https?://', cleaned_input):
                # Extract domain from URL
                domain_match = re.search(r'://([^/]+)', cleaned_input)
                domain = domain_match.group(1) if domain_match else "unknown"
                return f"url detected: {domain}"
            elif re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', cleaned_input):
                # Extract domain from email address
                domain_match = re.search(r'@([^@]+)$', cleaned_input)
                domain = domain_match.group(1) if domain_match else "unknown"
                return f"email address detected: {domain}"
            elif re.match(r'^\d{4}-\d{2}-\d{2}$', cleaned_input):
                return f"date detected: {cleaned_input}"
            else:
                # Count words in the input
                word_count = len(cleaned_input.split())
                return f"text input: {word_count} words"