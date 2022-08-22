from io import TextIOWrapper

FILENAME = "cancao-do-exilio.txt"


def open_poem(filename: str, mode: str) -> TextIOWrapper:
    file = open(filename, mode, encoding="utf-8")
    return file


def close_poem(file: TextIOWrapper):
    file.close()


def get_cancao_do_exilio() -> str:
    return """Canção do exílio
Por Gonçalves Dias
Minha terra tem palmeiras
Onde canta o Sabiá,
As aves, que aqui gorjeiam,
Não gorjeiam como lá.
Nosso céu tem mais estrelas,
Nossas várzeas têm mais flores,
Nossos bosques têm mais vida,
Nossa vida mais amores.
Em cismar, sozinho, à noite,
Mais prazer encontro eu lá;
Minha terra tem palmeiras,
Onde canta o Sabiá.
Minha terra tem primores,
Que tais não encontro eu cá;
Em cismar – sozinho, à noite –
Mais prazer encontro eu lá;
Minha terra tem palmeiras,
Onde canta o Sabiá.
Não permita Deus que eu morra,
Sem que eu volte para lá;
Sem que desfrute os primores
Que não encontro por cá;
Sem qu’inda aviste as palmeiras,
Onde canta o Sabiá."""