class AlienVault:
  def __init__(self,occupant=None,c=100):
    self.occupant = occupant
    self.__containment_level = c
    self.__temperature = 20 
    self.__oxygen_level = 21 
    self.__responses = {
      "hello": "Greetings, carbon-construct.",
      "escape": "Your structures are temporary.",
      "name": "I am designated Gorgax."
    }

  def capture(self,alien_name):
    self.occupant = alien_name
    print(f'SYSTEM: {alien_name} has been secured in the vault.')
  
  def greet_alien(self):
    if self.occupant is None:
      return f'SYSTEM: The vault is empty.'
    return f'{self.occupant} responds with strange look.'

  def reinforce(self,amount):
    self.__containment_level = min(100,self.__containment_level+amount)

  def weaken(self,amount):
    self.__containment_level = max(0,self.__containment_level-amount)

  def emergency_lockdown(self):
    self.__containment_level = 100

  def status(self):
    return f'Containment: {self.__containment_level}'

  def ask(self,question):
    question = question.lower()

    for key in self.__responses:
      if key in question:
        return self.__responses[key]


  def __str__(self):
    # Display the new environmental controls.
    return (
            f"Occupant: {self.occupant}\n"
            f'{self.status()}'           
        )  

if __name__ == "__main__":
  vault = AlienVault('Gorgax')

  choice = input('Choice (a/s/x): ')
  
  while choice != 'x':
    print(vault.ask(input('Ask: ')))
    choice = input('Choice (a/s/x): ')