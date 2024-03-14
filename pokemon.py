import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests

st.title('Pokemon Explorer!')

### Display image of pokemon (latest sprite from front) --stretch--> cycle through many sprites
### Make it look better
### Add the audio of the latest battle cry
### Use whole pokedex

# @st.cache_data
def get_all_id_numbers():
    # code to get all numbers
    return list_of_all_numbers

def get_details(poke_number):
    ''' Create an entry for our favourite pokemon '''
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
        response = requests.get(url)
        pokemon = response.json()
        return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']), pokemon['sprites']['front_default'], pokemon['sprites'],pokemon['cries']['legacy'],pokemon['types'][0]['type']['name']
    except:
        return 'Error', np.NAN, np.NAN, np.NAN, np.NAN, np.NAN,np.NAN,np.NAN ##



pokemon_number = st.slider('Pick a pokemon', min_value=1, max_value=500)


name, height, weight, moves, front_default, sprites, legacy_cry, type = get_details(pokemon_number)
height = height * 10
image_urls = list(sprites.values())
height_data = pd.DataFrame({'Pokemon':['Weedle',name.title(),'nidoqueen'],
               'Heights':[30,height,130]
              })
if type=='grass':
    color = 'green'
elif type=='bug':
    color = 'brown'
elif type=='fairy':
    color = 'pink'
elif type=='fighting':
    color = 'blue'
elif type=='electric':
    color = 'yellow'
elif type=='water':
    color = 'blue'
elif type=='fire':
    color = 'orange'

else:
    color = 'black'

colors = ['gray',color,'gray']
st.image(front_default,use_column_width=True)
st.image(image_urls[0:7:2])
st.audio(legacy_cry, format='audio/mp3')
graph = sns.barplot(data = height_data,
                    x = 'Pokemon',
                    y = 'Heights',
                    palette = colors)

st.write(f'Name:{name.title()}')
st.write(f'Height:{height}')
st.write(f'Weight:{weight}')
st.write(f'Moves:{moves}')
st.write(f'Type:{type}')

st.pyplot(graph.figure)

