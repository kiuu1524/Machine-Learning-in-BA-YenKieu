from flask import Flask
from flaskext.mysql import MySQL
import pandas as pd
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
app = Flask(__name__)

def getConnect(server, port, database, username, password):
    try:
        mysql = MySQL()

        app.config['MYSQL_DATABASE_HOST'] = server
        app.config['MYSQL_DATABASE_PORT'] = port
        app.config['MYSQL_DATABASE_DB'] = database
        app.config['MYSQL_DATABASE_USER'] = username
        app.config['MYSQL_DATABASE_PASSWORD'] = password

        mysql.init_app(app)
        conn = mysql.connect()
        return conn
    except mysql.connector.Error as e:
        print("Error =", e)
    return None
# Function to close MySQL connection
def closeConnection(conn):
    if conn is not None:
        conn.close()

# Function to execute query and return dataset
def queryDataset(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall())
    return df

# Kết nối đến database
conn = getConnect('localhost', 3306, 'salesdatabase', 'root', 'Yk12345678')

# Truy vấn dữ liệu từ bảng customer
sql1 = "SELECT * FROM customer"
df1 = queryDataset(conn, sql1)

# In kết quả
print(df1)


# Truy vấn dữ liệu từ hai bảng customer và customer_spend_score
sql2 = "SELECT DISTINCT customer.CustomerId, Age, Annual_Income, Spending_Score " \
       "FROM customer, customer_spend_score " \
       "WHERE customer.CustomerId = customer_spend_score.CustomerID"

df2 = queryDataset(conn, sql2)

# Đặt tên cột cho DataFrame
df2.columns = ['CustomerId', 'Age', 'Annual Income', 'Spending Score']

# In dữ liệu
print(df2)
print(df2.head())       # In 5 dòng đầu tiên
print(df2.describe())   # Thống kê dữ liệu


def showHistogram(df, columns):
    plt.figure(1, figsize=(7, 8))
    n = 0
    for column in columns:
        n += 1
        plt.subplot(3, 1, n)
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        sns.histplot(df[column], bins=32, kde=True)
        plt.title(f'Histogram of {column}')

    plt.show()


# Gọi hàm để hiển thị biểu đồ histogram
showHistogram(df2, df2.columns[1:])

def elbowMethod(df, columnsForElbow):
    X = df.loc[:, columnsForElbow].values
    inertia = []

    for n in range(1, 11):
        model = KMeans(
            n_clusters=n,
            init='k-means++',
            max_iter=500,
            random_state=42
        )
        model.fit(X)
        inertia.append(model.inertia_)

    plt.figure(1, figsize=(15, 6))
    plt.plot(np.arange(1, 11), inertia, 'o')
    plt.plot(np.arange(1, 11), inertia, '-', alpha=0.5)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Cluster sum of squared distances')
    plt.show()

# Gọi hàm elbowMethod với dataframe và cột cần sử dụng
columns = ['Age', 'Spending Score']
elbowMethod(df2, ['Annual Income', 'Spending Score'])

from sklearn.cluster import KMeans

def runKMeans(X, cluster):
    model = KMeans(n_clusters=cluster,
                   init='k-means++',
                   max_iter=500,
                   random_state=42)

    model.fit(X)
    labels = model.labels_
    centroids = model.cluster_centers_
    y_kmeans = model.fit_predict(X)

    return y_kmeans, centroids, labels

X = df2.loc[:, columns].values
cluster = 4
colors = ["red", "green", "blue", "purple", "black", "pink", "orange"]

y_kmeans, centroids, labels = runKMeans(X, cluster)

print(y_kmeans)
print(centroids)
print(labels)

df2["cluster"] = labels


def visualizeKMeans(X, y_kmeans, cluster, title, xlabel, ylabel, colors):
    plt.figure(figsize=(10, 10))
    for i in range(cluster):
        plt.scatter(X[y_kmeans == i, 0],
                    X[y_kmeans == i, 1],
                    s=100,
                    c=colors[i],
                    label='Cluster %i' % (i + 1))

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

visualizeKMeans(
    X,
    y_kmeans,
    cluster,
    "Clusters of Customers - Age X Spending Score",
    "Age",
    "Spending Score",
    colors
)

X = df2.loc[:, columns].values
cluster=5

y_kmeans, centroids, labels=runKMeans(X, cluster)

print(y_kmeans)
print(centroids)
print(labels)
df2["cluster"]=labels

visualizeKMeans(X,
y_kmeans,
cluster,
"Clusters of Customers - Annual Income X Spending Score",
"Annual Income",
"Spending Score",
colors)
