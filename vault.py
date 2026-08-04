class AlienVault:
  def __init__(self,occupant=None):
    self.occupant = occupant

  def capture(self,alien_name):
    self.occupant = alien_name
    print(f'SYSTEM: {alien_name} has been secured in the vault.')

  def __str__(self):
    return f'Vault occupant: {self.occupant}'