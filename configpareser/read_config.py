import configparser

config = configparser.ConfigParser()
config.sections()

config.read('example.ini')

print(config.sections())

print('forge.example' in config)

print('python.org' in config)

print(config['forge.example']['User'])

print(config['DEFAULT']['Compression']) 

topsecret = config['topsecret.server.example']
print(topsecret['ForwardX11'])  
print(topsecret['Port'])  

for key in config['forge.example']:  
    print(key)