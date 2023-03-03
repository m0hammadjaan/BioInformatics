# class SuffixTree:
#     def __init__(self, text):
#         self.text = text  # store the input text
#         self.edges = {}  # mapping from parent node to a list of (start, end, child) triples
#         self.nodes = {}  # mapping from node to a list of (start, end) pairs
#         self.current_node = 0
#         self.remaining = 0
#         self.active_node = 0
#         self.active_edge = 0
#         self.active_length = 0

#     def add_char(self, char):
#         self.remaining += 1
#         last_added_node = None
#         while self.remaining > 0:
#             if self.active_length == 0:
#                 self.active_edge = len(self.text) - self.remaining
#             if self.active_edge not in self.edges:
#                 self.edges[self.active_edge] = self.current_node
#                 last_added_node = self.current_node
#                 self.current_node += 1
#             else:
#                 next_node = self.edges[self.active_edge]
#                 if char in self.text[self.nodes[next_node][0]:self.nodes[next_node][1] + 1]:
#                     self.active_length += 1
#                     break
#                 if char < self.text[self.nodes[next_node][0]]:
#                     self.nodes[next_node] = (char, self.nodes[next_node][0])
#                     self.edges[self.active_edge] = self.current_node
#                     last_added_node = self.current_node
#                     self.current_node += 1
#                 else:
#                     self.nodes[next_node] = (self.nodes[next_node][0], char)
#             self.remaining -= 1
#             if self.active_node == 0:
#                 self.active_length -= 1
#                 self.active_edge = len(self.text) - self.remaining
#             else:
#                 self.active_node = self.parent[self.active_node]
#                 self.active_length = self.length[self.active_node]
#         return last_added_node


#     def build_tree(self, text):
#         self.parent = {}  # mapping from node to its parent node
#         self.length = {}  # mapping from node to the length of the edge leading to it
#         self.parent[0] = -1
#         self.length[0] = 0
#         for i, char in enumerate(text):
#             last_added_node = self.add_char(char)
#             if last_added_node is not None:
#                 self.parent[last_added_node] = self.active_node
#                 self.length[last_added_node] = self.active_length
#         return self.parent, self.length

#     def find_longest_common_substring(self, tree):
#         # Traverse the suffix tree and keep track of the longest common substring found so far
#         longest_common_substring = ""
#         current_substring = ""
#         stack = [(0, 0)]
#         while stack:
#             node, depth = stack.pop()
#             if node in tree.nodes:
#                 current_substring += tree.text[tree.nodes[node][0]:tree.nodes[node][1] + 1]
#                 # Update the longest common substring if the current substring is longer
#                 if len(current_substring) > len(longest_common_substring):
#                     longest_common_substring = current_substring
#                 for edge in tree.edges[node]:
#                     stack.append((edge[2], depth + edge[1] - edge[0] + 1))
#             else:
#                 current_substring = current_substring[:depth]
#         return longest_common_substring


# def main(strings):
#     # Concatenate the strings and add a unique separator between each one
#     text = "".join(strings) + "$"

#     # Construct the suffix tree for the text
#     tree = SuffixTree(text)
#     tree.build_tree(text)

#     # Find the longest common substring by traversing the suffix tree
#     common_substring = tree.find_longest_common_substring(tree)

#     return common_substring

# # Example usage
# strings = ["ATATCGTCGATCGTACGTA", "TATCGATCGATCGTACGTA", "ATCGTCGATCGTACGTAAT"]
# print(main(strings))  # Output: "ATCGTACGTA"





print()