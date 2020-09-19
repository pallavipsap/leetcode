# similar to course scheduling problem
from collections import deque

class Solution:
    # Time : O(c)
    # queue : all characters O(c), only 26 characters
    # build graph: all possible characters in dictionary O(c); n*m ;  n is len of words, m is avg len of word
    # Space :
    # O(V+E)

    '''
    - adding chaarcter to queue is tricky [ char - 'a'] gives the index
    - every time u want index, indegrees[ord(char) - ord('a')]
    - while setting values for dictionary, which is a set; do d[c] = {}
    -queue = deque();  queue.append(char), to add character
    - edge cases :
    ["za","zb","ca","cb"], non-connected graphs ; op: "abzc"
    ["abc","ab"] ; op = ""
        - we never go inside if(fc!=sc)

    ["ab","abc"]

    '''

    global d
    global indegrees
    d = {}  # adjacency matrix
    indegrees = [0] * 26  # array of 26 letters

    def alienOrder(self, words: List[str]) -> str:

        result = ""
        self.buildGraph(words)
        queue = deque()

        # Now come back here from build graph function, now the map is filled, graph is build
        # add the char to queue, if indegrees value is 0
        for c in d:  # c is char
            print(d)
            if indegrees[
                ord(c) - ord('a')] == 0:  # add to queue only those which are presnt as keys in map and indegrees as 0
                queue.append(c)  # add char to queue

        print('q', queue)
        while queue:  # O(c) = O(mn)

            c = queue.popleft()  # remove the char from queue
            result += c  # add it to result string

            # iterate on edges of c, that is in map
            edges = d[c]
            for edge in edges:  # edges is set of chars # No. of edges ( O(V+E))
                indegrees[ord(edge) - ord('a')] -= 1  # reduce indegree of char
                if indegrees[ord(edge) - ord('a')] == 0:  # add to queue if indegrees becomes 0
                    queue.append(edge)
        print(result)

        # to check if the indegrees of all chars have become 0, we can compare size of map with result string
        # if cycle we get emplty string, [abc,ab] gives empty string
        if len(d) != len(result):
            return ""

        return result

    def buildGraph(self, words):

        # build structure of adjacency matrix
        # key = char ( out ), val = set ( in )

        # this is an IMPORTANT so that we get all letters in the given input in the map
        for word in words:
            for c in word:
                if c not in d:
                    d[c] = {}  # value is a set

        # print(d)

        for i in range(len(words) - 1):  # iterating through words array
            print(indegrees)

            word1 = words[i]
            word2 = words[i + 1]

            word1_len = len(words[i])
            word2_len = len(words[i + 1])

            # edge case ["abc","ab"]
            if word1_len > word2_len and word1.startswith(word2):
                d.clear()
                break  # we go out, we need not go inside for loop

            # comparing two words in words array, and fill the map
            # Fill indegrees array simultaneously
            j = 0
            while j < word1_len and j < word2_len:
                fc = word1[j]  # first char
                sc = word2[j]  # second char

                # eg. wrt, wrf
                # first char = t, second char = f ; t->f ; t(out and key), f (in and value)
                if fc != sc:

                    out = fc
                    ind = sc
                    x = d[out]
                    print('x', x)

                    # if we do not put the below condition, we increase indegrees twice for 'b'
                    # eg. ["za","zb","ca","cb"]
                    if ind not in x:
                        d[out] = set(ind)  # here we are adding to hash set
                        indegrees[ord(ind) - ord('a')] += 1  # go to that particular index and increase indegrees number
                    break  # break out at first different character
                j += 1


