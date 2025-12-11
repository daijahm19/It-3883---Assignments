coin_values = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

sentence = "1 penny and 2 nickels"
sentence = sentence.replace(" and ", ", ")
parts = sentence.split(", ")

total = 0.0

for part in parts:
    words = part.strip().split()
    qty = int(words[0])
    coin = words[1].lower().rstrip("s")  
    if coin in coin_values:
        total += qty * coin_values[coin]

print(f"{total:.2f}")
