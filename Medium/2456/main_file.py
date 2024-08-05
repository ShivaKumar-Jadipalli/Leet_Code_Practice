from collections import defaultdict
class Solution:
    def dictonary_structure(self):
        return {"ids":[],"views":[]}
    def mostPopularCreator(self, creators, ids, views):
        database = defaultdict(self.dictonary_structure)
        creator_max = -1
        answers = []
        for i,j,k in zip(creators,ids,views):
            database[i]["ids"].append(j)
            database[i]["views"].append(k)
            total_views = sum(database[i]["views"])
            if total_views > creator_max:
                creator_max = total_views
                popular_creator = [i]
            elif total_views == creator_max:
                popular_creator.append(i)
        for creator in set(popular_creator): # assuming ids are unique 
            views_max = -1
            for count,value in enumerate(database[creator]['views']):
                if value > views_max:
                    views_max = value
                    ids_max = [database[creator]['ids'][count]]
                elif value == views_max:
                    ids_max.append(database[creator]['ids'][count])
            answers.append([creator,min(ids_max)])
        return answers

print(Solution().mostPopularCreator(["bb","bb"],["baa","bba"],[1,0]))       # [["bb","baa"]]...