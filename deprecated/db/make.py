fout = open('populate_countries.py', 'w')

fout.write('from django.core.management.base import BaseCommand\n')
fout.write('from beer.models import Country\n\n\n')
fout.write('class Command(BaseCommand):\n')
fout.write('\tdef _create_tags(self):\n')

with open('countries.txt', 'r') as fin:
    for line in fin:
        fout.write('\t\tcountry = Country(name=\'{0}\')\n'.format(line.strip()))
        fout.write('\t\tcountry.save()\n\n')

fout.write('\n')
fout.write('\tdef handle(self, *args, **options):\n')
fout.write('\t\tself._create_tags()')
fout.close()
