def tentacle(input_data):
    # Convert input to string and strip whitespace
    input_str = str(input_data).strip().lower()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific Wikipedia page titles based on knowledge
        if 'data analysis' in input_str:
            return "wikipedia page on data analysis detected"
        elif 'mathematics' in input_str:
            return "wikipedia page on mathematics detected"
        elif 'text processing' in input_str:
            return "wikipedia page on text processing detected"
        else:
            return "html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_str)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_str:
            # If input contains commas, sort and join the elements
            sorted_items = sorted(input_str.split(','))
            # Reverse each item before joining
            reversed_items = [item[::-1] for item in sorted_items]
            # Add new feature: capitalize the first letter of each item
            capitalized_items = [item.capitalize() for item in reversed_items]
            return ','.join(capitalized_items)
        elif input_str.isdigit():
            # If input is a number, return its square as a string
            return str(int(input_str) ** 2)
        elif input_str.isalpha():
            # If input is alphabetic, reverse the string and capitalize it
            return input_str[::-1].capitalize()
        elif any(char.isdigit() for char in input_str):
            # If input contains numbers, extract and sum them
            numbers = [int(char) for char in input_str if char.isdigit()]
            # Add new feature: return the product if there are multiple numbers
            if len(numbers) > 1:
                product = 1
                for num in numbers:
                    product *= num
                return f"sum: {sum(numbers)}, product: {product}"
            else:
                return str(sum(numbers))
        else:
            # For other inputs, return the first and last characters, 
            # and the length of the string
            if len(input_str) > 1:
                return f"{input_str[0]}{len(input_str)}{input_str[-1]}"
            else:
                # Add new feature: if single character, return it capitalized
                return input_str.capitalize()