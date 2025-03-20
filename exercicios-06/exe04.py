tupla = ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)

print(f"NOMES:")
for i in tupla:
    if isinstance(i, str):
        print(f"{i}")

print(f"\nNOTAS:")
for i in tupla:
    if isinstance(i, float):
        print(f"{i}")
