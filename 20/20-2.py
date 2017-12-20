class Particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def update(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
        self.v[2] += self.a[2]
        self.p[0] += self.v[0]
        self.p[1] += self.v[1]
        self.p[2] += self.v[2]

    def dist(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])


with open("input.txt", "r") as f:
    data = f.read()[:-1].split('\n')

particles = []

for particle in data:
    vals = particle.split('=')
    p = vals[1].replace('<', '').replace('>', '').split(',')[:3]
    v = vals[2].replace('<', '').replace('>', '').split(',')[:3]
    a = vals[3].replace('<', '').replace('>', '').split(',')[:3]
    p = [int(x) for x in p]
    v = [int(x) for x in v]
    a = [int(x) for x in a]

    particles.append(Particle(p, v, a))

streak = 0

while True:
    if streak > 1000:
        break

    for particle in particles:
        particle.update()

    destroyed = []
    for p0 in particles:
        for p1 in particles:
            if p0 is not p1 and p0.p == p1.p:
                destroyed.append(p0)
                destroyed.append(p1)

    particles = [x for x in particles if x not in destroyed]

    if not destroyed:
        streak += 1
    else:
        streak = 0

print(len(particles))
