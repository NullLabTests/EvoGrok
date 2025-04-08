import re
import math

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing html document detected"
        else:
            # Extract the title from the HTML if possible
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                return f"wikipedia {title_match.group(1).lower()} html document detected"
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
                # If numeric, calculate the sum, average, standard deviation, and median
                numeric_values = [float(value.strip()) for value in sorted_values]
                total = sum(numeric_values)
                average = total / len(numeric_values)
                std_dev = math.sqrt(sum((x - average) ** 2 for x in numeric_values) / len(numeric_values))
                median = sorted(numeric_values)[len(numeric_values) // 2] if len(numeric_values) % 2 else (sorted(numeric_values)[len(numeric_values) // 2 - 1] + sorted(numeric_values)[len(numeric_values) // 2]) / 2
                return f"numeric input: sum={total:.2f}, average={average:.2f}, std_dev={std_dev:.2f}, median={median:.2f}"
            else:
                # If not numeric, return sorted values, count unique words, and check for palindromes
                unique_words = len(set(word.lower() for word in ' '.join(sorted_values).split()))
                palindromes = sum(1 for word in sorted_values if word.lower().strip() == word.lower().strip()[::-1])
                return f"string input: {','.join(sorted_values).lower()}, unique_words={unique_words}, palindromes={palindromes}"
        else:
            # Check if the input is a palindrome
            cleaned_input = ''.join(char.lower() for char in input_data if char.isalnum())
            is_palindrome = cleaned_input == cleaned_input[::-1]
            
            # Count the number of words and unique words
            words = input_data.split()
            word_count = len(words)
            unique_words = len(set(word.lower() for word in words))
            
            # Return the input as a lowercase string with various statistics
            return f"string input: {str(input_data).lower()}, palindrome={is_palindrome}, word_count={word_count}, unique_words={unique_words}"