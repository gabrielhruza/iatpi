from graphviz import Digraph

f = Digraph('finite_state_machine', filename='fsm.gv')
f.attr(size='10')

f.attr('node', shape='doublecircle')
f.node('LR_0')


f.attr('node', shape='circle')
f.edge('LR_0', 'LR_0', label='SS(B)')
f.edge('LR_0', 'LR_1', label='SS(S)')


f.view()