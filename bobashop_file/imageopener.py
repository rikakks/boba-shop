from PIL import Image
tea = raw_input("Type menu name: ")
tea = tea.replace(' ', '')
toppings = raw_input("Did you add any toppings?")
if toppings.lower() == 'pearls' or toppings.lower() == 'pearls':
    toppings = '_pearls'
elif toppings.lower() == 'lychee':
    toppings = '_lychee'
elif toppings.lower() == 'grass jelly' or toppings.lower() == 'grassjelly':
    toppings = '_grassjelly'
elif toppings.lower() == 'creama' or toppings.lower() == 'cream':
    toppings = '_creama'
else:
    toppings = ''

boba = tea + toppings

address = boba + ".png"
im = Image.open(address)
im.show()
