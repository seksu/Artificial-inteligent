class State:
	def __init__(self ,M = 0 ,C = 0 ,B = 0):
		self.M = M
		self.C = C
		self.B = B
	def __str__(self):
		return "State = " + str(self.get())
	def sent_2M(self):
		if(self.B == 0):
			return State(self.M+2, self.C, 1)
		else:
			return State(self.M-2, self.C, 0)
	def sent_2C(self):
		if(self.B == 0):
			return State(self.M, self.C+2, 1)
		else:
			return State(self.M, self.C-2, 0)
	def sent_1C(self):
		if(self.B == 0):
			return State(self.M, self.C+1, 1)
		else:
			return State(self.M, self.C-1, 0)
	def sent_1M(self):
		if(self.B == 0):
			return State(self.M+1, self.C, 1)
		else:
			return State(self.M-1, self.C, 0)
	def sent_1C1M(self):
		if(self.B == 0):
			return State(self.M+1, self.C+1, 1)
		else:
			return State(self.M-1, self.C-1, 0)
	def check_rule(self): 			# check if this state is possible depend on rule 
		return (True if self.M == 0 else self.M >= self.C) and \
			   (True if self.M == start_Missionary else start_Missionary - self.M >= start_Canibal - self.C) and \
			   (self.M >= 0 and self.M <= start_Missionary) and (self.C >= 0 and self.C <= start_Canibal)
	def get(self):
		return [self.M, self.C, self.B]
	def print_state(self):
		print("Missionary = " ,self.M ,",Canibal = " ,self.C ,",Boat = " ,self.B , "(left)" if self.B == 0 else "(right)")

class Node:  			# node collect state and next node
	def __init__(self, state = None, path = [], path_action = None):
		self.state = state
		self.next = []
		self.path = path
		if path_action != None :
			self.path.append(path_action)
		self.actions = [state.sent_2M, state.sent_1M, state.sent_2C, state.sent_1C, state.sent_1C1M]
	def __str__(self):
		return "Node state = " + str(self.state.get()) + ", Next node = " + str(len(self.next)) + " node" + ", Path = " + str(self.path)
	def add_next(self, node):
		self.next.append(node)
	def get_depth(self):
		return len(self.path)

def DLS(node, depth): 	# depth limited search input root and depth to search return None if no final state
	def genNode(node):
		for count, action in enumerate(node.actions):
			temp = action()
			if(temp.check_rule()): 		# if this state pass
				node.add_next(Node(temp, node.path[:], count)) 		# add new node to node.next[]
	def checkNode(node):    # return True if this node have final state
		return True if node.state.get() == [start_Missionary, start_Canibal, 1] else False

	queue = [node]
	while queue : 		# the search stop when nothing in queue
		ptr = queue.pop(0)				# search sequence is    check answer, check depth gen node and enqueue gen node
		if checkNode(ptr) :
			return ptr 			# if it's final answer return node of final state
		if ptr.get_depth() < depth :
			genNode(ptr)
			queue = ptr.next + queue     # result = [next node  , in queue node]
		#print(ptr)
	return None

while 1 :
	start_Missionary = int(input("Start Missionary : "))
	start_Canibal = int(input("Start Canibal : "))
	if start_Canibal >  start_Missionary :
		print("Canibal must equal or lower then missionary.")
		continue
	break

#start_Missionary = 3
#start_Canibal = 3


for i in range(100):				# Iterative Deepening Search
	root = Node(State(0,0,0))   	# start state
	result = DLS(root, i)
	if result != None :
		break

# root = Node(State(0,0,0))   	# Depth Limited Search
# result = DLS(root, 11)


#testing
print(root)
print(result)

#
print(root.next)
while 1:
	pass