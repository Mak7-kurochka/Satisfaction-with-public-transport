#Here i importing all libraries which will use in work
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

#Selecting a style for plots
plt.style.use('fivethirtyeight')

#Reading a table which i want to annalise
_ = pd.read_csv('Zadowolenie z komunikacji miejskiej mieszkańców Krakowa (Responses).csv')

#Dropping two columns beacuse i don't need them
_.drop(columns=['Timestamp', 'Email Address'], inplace=True)
df = _[:259]

#Creating a functionsthat will help me write less lines 
def create_pie(name_file):
    
    #I starting analysis by creation a new table with counts of reccuring values
    fstdf = pd.DataFrame(df[name_file].value_counts())
    #Creating a list which contain all indexes. I'll use them like a legend fro the plot
    age = list(fstdf.index)

    #Creating a variable which will be used as values for the plot
    count = []
    #
    for i in range(fstdf[name_file].count()):
        count.append(fstdf[name_file][i])

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

        plt.show()

def create_bar(name_file, inp=None):
        for rr in df[name_file]:
            if rr == int or rr == float:
                break
            else:
                break
        if type(rr) == int or type(rr) == float:
            for_bar = pd.DataFrame(df[name_file].value_counts())
            name_f_b = list(for_bar.index)
            numb = list(for_bar[name_file])

            plt.bar(name_f_b, numb)

            plt.tight_layout()

            plt.title(name_file)

            plt.show()

        else:
            my_counter = Counter()

            for response in df[name_file]:
                if type(response) == str:
                    my_counter.update(response.split(','))
                smo = []
                popularity = []

            for item in my_counter.most_common(15):
                smo.append(item[0])
                popularity.append(item[1])
            
            if inp == 'h':
                plt.barh(smo, popularity)
                plt.gca().invert_yaxis()
            else:
                plt.bar(smo, popularity)
            plt.tight_layout()
            plt.title(name_file)
            plt.show()
