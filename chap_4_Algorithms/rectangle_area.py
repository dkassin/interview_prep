## First Solution
def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x1,x2,y1,y2 = [ax1, bx1],[ax2,bx2],[ay1,by1],[ay2,by2]
        array_of_rect = []
        area_array = []
        for i in range(2):
            corner_1 = (x1[i],y1[i])
            corner_2 = (x1[i],y2[i])
            corner_3 = (x2[i],y2[i])
            corner_4 = (x2[i],y1[i])
            area_of_rect = (x2[i] - x1[i]) * (y2[i] - y1[i])
            area_array.append(area_of_rect)
            array_of_rect.append(([corner_1,corner_2,corner_3,corner_4],area_of_rect))
        overlap_rect = []
        print(array_of_rect)
        corner_1_overlap = [max(array_of_rect[0][0][0][0], array_of_rect[1][0][0][0]),max(array_of_rect[0][0][0][1], array_of_rect[1][0][0][1])]
        corner_2_overlap = [max(array_of_rect[0][0][1][0], array_of_rect[1][0][1][0]),min(array_of_rect[0][0][1][1], array_of_rect[1][0][1][1])]
        corner_3_overlap = [min(array_of_rect[0][0][2][0], array_of_rect[1][0][2][0]),min(array_of_rect[0][0][2][1], array_of_rect[1][0][2][1])]
        corner_4_overlap = [min(array_of_rect[0][0][3][0], array_of_rect[1][0][3][0]),max(array_of_rect[0][0][3][1], array_of_rect[1][0][3][1])]
        area_of_overlap_rect = (corner_3_overlap[0] - corner_1_overlap[0]) * (corner_3_overlap[1] - corner_1_overlap[1])
        area = area_array[0] + area_array[1] - (area_of_overlap_rect)
        return (area)

def computeArea_2(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x1,x2,y1,y2 = [ax1, bx1],[ax2,bx2],[ay1,by1],[ay2,by2]
        array_of_rect = []
        area_array = []
        for i in range(2):
            corner_1 = (x1[i],y1[i])
            corner_2 = (x1[i],y2[i])
            corner_3 = (x2[i],y2[i])
            corner_4 = (x2[i],y1[i])
            area_of_rect = (x2[i] - x1[i]) * (y2[i] - y1[i])
            area_array.append(area_of_rect)
            
  
        
        corner_1_overlap = [max(x1),max(y1)]
        corner_2_overlap = [max(x1),min(y2)]
        corner_3_overlap = [min(x2),min(y2)]
        corner_4_overlap = [min(x2),max(y1)]
        overlap_x = [max(x1),min(x2)]
        overlap_y = [max(y1),min(y2)]

        area_of_overlap_rect = (overlap_x[0] - overlap_x[1]) * (overlap_y[0] - overlap_y[1])
        area = area_array[0] + area_array[1] - (area_of_overlap_rect)
        return (area)