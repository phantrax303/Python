def dictXML(xmlCandidate,root='root', recursion=False):
  if type(xmlCandidate) is not dict:
    return false
  xml = ''
  for key in xmlCandidate:
    if type(xmlCandidate[key]) is list:
      for value in xmlCandidate[key]:
        xml += f'<{key}>{value}</{key}>'
    elif type(xmlCandidate[key]) is dict:
      xml += f'<{key}>{dictXML(xmlCandidate[key],recursion=True)}</{key}>'
    else:
      xml += f'<{key}>{xmlCandidate[key]}</{key}>'
  if not recursion: 
    xml = f'<{root}>{xml}</{root}>'
  return xml