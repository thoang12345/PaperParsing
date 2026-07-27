from Functions import system

system.giveGPUstatus()

from marker.renderers.markdown import MarkdownOutput
import inspect

print(inspect.getsource(MarkdownOutput))
