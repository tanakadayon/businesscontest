import pymysql
from faker import Faker
import random

# ダミーデータ生成用のFakerオブジェクトを作成
fake = Faker()

# MySQLデータベースに接続
connection = pymysql.connect(host='localhost', user='root', password='eiko3150', db='mirugigu')

# カーソルを取得
cursor = connection.cursor()

# アーティストテーブルのダミーデータ生成
for _ in range(10000):
    artist_name = fake.unique.first_name() + ' ' + fake.unique.last_name()
    genre = random.choice(['弾き語り', 'ロック', 'DJ', 'HIPHOP'])
    region = fake.unique.state()
    years_active = random.randint(1, 20)

    # SQL文でアーティストテーブルにデータを挿入
    insert_artist_sql = "INSERT INTO artist (name, genre, region, years_active) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_artist_sql, (artist_name, genre, region, years_active))

# ライブハウステーブルのダミーデータ生成
for _ in range(10000):
    livehouse_name = fake.unique.company()
    address = fake.address()
    phone_number = fake.unique.phone_number()
    email = fake.unique.email()
    genres = random.sample(['ロック', '弾き語り', 'DJ', 'HIPHOP'], random.randint(1, 4))
    genre_str = ', '.join(genres)

    # SQL文でライブハウステーブルにデータを挿入
    insert_livehouse_sql = "INSERT INTO livehouse (name, address, phone, email, genre) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_livehouse_sql, (livehouse_name, address, phone_number, email, genre_str))

# 変更をコミット
connection.commit()

# 接続をクローズ
connection.close()
