

def verifica_romano(romano):
    for i in romano:
        if i in 'IVXLCDM':
            resultado = True
        else:
            resultado = i
            break     
    return resultado

def romano_para_inteiro(romano):
    validador = verifica_romano(romano) 
    if validador == True:
        tam_romano = len(romano)
        inteiro = 0
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(tam_romano):
            atual =  romano[i]
            try:
                prox = romano[i+1]
            except IndexError: 
                prox = False
            if (prox and dic[atual] < dic[prox]):
                inteiro -= dic[atual]
            else:
                inteiro += dic[atual]
        return inteiro
    else:
        return validador 