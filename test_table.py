table=[]

class Person:
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand


def query(name):
    p1=Person(name,[])
    table.append(p1)



# print(p1.hand)

# p1.hand.append('cum')
# print(type(p1.hand))

# while len(table)<5:
#     x=input('Who are you? ')
#     query(x)

# print(table)


dict_={
    
}

# print(dict_['item2'])



def add(name):
    dict_.update({name:{'player hand':[],'dealer hand':[],'player hand count':[],'dealer hand count':[]}})

# add('jack')

# print(dict_)

# print('before')
# print(dict_['jack']['player_hand'])

# lst=[5,5]
# dict_['jack']['player_hand']=lst

# print(dict_['jack'])

# dict_['jack']['player_hand'].pop()

# print(dict_['jack']['player_hand'])

# print(sum(dict_['jack']['player_hand']))