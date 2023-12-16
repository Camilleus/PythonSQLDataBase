from faker import Faker
import random
import sqlite3

fake = Faker()

conn = sqlite3.connect('university.db')
cursor = conn.cursor()