salario = float(input())
imposto = 0.0

if salario <= 2000.00:
    print("Isento")
else:
    # Faixa 8% (de R$ 2000.01 até R$ 3000.00)
    if salario > 2000.00:
        faixa_8 = min(salario, 3000.00) - 2000.00
        imposto += faixa_8 * 0.08
    
    # Faixa 18% (de R$ 3000.01 até R$ 4500.00)
    if salario > 3000.00:
        faixa_18 = min(salario, 4500.00) - 3000.00
        imposto += faixa_18 * 0.18
    
    # Faixa 28% (acima de R$ 4500.00)
    if salario > 4500.00:
        faixa_28 = salario - 4500.00
        imposto += faixa_28 * 0.28
    
    print(f"R$ {imposto:.2f}")