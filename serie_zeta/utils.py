from django.db.models import Case, When, Value, CharField
from serie_zeta.models import Team, Player
import random, string

position_order = Case(
    When(position=Player.GOALKEEPER, then=Value('Portiere')),
    When(position=Player.DEFENDER, then=Value('Difensore')),
    When(position=Player.MIDFIELDER, then=Value('Centrocampista')),
    When(position=Player.FORWARD, then=Value('Attaccante')),
    When(position=Player.COACH, then=Value('Allenatore')),
    output_field=CharField(),
)

def get_random_string(length=8):
    """Return a random string of length characters."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))