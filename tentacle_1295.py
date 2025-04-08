import math
import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Detect specific types of HTML documents
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # Count the number of classes and ids in the HTML
            class_count = len(re.findall(r'class="[^"]*"', lowercase_input))
            id_count = len(re.findall(r'id="[^"]*"', lowercase_input))
            return f"generic html document detected with {class_count} classes and {id_count} ids"

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, lowercase it, and add various mathematical operations
        result_str = str(result).lower()
        if isinstance(result, (int, float)):
            operations = {
                "square": result**2,
                "cube": result**3,
                "square root": math.sqrt(abs(result)),
                "absolute value": abs(result),
                "factorial": math.factorial(int(result)) if result.is_integer() and 0 <= result <= 20 else "n/a",
            }
            return f"{result_str}, " + ", ".join(f"{key}: {value:.2f}" for key, value in operations.items())
        else:
            return result_str
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, lowercase it, capitalize the first letter, and join them
            processed_items = [item[::-1].lower().capitalize() for item in sorted_items]
            # Calculate the average length of the processed items
            avg_length = sum(len(item) for item in processed_items) / len(processed_items)
            return f"{','.join(processed_items)}, average length: {avg_length:.2f}"
        elif input_data.isdigit():
            # If it's a single number, return various mathematical operations
            number = int(input_data)
            operations = {
                "square": number ** 2,
                "cube": number ** 3,
                "factorial": math.factorial(number),
                "fibonacci": sum(int((5**0.5 * (1 + 5**0.5)/2)**n - int((5**0.5 * (1 + 5**0.5)/2)**n)) for n in range(number+1)),
                "prime": "yes" if all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1)) else "no",
            }
            return ", ".join(f"{key}: {value}" for key, value in operations.items())
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return various text analysis results
            lowercase_input = input_data.lower()
            vowels = sum(1 for char in lowercase_input if char in 'aeiou')
            consonants = sum(1 for char in lowercase_input if char.isalpha() and char not in 'aeiou')
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, first three: {input_data[:3]}, last three: {input_data[-3:]}, vowel count: {vowels}, consonant count: {consonants}"
        else:
            # For other inputs, perform comprehensive analysis
            reversed_cleaned = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            vowels = sum(1 for char in reversed_cleaned if char in 'aeiou')
            ascii_sum = sum(ord(char) for char in reversed_cleaned)
            digit_sum = sum(int(char) for char in reversed_cleaned if char.isdigit())
            word_count = len(re.findall(r'\b\w+\b', input_data))
            return f"{reversed_cleaned}, vowel count: {vowels}, ascii sum: {ascii_sum}, digit sum: {digit_sum}, word count: {word_count}"