def descomprime_fichero(origen, destino):
    """función que descomprime un fichero de nucleótidos comprimido y guarda el resultado
    en otro fichero
    Args:
        origen (str): ruta hacia el fichero comprimido
        destino (str): ruta hacia el fichero donde se guardarán los datos originales
    """
    pass

def descomprime(txt):
    """función auxiliar que descomprime una línea del fichero comprimido y la devuelve en su formato original

    Args:
        txt (str): línea de texto que representa una secuencia de nucleótidos en formato comprimido

    Returns:
        str: secuencia de nucleótidos
    """
    pass

def check_Ok(descomprimido, original):
    """función que comprueba si el fichero generado por nosotros coincide con el original

    Args:
        descomprimido (str): ruta hacia el fichero descomprimido por nosotros
        original (str): ruta hacia el fichero original

    Returns:
        bool: Devuelve True si el fichero descomprimido coincide con el original
    """
    ok=True
    fd=open(descomprimido, encoding='utf-8')
    fo=open(original, encoding='utf-8')
    for linea1,linea2 in zip(fd,fo):
        ok=linea1==linea2
        if not ok:
            break
    fd.close()
    fo.close()
    return ok

######################################### Test ################################################
if __name__ == '__main__':
    '''
    Realice las siguientes pruebas:
    1.- descomprima el fichero 'sacCer3cmp.txt' y guardelo en el fichero 'sacCer3descmp.txt' 
        (ambos en la ruta de la carpeta 'data')
    2.- Compruebe que el algoritmo funciona usando el método 'ckeck_Ok', que toma como parámetros
        la ruta hacia el fichero que usted ha generado ('sacCer3descmp.txt'), y la ruta hacia 
        el fichero original ('sacCer3.txt')
    '''
    pass
