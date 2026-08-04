class AlienVault:
  def __init__(self,occupant=None):
    self.occupant = occupant

  def capture(self,alien_name):
    self.occupant = alien_name
    print(f'SYSTEM: {alien_name} has been secured in the vault.')
  
  def greet_alien(self):
    if self.occupant is None:
      return f'SYSTEM: The vault is empty.'
    return f'{self.occupant} responds with strange look.'


  def __str__(self):
    return f'Vault occupant: {self.occupant}'

  