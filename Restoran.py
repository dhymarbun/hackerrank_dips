def Konso(e, L):
    return [e] + L

def IsEmpty(S):
    return S == []

def KonsLo(L, S):
    return [L] + S

def FirstList(S):
    return S[0]

def TailList(S):
    return S[1:]

def IsAtom(S):
    return type(S) != list

def IsList(S):
    return type(S) == list

def FirstElmt(L):
    return L[0]

def Tail(L):
    return L[1:]

def NBLoL(S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(FirstList(S)):
            return 1 + NBLoL(TailList(S))
        elif IsList(FirstList(S)):
            return NBLoL(FirstList(S)) + NBLoL(TailList(S))

def SumLoL(S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(FirstList(S)):
            return FirstList(S) + SumLoL(TailList(S))
        elif IsList(FirstList(S)):
            return SumLoL(FirstList(S)) + SumLoL(TailList(S))

def AverageLoL(S):
    return SumLoL(S) / NBLoL(S)

def ListCheck(S, avgfix):
    if IsEmpty(S):
        return []
    else:
        if FirstElmt(S) >= avgfix:
            return Konso(FirstElmt(S), ListCheck(Tail(S), avgfix))
        else:
            return ListCheck(Tail(S), avgfix)

def Check(daftar_rating, avgfix):
    if IsEmpty(daftar_rating):
        return []
    else:
        return KonsLo(ListCheck(FirstList(daftar_rating), avgfix), Check(TailList(daftar_rating), avgfix))

def rating(daftar_rating):
    avgfix = AverageLoL(daftar_rating)
    return Check(daftar_rating, avgfix)

print(eval(input()))