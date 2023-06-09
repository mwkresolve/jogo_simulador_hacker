from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import SoftwareType, Software
from core.models import Jogador
from .utils import get_software_name

@receiver(post_migrate)
def create_default_software_types(sender, **kwargs):
    if sender.name == 'software':
        # Verifica se já existem tipos de software cadastrados
        existing_types = SoftwareType.objects.exists()
        if not existing_types:
            # Cria os tipos de software
            software_types = [
                {'type_id': '1', 'description': 'Cracker'},
                {'type_id': '2', 'description': 'Hasher'},
                {'type_id': '3', 'description': 'Port Scan'},
                {'type_id': '4', 'description': 'Firewall'},
                {'type_id': '5', 'description': 'Hidder'},
                {'type_id': '6', 'description': 'Seeker'},
                {'type_id': '7', 'description': 'Anti-Virus'},
                {'type_id': '8', 'description': 'Spam'},
                {'type_id': '9', 'description': 'Warez'},
                {'type_id': '10', 'description': 'DDoS'},
                {'type_id': '11', 'description': 'Collector'},
                {'type_id': '12', 'description': 'Breaker'},
                {'type_id': '13', 'description': 'FTP Exploit'},
                {'type_id': '14', 'description': 'SSH Exploit'},
                {'type_id': '15', 'description': 'Nmap'},
                {'type_id': '16', 'description': 'Analyzer'},
                {'type_id': '17', 'description': 'Torrent'},
                {'type_id': '20', 'description': 'Miner'},

            ]

            # Cria os tipos de software no banco de dados
            for software_type in software_types:
                SoftwareType.objects.create(**software_type)

@receiver(post_migrate)
def create_bot_softwares(sender, **kwargs):
    if sender.name == 'software':
        # Verifica se existem bots com o nome "zeroguy"
        if Jogador.objects.filter(username='ZeroGuy', is_bot=True).exists():
            # Obtém o bot "zeroguy"
            zeroguy = Jogador.objects.get(username='ZeroGuy', is_bot=True)

            # Cria os softwares para o bot "zeroguy"
            software_types = SoftwareType.objects.all()

            for software_type in software_types:
                Software.objects.create(user=zeroguy,
                                        soft_name='Baby',
                                        type_of_software=software_type,
                                        soft_version=1,
                                        soft_size = 100,
                                        soft_ram = 10)

        # Obtém todos os bots, excluindo o bot "zeroguy"
        bots = Jogador.objects.filter(is_bot=True).exclude(username='ZeroGuy')

        # Obtém as instâncias dos tipos de software
        cracker_type = SoftwareType.objects.get(type_id=1)  # ID do tipo de software "Cracker"
        hasher_type = SoftwareType.objects.get(type_id=2)  # ID do tipo de software "Hasher"

        # Cria os softwares "Cracker" e "Hasher" em ordem crescente de versão
        cracker_version = 2
        hasher_version = 1
        # Define os valores iniciais para soft_size e soft_ram
        soft_size = 100
        soft_ram = 10


        for bot in bots:
            Software.objects.create(user=bot, soft_name=get_software_name(cracker_version), type_of_software=cracker_type, soft_version=cracker_version,
                                    soft_size=soft_size, soft_ram=soft_ram)
            Software.objects.create(user=bot, soft_name=get_software_name(cracker_version), type_of_software=hasher_type, soft_version=hasher_version,
                                    soft_size=soft_size, soft_ram=soft_ram)

            soft_size += 100
            soft_ram += 10
            cracker_version += 1
            hasher_version += 1


