from GradiniteMiniProiect.ClaseGradinita.GradinitaPrivata import GradinitaPrivata
from GradiniteMiniProiect.ClaseGradinita.GradinitaPublica import GradinitaPublica
from GradiniteMiniProiect.ClaseGradinita.GradinitaPublica25 import GradinitaPublica25


if __name__ == '__main__':
    gradinita_privata1 = GradinitaPrivata()
    gradinita_privata1.activitate_practica()
    gradinita_privata1.ora_de_somn()

    gradinita_publica = GradinitaPublica()
    gradinita_publica.activitate_practica()
    gradinita_publica.ora_de_somn()

    gradinita_publica25 = GradinitaPublica25()
    gradinita_publica25.activitate_practica()

    gradinita_publica25.calcul_buline()

    gradinita_publica25.introd_informatii_elevi()



