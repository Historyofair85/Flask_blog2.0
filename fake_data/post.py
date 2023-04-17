from faker import Faker
from datetime import datetime

fake = Faker()

posts = []

for i in range(1, 11):
    posts.append(
        {
            'id': 1,
            'title': fake.paragraph(),
            'image': f'https://picsum.photos/500?random={i}',
            'date_created': datetime.now()
        }
    )