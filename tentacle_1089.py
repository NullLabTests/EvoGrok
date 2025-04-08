def tentacle(input_data):
    # Convert input to string, strip whitespace, and convert to lowercase
    input_str = str(input_data).strip().lower()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific Wikipedia page titles
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
            sorted_elements = sorted(input_str.split(','))
            # Reverse each element before joining
            reversed_elements = [elem[::-1] for elem in sorted_elements]
            return ','.join(reversed_elements)
        elif input_str.isdigit():
            # If input is a number, return it as a string, its square, its cube, and its factorial
            number = int(input_str)
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            return f"{input_str}, square: {number**2}, cube: {number**3}, factorial: {factorial}"
        elif input_str.startswith('lang='):
            # If input starts with 'lang=', process it as a language code
            lang_code = input_str.split('=')[1]
            if lang_code == 'en':
                return "english language detected"
            elif lang_code == 'es':
                return "spanish language detected"
            elif lang_code == 'fr':
                return "french language detected"
            else:
                return f"language code detected: {lang_code}"
        elif input_str.startswith('url='):
            # If input starts with 'url=', process it as a URL
            url = input_str.split('=')[1]
            if url.startswith('https://'):
                return f"secure url detected: {url}"
            elif url.startswith('http://'):
                return f"insecure url detected: {url}"
            else:
                return f"url detected: {url}"
        elif input_str.startswith('date='):
            # If input starts with 'date=', process it as a date
            try:
                from datetime import datetime
                date = datetime.strptime(input_str.split('=')[1], '%Y-%m-%d')
                return f"date detected: {date.strftime('%B %d, %Y')}"
            except ValueError:
                return "invalid date format detected"
        else:
            # For other inputs, reverse the string, capitalize the first letter, and add a prefix
            reversed_str = input_str[::-1]
            return f"processed: {reversed_str.capitalize()}"