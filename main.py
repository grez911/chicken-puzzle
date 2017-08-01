import chickens

ROUNDS = 100000

c = chickens.Chickens()
gen = c.gen_rounds()
overal_unpecked = 0

for i in range(0, ROUNDS):
    next(gen)
    overal_unpecked += c.result()

print("Number of rounds: %d" % ROUNDS)
print("Average of unpecked: %.5f" % (overal_unpecked / ROUNDS))
