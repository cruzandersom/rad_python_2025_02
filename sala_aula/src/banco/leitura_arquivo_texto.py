# Leitura do arquivo;
with open('meuarquivo.txt', 'r') as f:
    conteudo = f.read()  # Lê todo o conteúdo do arquivo
    print(conteudo)

# escrita do arquivo;
with open('meuarquivo.txt', 'w') as f:
    f.write("Esta é a primeira linha.\n")
    f.write("Esta é a segunda linha.")

# anexar ao arquivo;
with open('meuarquivo.txt', 'a') as f:
    f.write("\nEsta linha foi adicionada depois.")
