from re import sub, IGNORECASE


def text_to_p_lang(string: str):
    return sub(r'(ij|[aeiou])+', lambda m: m.group() + 'p' + m.group().lower(), string, flags=IGNORECASE)


def p_lang_to_text(string: str):
    return sub(r'((ij|[aeiou])+)p\1', r'\1', string, flags=IGNORECASE)


print(text_to_p_lang("Grandma Eve's cuckoo clock seems broken."))
print(p_lang_to_text("Grapandmapa Epevepe's cupuckoopoo clopock seepeems bropokepen."))
