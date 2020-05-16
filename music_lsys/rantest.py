from randomlsys import randomLsys

axiom = 'F+F'
rules = {'F': (['q', 'r', 't'], [0.3, 0.4, 0.3])}
alpha = '+-Fqrt'
ra = randomLsys(axiom, rules, alpha)
print(ra.iterate_for(3))
ra.reset()
print(ra.iterate_for(3))

