from collections import Counter
import math
documents=["transformer uses attention mechanism","cnn is widely used for image processing",
           "clip connects images and text","python is useful for artificial intelligence","neural networks learn parameters from data"]
def tokenize(text):
    return text.lower().split()
def create_vector(text):
    words=tokenize(text)
    return Counter(words)
def cosine_similarity(vector1,vector2):
    common_words=set(vector1.keys())&set(vector2.keys())
    dot_product=sum(vector1[word]*vector2[word]
    for word in common_words                )
    norm1=math.sqrt(sum(value**2 for value in vector1.values()))
    norm2=math.sqrt(sum(value**2 for value in vector2.values()))
    if norm1==0 or norm2==0:
        return 0
    return dot_product/(norm1*norm2)
query=input("请输入搜索内容：")
query_vector=create_vector(query)
results=[]
for document in documents:
    document_vector=create_vector(document)
    similarity=cosine_similarity(query_vector,document_vector)
    results.append({"text":document,"score":similarity})
results.sort(key=lambda x:x["score"],reverse=True)
print("\n----------搜索-----------")
for result in results:
        print(f"{result['score']:.3f}"f"{result['text']}")

   