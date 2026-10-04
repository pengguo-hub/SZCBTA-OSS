import random
import json
import numpy as np
import matplotlib.pyplot as plt

# 生成的商品各自占用空间
def generate_item_sizes(total_items, size_range):
    item_sizes = [random.randint(size_range[0], size_range[1]) for _ in range(total_items)]
    return item_sizes

# 为每个区域分配容量
def generate_zone_capacities(total_zones, item_sizes):
    total_capacity = sum(item_sizes)  # 计算商品总占用空间
    base_capacity = total_capacity // total_zones  # 每个区域初始容量（整数部分）
    remaining_capacity = total_capacity % total_zones  # 剩余容量

    # 均匀分配剩余容量
    
    zone_capacities = [base_capacity for _ in range(total_zones)]
    for i in range(remaining_capacity):
        zone_capacities[i] += 1

    return total_capacity, zone_capacities

def get_order_item(probabilities):
    # 根据归一化的概率随机选择一个商品
    item = random.choices(range(total_items), weights=probabilities, k=1)[0]
    return item

def get_order(order_size, order_lb, order_ub, delivery_date_range):
    orders = []
    delivery_dates = []
    for _ in range(order_size):
        num_items = random.randint(order_lb, order_ub)
        order = [get_order_item(probabilities) for _ in range(num_items)]
        orders.append(order)
        # 为每个订单随机分配一个交货期
        delivery_date = random.randint(delivery_date_range[0], delivery_date_range[1])
        delivery_dates.append(delivery_date)
    return orders , delivery_dates


# 商品总数
total_items = 50
# 定义指数衰减的速率
decay_rate = 0.05 # 衰减率，可根据需要调整

# 计算每种商品的出现概率
probabilities = [np.exp(-decay_rate * i) for i in range(total_items)]

# 归一化概率，确保它们的和为1
probabilities = [p / sum(probabilities) for p in probabilities]
order_lb = 5  # 每个订单包含的商品数量下界
order_ub = 20
order_size = 100
delivery_date_range = (3, 20)  # 订单交货时间
item_size_range = (1.0, 10.0)  # 商品占用空间范围
workbench_capacity = 3  # 工作台容量
total_zones = 5         # 总区域数量
picker_capacity = [5] * total_zones  # 各区域拣货员一次可拣货数量



# 生成商品的占用空间大小
item_sizes = generate_item_sizes(total_items, item_size_range)

# 为每个区域分配总容量
total_capacity, zone_capacities = generate_zone_capacities(total_zones, item_sizes)

orders, delivery_dates = get_order(order_size, order_lb, order_ub, delivery_date_range)
print("订单生成完成！")

output_data = {
    "orders": orders,
    "delivery_dates": delivery_dates,
    "item_sizes": item_sizes,
    "total_capacity": total_capacity,
    "zone_capacities": zone_capacities,
    "workbench_capacity": workbench_capacity,
    "total_zones": total_zones,
    "picker_capacity": picker_capacity,
    "total_items": total_items,
    "order_size" : order_size
}

# print(output_data)
# 将订单信息写入json文件
with open ('./json_order', "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=4)

