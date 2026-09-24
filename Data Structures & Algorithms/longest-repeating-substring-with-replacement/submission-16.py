
class Solution:

    def characterReplacement(self, s: str, k: int) -> int:

        i = 0
        j = 0
        fl = 0

        freq = {}

        while j < len(s):

            freq[s[j]] = freq.get(s[j], 0) + 1

            maxfreq = max(freq.values())

            window = j - i + 1

            req = window - maxfreq

            if req <= k:
                fl = max(fl, window)

            else:
                freq[s[i]] -= 1
                i += 1

            j += 1

        return fl
        