def is_lattice_point_with_distance_5(x1, y1, x2, y2):
    # 距離が5になる相対的な座標のリスト
    distance_5_offsets = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    # x1, y1 からの距離が5の点を列挙し、x2, y2 からの距離も確認
    for dx, dy in distance_5_offsets:
        nx, ny = x1 + dx, y1 + dy
        if (nx - x2) ** 2 + (ny - y2) ** 2 == 5:
            return "Yes"
    
    return "No"

# 入力の読み取り
x1, y1, x2, y2 = map(int, input().split())
print(is_lattice_point_with_distance_5(x1, y1, x2, y2))
