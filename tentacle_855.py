import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia text processing html document detected"
        else:
            # Attempt to extract the title from the HTML
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip().lower()
                # Check for common keywords in the title
                if 'data' in title or 'analysis' in title:
                    return f"data-related html document detected: {title}"
                elif 'math' in title or 'equation' in title:
                    return f"math-related html document detected: {title}"
                elif 'text' in title or 'processing' in title:
                    return f"text processing html document detected: {title}"
                else:
                    return f"html document detected: {title}"
            else:
                # Attempt to extract meta description
                meta_match = re.search(r'<meta name="description" content="(.*?)"', input_data, re.IGNORECASE)
                if meta_match:
                    return f"html document with description: {meta_match.group(1).strip().lower()}"
                else:
                    return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Check if the result is a number
        if isinstance(result, (int, float)):
            return f"numerical result: {str(result).lower()}"
        else:
            return f"non-numerical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if isinstance(input_data, str):
            # Check for comma-separated values
            if ',' in input_data:
                # Sort and join comma-separated values, then convert to lowercase
                sorted_values = sorted(input_data.split(','))
                return f"sorted values: {','.join(sorted_values).lower()}"
            # Check for potential list or dictionary
            elif input_data.strip().startswith('[') and input_data.strip().endswith(']'):
                try:
                    # Attempt to parse as a list
                    parsed_list = eval(input_data)
                    # Check if all elements are numbers
                    if all(isinstance(item, (int, float)) for item in parsed_list):
                        return f"numerical list detected: {','.join(map(str, sorted(parsed_list))).lower()}"
                    else:
                        return f"list detected: {','.join(map(str, parsed_list)).lower()}"
                except:
                    pass
            elif input_data.strip().startswith('{') and input_data.strip().endswith('}'):
                try:
                    # Attempt to parse as a dictionary
                    parsed_dict = eval(input_data)
                    # Sort dictionary by keys
                    sorted_items = sorted(parsed_dict.items())
                    return f"sorted dictionary detected: {','.join(f'{k}:{v}' for k,v in sorted_items).lower()}"
                except:
                    pass
        
        # Check for potential mathematical expression
        if any(char in input_data for char in '+-*/^%'):
            return f"unevaluated mathematical expression: {input_data.lower()}"
        
        # If no special processing applies, return the input as a lowercase string
        return str(input_data).lower()