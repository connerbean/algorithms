class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # Just run BFS on the list
        # Rooms in the format of rooms[roomID][roomsItUnlocks]
        
        if len(rooms) == 0:
            return False
        
        stack = []                      # stack contains roomIds
        visited = set()                 # visited roomIds
        stack.append(0)                 # if we're ok - start with first room
        
        while((len(stack) > 0) and len(visited) < len(rooms)):
            roomId = stack[0]
            stack.pop(0)
            visited.add(roomId)         # add to visited, process it
            room = rooms[roomId]        # room is list of roomIDs it unlocks
            
            # Add each room it can unlock to the stack
            for unlock in room:
                if unlock not in visited:
                    stack.append(unlock)
    
        return len(visited) == len(rooms) 