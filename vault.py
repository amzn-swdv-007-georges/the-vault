class AlienVault:
  def __init__(self,occupant=None):
    self.occupant = occupant
    self.containment_level = 100 
    self.temperature = 20 
    self.oxygen_level = 21 

  def capture(self,alien_name):
    self.occupant = alien_name
    print(f'SYSTEM: {alien_name} has been secured in the vault.')
  
  def greet_alien(self):
    if self.occupant is None:
      return f'SYSTEM: The vault is empty.'
    return f'{self.occupant} responds with strange look.'


  def __str__(self):
    # Display the new environmental controls.
    return (
            f"Occupant: {self.occupant}\n"
            f"Containment: {self.containment_level}%\n"
            f"Temperature: {self.temperature}°C\n"
            f"Oxygen: {self.oxygen_level}%"
        )

  