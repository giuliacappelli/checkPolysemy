from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
import itertools

# quantifies the polysemy of verbs in a list

verbs = ["break", "build", "chop", "clean", "cook", "cut", "drink", "eat", "embroider", "pour", "sew", "steal", "wash", "watch", "write", "behead", "devour", "doodle", "kill", "knife", "poison", "sign", "sip", "smoke", "swig", "polish", "teach", "sing", "hum", "slice"]

for v in verbs:
	synsets = wn.synsets(v, pos='v', lang='eng')

	simlist = []
	for synset1, synset2 in itertools.combinations(synsets, 2):
		similarity = wn.wup_similarity(synset1, synset2) # Wu-Palmer similarity score
		simlist.append(similarity)
	if len(simlist) != 0:
		critical = [i for i in simlist if i < 0.15] # bank1-2 0.1428, bank 1-6 0.1538 (typical textbook examples for polysemy)

		# UNCOMMENT TO QUANTIFY POLYSEMY OF VERB
		# print(v, len(critical), " out of ", len(simlist))

		# UNCOMMENT TO PRINT OUT ONLY POLYSEMOUS VERBS (having more than 20% of different word senses)
		if len(critical)/len(simlist) >= 0.20:
			print(v, len(critical), " out of ", len(simlist))
