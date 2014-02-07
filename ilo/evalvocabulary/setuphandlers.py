from collective.grok import gs
from ilo.evalvocabulary import MessageFactory as _

@gs.importstep(
    name=u'ilo.evalvocabulary', 
    title=_('ilo.evalvocabulary import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ilo.evalvocabulary.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
