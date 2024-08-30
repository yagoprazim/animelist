import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Anime, Gender

json_file_path = os.path.join(os.path.dirname(__file__), 'initial_data.json')

if os.path.exists(json_file_path):
    print(f'Loading initial data from {json_file_path}')
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        for entry in data:
            name = entry['name']
            gender = entry['gender']
            release_date = entry['release_date']
            seasons = entry['seasons']
            total_episodes = entry['total_episodes']
            image = entry.get('image', None)

            gender_value = Gender(gender).value if isinstance(gender, int) else gender

            anime, created = Anime.objects.update_or_create(
                name=name,
                defaults={
                    'gender': gender_value,
                    'release_date': release_date,
                    'seasons': seasons,
                    'total_episodes': total_episodes,
                    'image': image
                }
            )
            
            if created:
                print(f'Successfully created {anime.name}')
            else:
                print(f'Successfully updated {anime.name}')
else:
    print(f'{json_file_path} does not exist')
