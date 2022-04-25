"""
    Fazendo uso de Annotations
    -> Nos ajudam a utilizar o type hints
    -> Ex: def cabecalho(texto: *str*) -> *str*:
        -> str = ANNOTATION
    -> os espaços fazem parte da formatação de Annotations
    -> ExErrado: texto:str, texto : str,
    -> ExErrado: ()->str , () ->str
    -> ExErrado: alinhamento:bool=true

    -> METODO DUNDER ANNOTATIONS:
        ->EX: metodo.__annotations__
            Resp: {metodo: type, return: type}
        ->OBS: Precisa ser usado em um metodo.
            Resp: __init__.__annotations__
"""
#Ex:
nome: str = 'Geek University'

peso: float = 6.55

ativo: bool = True

