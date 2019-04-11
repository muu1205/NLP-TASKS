import numpy

A = "One of the finer books I read this year was John Kaag's Hiking With Nietzsche, in which Kaag,a professor of philosophy, rekindles his passion for the German thinker while tracing picturesque hiking trails in the mountains of Switzerland . I t's a near precise rendering of the travelogue as a self - helpbook. A young Kaag was an avowed Nietzsche acolyte but given the ravages of responsibilities and adulthood, the writer put his affinity to test by under taking physically enduring hikes through the Alps, revisiting haunts that the philosopher escaped to, in search of solitude and salve. The journey's demands, coupled with his own inner turmoil, are catnip for anybody feeling at cross purposes with their own life."
B = "If there is a phrase I would prefer to from online bios, personal or rosa it is, I love travel. Or some point.Or some approximation of that sentiment. To clarify I am not against travellers or those who prouldy flaunt their passion for travel. On the contrary a editing a travel magazine has now made me oddly protective of travellers and submission is that love to travel suggested so casually just doesn't feel adequate to depth of emotion if sparks in true devotoees"

wordsA = A.lower().split()
wordsB = B.lower().split()
print(wordsA)
print(wordsB)


vocab = set(wordsA)
vocab = vocab.union(set(wordsB))
print(vocab)

vocab = list(vocab)
print(vocab)

vA = numpy.zeros(len(vocab), dtype=float)
vB = numpy.zeros(len(vocab), dtype=float)

for w in wordsA:
    i = vocab.index(w)
    vA[i] += 1

print(vA)

for w in wordsB:
    i = vocab.index(w)
    vB[i] += 1

print(vB)

cos = numpy.dot(vA, vB) / (numpy.sqrt(numpy.dot(vA,vA)) * numpy.sqrt(numpy.dot(vB,vB)))
print(cos)