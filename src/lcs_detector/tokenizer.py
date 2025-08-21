import re

KW = {"if","else","for","while","return","class","def","public","private","static",
      "void","int","float","double","true","false","null","try","except","finally","import"}

MULTI = {"==","!=", "<=", ">=", "&&", "||", "++", "--", "+=", "-=", "*=", "/=", "%=", "<<", ">>", "->", "::", ":=", "**"}
DELIMS = set("()[]{};:,.")
OPS = set("+-*/%=<>&|^~!?")

def _strip_comments(s: str) -> str:
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)      # /* ... */
    s = re.sub(r"//.*?$", "", s, flags=re.M)         # // ...
    s = re.sub(r"(?m)#.*$", "", s)                   # # ...
    return s

def Tokenizar(code: str):
    code = _strip_comments(code)
    out = []
    i, n = 0, len(code)
    while i < n:
        c = code[i]
        if c.isspace():
            i += 1; continue

        # strings '...' o "..."
        if c in "'\"":
            j = i+1; esc = False
            while j < n and (esc or code[j] != c):
                esc = (code[j] == "\\") and not esc
                j += 1
            i = min(j+1, n)
            out.append("STR"); continue

        # identificadores / keywords
        if c.isalpha() or c == "_":
            j = i+1
            while j < n and (code[j].isalnum() or code[j] == "_"): j += 1
            w = code[i:j]
            out.append(f"KW:{w}" if w in KW else "ID")
            i = j; continue

        # números
        if c.isdigit():
            j = i+1
            while j < n and (code[j].isdigit() or code[j] == "."): j += 1
            out.append("NUM"); i = j; continue

        # operadores y delimitadores
        if i+1 < n and code[i:i+2] in MULTI:
            out.append(f"OP:{code[i:i+2]}"); i += 2; continue
        if c in DELIMS:
            out.append(f"DELIM:{c}"); i += 1; continue
        if c in OPS:
            out.append(f"OP:{c}"); i += 1; continue

        i += 1
    return out
