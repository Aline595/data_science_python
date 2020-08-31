from collections import Counter
#Definir lista: coleção de itens mutaveis
users = [
  # Dicionario(pares de chave e valor)
  {"id": 0, "name": "Hero"},
  {"id": 1, "name": "Dunn"},
  {"id": 2, "name": "Sue"},
  {"id": 3, "name": "Chi"},
  {"id": 4, "name": "Thor"},
  {"id": 5, "name": "Clive"},
  {"id": 6, "name": "Hick"},
  {"id": 7, "name": "Devin"},
  {"id": 8, "name": "Kate"},
  {"id": 9, "name": "Klein"},
]

friendships = [
  #Tupla: Coleção de itens imutavel
  (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5),
  (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

for user in users:
  user["friends"] = []


#for t in friendships:
  #print(t) -> Mostra tudo
  #Desenpacotar o pacote/ vai mostar o 0 e depois o 1
  #print(t[0])
  #print(t[1])

#Desenpacotar automatico
for i, j in friendships:
  #print(i)
  #print(j)
  users[i]["friends"].append(users[j])
  users[j]["friends"].append(users[i])

#print(users)
def number_of_friends (user):
  return len(user["friends"])

#print (number_of_friends(users[0]))

total_connections = sum([number_of_friends(u) for u in users])
#print (total_connections)

num_users = len(users)
avg_connections = total_connections / num_users
#print(avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
#print(num_friends_by_id)

lista_ordenada = sorted(num_friends_by_id, key=lambda num_friends: num_friends[1], reverse = True)
#print (lista_ordenada)

def friends_of_friends_ids_bad(user):
  return [
    foaf["id"]
    for friend in user["friends"]
    for foaf in friend["friends"]
  ]

def not_the_same(user, other_user):
  return user["id"] != other_user["id"]

def not_friends (user, other_user):
  return all(not_the_same(friend, other_user) for friend in user['friends'])
#print([not_the_same(friend, users[0]) for friend in users[1]['friends']])

#print (not_friends(users[0], users[9]))

def friends_of_friends_ids (user):
  return set([
    foaf["id"]
    for friend in user['friends']
    for foaf in friend["friends"]
    if not_the_same(user, foaf)
    and not_friends(user, foaf)
  ])

#print (friends_of_friends_ids(users[0]))


#Counter: Conta quantas vezes determinada coisa aparece em uma coleção, devolve dicionario de frequencias
#fazer importação
#teste = [1, 2, 5, 4, 3, 2, 1, 2 ,3, 2, 1]
#c = Counter(teste)
#print (c)


def friends_of_friends_ids_frequency (user):
  return Counter([
    foaf["id"]
    for friend in user["friends"]
    for foaf in friend['friends']
    if not_the_same(user, foaf)
    and not_friends(user, foaf)
  ])

#print (friends_of_friends_ids_frequency(users[4]))

# tupla de interesses
interests = [
  (0, "Haddoop"), (0, "Big Data"), (0, "Java"),
  (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
  (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
  (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
  (2, "numpy"), (2, "statsmodel"), (2, "pandas"), (3, "R"), (3, "Python"),
  (3, "statistics"), (3, "regression"), (3, "probability"),
  (4, "machine learning"), (4, "regression"), (4, "decision trees"),
  (4, "libsvm"), (5, "Python"), (5, "R"),(5, "Java"), (5, "C++"),
  (5, "Haskell"), (5, "programming languages"), (6, "theory"),
  (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
  (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
  (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
  (9, "Java"), (9, "MapReduce"), (9, "Big Data"), 
]

def data_scientists_who_like(target_interest):
  return [
    user_id for user_id, interest in interests if interest == target_interest
  ]

print (data_scientists_who_like("Big Data"))

