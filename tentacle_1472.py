import re
from collections import Counter

def tentacle(input_data):
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Detect specific HTML document types
        if 'data analysis' in input_str:
            return "data analysis html document detected"
        elif 'mathematics' in input_str:
            return "mathematics html document detected"
        elif 'text processing' in input_str:
            return "text processing html document detected"
        elif any(topic in input_str for topic in ['science', 'technology', 'engineering', 'stem']):
            return "stem-related html document detected"
        elif 'wikipedia' in input_str:
            # Check for specific Wikipedia topics
            if 'data analysis' in input_str:
                return "wikipedia data analysis html document detected"
            elif 'mathematics' in input_str:
                return "wikipedia mathematics html document detected"
            elif 'text processing' in input_str:
                return "wikipedia text processing html document detected"
            else:
                return "wikipedia html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process as text
        if ',' in input_str:
            # Process as a comma-separated list
            items = [item.strip() for item in input_str.split(',') if item.strip()]
            
            # Perform basic data analysis on the list
            item_count = len(items)
            unique_items = len(set(items))
            most_common = Counter(items).most_common(1)[0] if items else ('', 0)
            
            sorted_list = sorted(items)
            return f"sorted list: {','.join(sorted_list)}. analysis: {item_count} items, {unique_items} unique, most common: {most_common[0]} ({most_common[1]} occurrences)"
        
        else:
            # Process as a single text input
            if input_str.isdigit():
                return f"positive integer: {input_str}"
            elif input_str.replace('.', '').isdigit():
                return f"decimal number: {input_str}"
            elif input_str.replace('-', '').isdigit():
                return f"negative number: {input_str}"
            elif input_str.startswith('http://') or input_str.startswith('https://'):
                return f"url detected: {input_str}"
            elif '@' in input_str and '.' in input_str.split('@')[-1]:
                return f"email address detected: {input_str}"
            elif input_str == 'true' or input_str == 'false':
                return f"boolean value: {input_str}"
            elif input_str.startswith('0x') and all(c in '0123456789abcdef' for c in input_str[2:]):
                return f"hexadecimal number: {input_str}"
            else:
                # Perform text analysis
                word_count = len(input_str.split())
                char_count = len(input_str)
                unique_words = len(set(input_str.split()))
                most_common_word = Counter(input_str.split()).most_common(1)[0] if word_count > 0 else ('', 0)
                
                # Check for specific patterns or topics
                if re.search(r'\b(data|analysis|statistics)\b', input_str):
                    return f"text input related to data analysis: {input_str}. analysis: {word_count} words, {char_count} characters, {unique_words} unique words, most common: {most_common_word[0]} ({most_common_word[1]} occurrences)"
                elif re.search(r'\b(math|equation|formula)\b', input_str):
                    return f"text input related to mathematics: {input_str}. analysis: {word_count} words, {char_count} characters, {unique_words} unique words, most common: {most_common_word[0]} ({most_common_word[1]} occurrences)"
                elif re.search(r'\b(text|processing|nlp)\b', input_str):
                    return f"text input related to text processing: {input_str}. analysis: {word_count} words, {char_count} characters, {unique_words} unique words, most common: {most_common_word[0]} ({most_common_word[1]} occurrences)"
                else:
                    return f"text input: {input_str}. analysis: {word_count} words, {char_count} characters, {unique_words} unique words, most common: {most_common_word[0]} ({most_common_word[1]} occurrences)"