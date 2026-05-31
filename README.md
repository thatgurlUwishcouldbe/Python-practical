import pandas as pd
import matplotlib.pyplot as plt

#df.isna() تطلع null

df = pd.read_csv('/content/raw_data.csv')


df['Age'].fillna(df['Age'].median(), inplace=True) #استبدال النلز بالمتوسط
df.drop('Cabin', axis=1, inplace=True)#حذف العامود كامل
df = df.dropna(subset=['Embarked'])#حذف صفوف النلز
#df.isnull().sum()

# task1
#more = df[df['Fare'] > 35]
#less = df[df['Fare'] <= 35]


#moreR = more['Survived'].mean()
#lessR = less['Survived'].mean()

#plt.bar(['>35', '<=35'], [moreR, lessR])
#plt.ylabel('Survival Rate')
#plt.show()

# task2
#df['Sex'].isnull().sum()
#df.groupby('Sex')['Survived'].mean()

#plt.ylabel('Survival Rate')
#plt.show()

# task3
#class_rate = df.groupby('Pclass')['Survived'].mean()

#print(class_rate)

#class_rate.plot(kind='bar')
#plt.title('Survival Rate by Passenger Class')
#plt.ylabel('Survival Rate')
#plt.show()

# task4
def classify_age(age):
    if age < 13:
        return 'Child'
    elif age < 25:
        return 'Young'
    else:
        return 'Adult'

#بداية الحل
df['AgeGroup'] = df['Age'].apply(classify_age)

ageR = df.groupby('AgeGroup')['Survived'].mean()

print(ageR)

ageR.plot(kind='bar')
plt.title('Survival Rate by Age Group')
plt.ylabel('Survival Rate')
plt.show()
