import re
from statistics import mean, median

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of Wikipedia HTML document based on known patterns
        if re.search(r'<title>\s*Data analysis\s*</title>', input_data, re.IGNORECASE):
            return "wikipedia data analysis html document detected"
        elif re.search(r'<title>\s*Mathematics\s*</title>', input_data, re.IGNORECASE):
            return "wikipedia mathematics html document detected"
        elif re.search(r'<title>\s*Text processing\s*</title>', input_data, re.IGNORECASE):
            return "wikipedia text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add a prefix
        return f"math result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values, then lowercase
            sorted_values = sorted(input_data.split(','))
            # Check if all values are numeric
            if all(value.strip().replace('.', '').isdigit() for value in sorted_values):
                # If numeric, calculate statistics
                numeric_values = [float(value.strip()) for value in sorted_values]
                stats = {
                    'sum': sum(numeric_values),
                    'average': mean(numeric_values),
                    'median': median(numeric_values),
                    'min': min(numeric_values),
                    'max': max(numeric_values)
                }
                return f"numeric input: {', '.join(f'{k}={v:.2f}' for k, v in stats.items())}"
            else:
                # If not numeric, return sorted values and count unique values
                unique_count = len(set(sorted_values))
                return f"string input: {','.join(sorted_values).lower()}, unique values: {unique_count}"
        else:
            # Process single string input
            cleaned_input = ''.join(char.lower() for char in input_data if char.isalnum())
            is_palindrome = cleaned_input == cleaned_input[::-1]
            word_count = len(re.findall(r'\b\w+\b', input_data))
            
            # Check for common programming language keywords
            programming_languages = {
                'python': ['def', 'class', 'import', 'if', 'else', 'for', 'while'],
                'javascript': ['function', 'let', 'const', 'if', 'else', 'for', 'while'],
                'java': ['public', 'class', 'static', 'void', 'if', 'else', 'for', 'while']
            }
            detected_languages = []
            for lang, keywords in programming_languages.items():
                if any(keyword in input_data.lower() for keyword in keywords):
                    detected_languages.append(lang)
            
            result = f"string input: {str(input_data).lower()}, palindrome: {is_palindrome}, word count: {word_count}"
            if detected_languages:
                result += f", possible programming language(s): {', '.join(detected_languages)}"
            
            return result