
def num_words(param, child=False):    
    ret = ""
    
    """Dicionario de dados"""
    ones = {"0": "zero", "1": "um", "2": "dois","3": "tres","4": "quatro", "5": "cinco", "6": "seis", "7": "sete",
            "8": "oito", "9": "nove"}
    tens = {"10": "dez", "11": "onze", "12": "doze", "13": "treze", "14": "catorze", "15": "quinze", "16": "dezesseis",
            "17": "dezessete", "18": "dezoito", "19": "dezenove"}
    decs = {"2": "vinte", "3": "trinta", "4": "quarenta", "5": "cinquenta", "6": "sessenta", "7": "setenta",
            "8": "oitenta", "9": "noventa"}
    hunds = {"100": "cem", "1": "cento", "2": "duzentos", "3": "trezentos", "4": "quatrocentos", "5": "quinhentos",
             "6": "seiscentos", "7": "setecentos", "8": "oitocentos", "9": "novecentos"}
    
    """Controle numero negativo"""
    if param < 0:
        param = param * -1
        ret = "menos "

        # controle intervalo negativo
        if param < -99999:
            return "Numero fora do intervalo"

    # unidades
    if 0 <= param <= 9:
        ret += ones.get(str(param))
    
    # dezenas
    elif 9 < param <= 19:
        ret += tens.get(str(param))

    # decimais
    elif 19 < param <= 99:
        ret += decs.get(str(param // 10))
        if (param % 10) > 0:
            ret += ' e ' + num_words((param % 10))

    # centenas
    elif 99 < param <= 999:
        if param == 100:
            ret += hunds.get(str(param))
        else:
            ret += hunds.get(str(param // 100))
            if (param % 100) > 0:
                ret += ' e ' + num_words(param % 100)
    
    # milhares
    elif 999 < param <= 9999:
        if str(param)[0] == '1' and not child:
            ret += 'mil'
        else:
            ret += ones.get(str(param // 1000))
            ret += ' mil'

        if (param % 1000) > 0:
            ret += ' e ' + num_words(param % 1000)

    # dezenas de milhares
    elif 9999 < param <= 19999:
        ret += tens.get(str(param // 1000))        
        if (param % 1000) > 0:
            ret_aux = num_words(param % 1000, True)
            if 'mil' in ret_aux:
                ret += ' e ' + ret_aux
            else:
                ret += ' mil e ' + ret_aux
        else:
            ret += ' mil'

    # decimais dos milhares
    elif 19999 < param <= 99999:
        ret += decs.get(str(param // 10000))
        if (param % 10000) > 0:
            ret_aux = num_words(param % 10000, True)
            if 'mil' in ret_aux:
                ret += ' e ' + ret_aux
            else:
                ret += ' mil e ' + ret_aux
        else:
            ret += ' mil'

    # controle intervalo positivo
    elif param > 99999:
        return "Numero fora do intervalo"
    
    return ret
