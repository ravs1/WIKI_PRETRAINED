from gensim.models import Word2Vec

model = Word2Vec.load("/Users/ravs/Documents/en_1000_no_stem/en_1000_no_stem/en.model")
#print(model.similarity('woman', 'man'))
print(model.most_similar('prostitute'))


def nearest_similarity_cosmul(start1, end1, end2):
    similarities = model.most_similar_cosmul(
        positive=[end2, start1],
        negative=[end1]
    )
    start2 = similarities[0][0]
    print("{start1} is related to {end1}, as {start2} is related to {end2}".format(**locals()))
    return start2

nearest_similarity_cosmul("men", "engineer", "women")
#nearest_similarity_cosmul("men", "homemaker", "women")
#nearest_similarity_cosmul("men", "king", "women")
