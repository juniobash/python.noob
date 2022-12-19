#estrutura de repeticao em python
#for

# percorre a string e retorna item a item
tituloLivro = "caibalion"
for letra in tituloLivro :
	print(letra)

# percorre string e retorna a posicao
nome = "samuel oliveira"
for posicao, letra in enumerate(nome) :
	print(f"Posição: {posicao}, letra: {letra}")
