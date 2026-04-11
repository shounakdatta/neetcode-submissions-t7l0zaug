class Solution:
    esc = '/'
    start = '<'
    end = '>'

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code_s = "<"
            for c in s:
                if c == self.esc or c == self.start or c == self.end:
                    code_s += self.esc
                code_s += c
            code_s += ">"
            code += code_s
        return code

    def decode(self, code: str) -> List[str]:
        print("code:", code)
        strs = []
        s = ""
        i = 0
        while i < len(code):
            if code[i] == self.start:
                s = ""
                i += 1
            if code[i] == self.end:
                strs.append(s)
            if code[i] == self.esc:
                i += 1
            s += code[i]
            i += 1
        return strs

        
