import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Check for specific HTML document types based on known patterns
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        
        # If not a known type, try to extract and analyze the title
        title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip().lower()
            
            # Categorize based on title content
            if 'data' in title:
                return f"data-related html document detected: {title}"
            elif 'math' in title or 'equation' in title:
                return f"math-related html document detected: {title}"
            elif 'text' in title or 'processing' in title:
                return f"text processing-related html document detected: {title}"
            else:
                return f"html document detected: {title}"
        
        # If no title found, return a generic message
        return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any empty strings and strip whitespace
            cleaned_values = [value.strip() for value in sorted_values if value.strip()]
            
            numeric_values = []
            non_numeric_values = []
            
            for value in cleaned_values:
                if value.replace('.', '', 1).replace('-', '', 1).isdigit():
                    numeric_values.append(float(value))
                else:
                    non_numeric_values.append(value)
            
            # If all values are numbers, sum them up
            if numeric_values and not non_numeric_values:
                return str(sum(numeric_values)).lower()
            else:
                # Process non-numeric values
                processed_values = []
                for value in non_numeric_values:
                    if value.isupper():
                        processed_values.append(value.lower() + " (was all uppercase)")
                    elif len(value) > 20:
                        processed_values.append(value[:20].lower() + "... (truncated)")
                    else:
                        processed_values.append(value.lower())
                
                # Combine numeric and processed non-numeric values
                all_values = [str(sum(numeric_values)).lower()] if numeric_values else []
                all_values.extend(processed_values)
                
                return ','.join(all_values)
        else:
            # Process single value inputs
            if input_data.strip().replace('.', '', 1).replace('-', '', 1).isdigit():
                return str(input_data).lower()
            elif input_data.strip().isupper():
                return input_data.lower() + " (was all uppercase)"
            elif len(input_data) > 50:
                return input_data[:50].lower() + "... (truncated)"
            else:
                return input_data.lower()