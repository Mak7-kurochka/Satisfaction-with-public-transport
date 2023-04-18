import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

df = pd.read_csv('Zadowolenie z komunikacji miejskiej mieszkańców Krakowa (Responses).csv')
df.drop(columns=['Timestamp', 'Email Address'], inplace=True)

def create_pie(name_file):
    fstdf = pd.DataFrame(df[name_file].value_counts())
    age = list(fstdf.index)

    count = []
    for i in range(fstdf[name_file].count()):
        count.append(fstdf[name_file][i])
    for i in range(len(count)): count[i] *= 100

    inp = input('Maybe you want add a title for legend table?: ')
    if inp == 'Yes' or inp == 'yes':
        name_table = input('Enter a title: ')
        plt.pie(count,
            autopct = '%1.1f%%', pctdistance=1.15)

        plt.legend(age, loc='center right', title=name_table, 
                   bbox_to_anchor=(1, 0, 0.5, 0), fontsize='12')

        plt.title(name_file, fontsize=15)
    else:
        plt.pie(count,
            autopct = '%1.1f%%', pctdistance=1.15)

        plt.legend(age, loc='center right', bbox_to_anchor=(1, 0, 0.5, 0), fontsize='12')

        plt.tight_layout()

        plt.title(name_file)

def create_bar_for_str(name_file):
    my_counter = Counter()

    for response in df[name_file]:
        my_counter.update(response.split(','))
    smo = []
    popularity = []

    for item in my_counter.most_common(15):
        smo.append(item[0])
        popularity.append(item[1])
    smo, popularity

    plt.barh(smo, popularity)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.title(name_file)
