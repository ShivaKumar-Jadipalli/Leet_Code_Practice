class Solution:
    def mostPopularCreator(self, creators, ids, views):
        n = len(creators)
        creator_data = {}   # Value: [total_view, most_view_video, most_view_video_view]
        for i in range(n):
            if creators[i] in creator_data:
                view_datas = creator_data[creators[i]]
                view_datas[0] += views[i]
                if views[i] > view_datas[2] or (views[i] == view_datas[2] and ids[i] < view_datas[1]):
                    view_datas[1] = ids[i]
                    view_datas[2] = views[i]
            else:
                creator_data[creators[i]] = [views[i], ids[i], views[i]]

        max_view_creators = [None]
        max_view = -1
        for creator in creator_data:
            view_data = creator_data[creator]
            if view_data[0] > max_view:
                max_view_creators = [[creator, view_data[1]]]
                max_view = view_data[0]
            elif view_data[0] == max_view:
                max_view_creators.append([creator, view_data[1]])

        return max_view_creators
    

