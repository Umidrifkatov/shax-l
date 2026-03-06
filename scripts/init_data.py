import os
from django.utils.text import slugify
from apps.services.models import Service

services_data = [
    {
        'slug': 'auto',
        'icon': 'truck',
        'category': 'auto',
        'title_ru': 'Автоперевозки',
        'title_uz_cyrl': 'Автотранспорт ташувлари',
        'title_uz_latn': 'Avtotransport tashuvlari',
        'description_ru': 'Надежные автомобильные перевозки по СНГ, Европе и Азии. Собственный и привлеченный парк техники.',
        'description_uz_cyrl': 'МДҲ, Европа ва Осиё бўйлаб ишончли автотранспорт ташувлари.',
        'description_uz_latn': 'MDH, Yevropa va Osiyo bo\'ylab ishonchli avtotransport tashuvlari.',
        'order': 1
    },
    {
        'slug': 'air',
        'icon': 'plane',
        'category': 'air',
        'title_ru': 'Авиаперевозки',
        'title_uz_cyrl': 'Авиаташувлар',
        'title_uz_latn': 'Aviatashuvlar',
        'description_ru': 'Самый быстрый способ доставки грузов по всему миру. Прямые контракты с авиалиниями.',
        'description_uz_cyrl': 'Бутун дунё бўйлаб юкларни етказиб беришнинг энг тезкор усули.',
        'description_uz_latn': 'Butun dunyo bo\'ylab yuklarni yetkazib berishning eng tezkor usuli.',
        'order': 2
    },
    {
        'slug': 'rail',
        'icon': 'train',
        'category': 'rail',
        'title_ru': 'Железнодорожные перевозки',
        'title_uz_cyrl': 'Темир йўл ташувлари',
        'title_uz_latn': 'Temir yo\'l tashuvlari',
        'description_ru': 'Оптимальное сочетание цены и сроков. Перевозки в вагонах, полувагонах и на платформах.',
        'description_uz_cyrl': 'Нарх ва муддатнинг оптимал комбинацияси.',
        'description_uz_latn': 'Narx va muddatning optimal kombinatsiyasi.',
        'order': 3
    },
    {
        'slug': 'sea',
        'icon': 'ship',
        'category': 'sea',
        'title_ru': 'Морские перевозки',
        'title_uz_cyrl': 'Денгиз ташувлари',
        'title_uz_latn': 'Dengiz tashuvlari',
        'description_ru': 'Контейнерные перевозки из любой точки мира. Работаем со всеми крупнейшими портами.',
        'description_uz_cyrl': 'Дунёнинг исталган нуқтасидан контейнер ташувлари.',
        'description_uz_latn': 'Dunyoning istalgan nuqtasidan konteyner tashuvlari.',
        'order': 4
    }
]

def run():
    print("Seeding services...")
    for item in services_data:
        service, created = Service.objects.update_or_create(
            slug=item['slug'],
            defaults=item
        )
        if created:
            print(f"Created service: {service.title_ru}")
        else:
            print(f"Updated service: {service.title_ru}")

if __name__ == "__main__":
    run()
