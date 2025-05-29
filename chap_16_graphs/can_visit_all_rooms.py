def can_visit_all_rooms(rooms) -> bool:
    visited = set()
    def dfs(room):
        if room in visited:
            return
        visited.add(room)
        for key in rooms[room]:
             dfs(key)
    dfs(0)
    return len(visited == len(rooms))


# def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         keys = set()
#         for i in range(len(rooms)):
#             if i == 0:
#                 self.add_keys(rooms[i],keys)
#                 continue
#             if i not in keys:
#                 return False
#             else:
#                 self.add_keys(rooms[i],keys)
#             print(keys)
        
#         return True

#     def add_keys(self, room, keys):
#             for i in room:
#                 keys.add(i)