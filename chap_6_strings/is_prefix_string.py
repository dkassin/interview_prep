def is_prefix_string(s: str, words) -> bool:
    for i in range(len(words)):
          if "".join(words[:i+1]) == s:
               return True
    return False