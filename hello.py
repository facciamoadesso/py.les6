password = input("Введите пароль: ")


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)
    
    
def is_very_long(password):
    return len(password) > 12
 
 
def has_letters(password):
    return any(symbol.isalpha() for symbol in password)
    
    
def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)
    
    
def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)
    
    
def has_symbols(password):
    return any(not symbol.isalnum() for symbol in password)
    
    
checks = [has_digit, is_very_long, has_letters, has_upper_letters, has_lower_letters, has_symbols]
    
score = sum(2 for check in checks if check(password))
        
print("Рейтинг пароля: ", score)
