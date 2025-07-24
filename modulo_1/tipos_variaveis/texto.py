#Declaração
nome_completo = "Thigas"

nome_completo_aspas = """Thigas
    Re4l"""

nome_completo_quebra = "thigas \
    re4l"

nome = "thigas"
sobrenome = "re4l"

#Formatação
print("Nome completo (1° forma):", nome_completo)
print("Nome completo (2° forma):" + nome_completo)
print("Nome completo (3° forma):" + nome_completo + sobrenome)
print("Nome completo (4° forma):" + nome_completo, sobrenome)
print("Nome completo (5° forma):", nome_completo_aspas, sobrenome)
print("Nome completo (6° forma):", nome_completo_quebra, sobrenome)
print("Nome completo (7° forma): %s" % nome_completo) 
print("Nome completo (8° forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9° forma): {nome} {sobrenome}")
print("Nome completo (9° forma): {} {}".format(nome, sobrenome))