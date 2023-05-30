import nuke

for node in nuke.allNodes('Read'):
    node['localizationPolicy'].setValue('on')