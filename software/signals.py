from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import SoftwareType

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


