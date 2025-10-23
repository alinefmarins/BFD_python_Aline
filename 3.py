# 3 - Suponha que você faz parte de uma equipe de desenvolvimento para softwares de astronomia e irá criar um protótipo expansível de sistema solar, para isso siga as definições:
 
# A - Crie uma classe Planeta, 
class Planeta:
   
# ela deve ser inicializada com os parâmetros: nome, raio_equatorial, distancia_do_sol e composicao.   
    def __init__(self, nome, raio_equatorial, distancia_do_sol, composicao):
        self.nome = nome
        self.raio_equatorial = raio_equatorial
        self.distancia_do_sol = distancia_do_sol
        self.composicao = composicao

# B - O raio_equatorial deve ser em km, a distancia_do_sol em milhões de km e composição "Rochoso" ou "Gasoso".
# C - Adicione um método de apresentação, sem parâmetros, que mostre na tela as informações do planeta.
    def exibir_inf(self):
        print(f"Planeta: {self.nome}"s)
        print(f"Raio equatorial: {self.raio_equatorial} km")
        print(f"Distância do Sol: {self.distancia_do_sol} milhões de km")
        print(f"Composição: {self.composicao}")
   

# D - Fora da classe, crie uma função que calcule e retorne o valor da distância do planeta instanciado até o SOL em UA (Unidades Astronômicas, representada pela distância da terra até o Sol, aproximadamente 150 milhões de km).
# Utilize a fórmula: distancia_do_sol / 150.
# Essa função deve receber como parâmetro o atributo distancia_do_sol da classe planeta, ou seja, deve funcionar para qualquer objeto do tipo planeta.
def distancia_em_ua(distancia_milhoes_km):
    distancia_km = distancia_milhoes_km * 100000
    uma_ua_km = 150 * 1000000
    return distancia_km / uma_ua_km

# Pesquisa na internet pelas informações de 3 planetas e as utilize para instanciar 3 objetos. 
mercurio = Planeta("Mercúrio", 2439.7, 57.91, "Rochoso") 
terra = Planeta("Terra", 6378.14, 150.0, "Rochoso")
vênus = Planeta("Júpiter", 6052, 108.2, "Rochoso. ")

# Execute o método de apresentação e a função de distância para cada um dos objetos instanciados.
for planeta in (mercurio, terra, vênus):
    planeta.exibir_inf()
    ua = distancia_em_ua(planeta.distancia_do_sol)
    print(f"Distância de {planeta.nome} ao Sol em UA: {ua:.4f} UA")
    print("________________________________")
