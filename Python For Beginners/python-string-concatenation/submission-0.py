def concatenate(s1: str, s2: str) -> str:
    str_combined = s1 + s2
    if len(str_combined) <= 10:
        return str_combined
    else:
        return "Too long!"




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
