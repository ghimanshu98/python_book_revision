from typing import Optional

class LongNameDict(dict[str, int]):
    """
    an extended dictionary that tracks the longest key it has seen:
    The hint for the class narrowed the generic dict to a more specific dict[str, int]
    the keys are of type str and the values are of type int.
    """
    def longest_key(self) -> Optional[str]:
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest